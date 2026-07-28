#!/usr/bin/env python3
"""
Post newly published blog entries to a Facebook Page.

The deploy workflow runs on every push and once a day on cron, so this script
must be safe to run repeatedly. It is made idempotent by a committed ledger of
what has already been announced: content/announced.json. A post is announced
once, ever, and only after the site that hosts it has deployed.

Two further guards stop a bad day becoming a spam incident:

  --max-age-days  ignore posts published longer ago than this, so a lost or
                  reset ledger cannot re-announce the entire back catalogue.
  --max           hard cap on posts per run.

Environment:
  FB_PAGE_ID            Facebook Page numeric id.        Required to post.
  FB_PAGE_ACCESS_TOKEN  Long-lived Page access token.    Required to post.
  FB_API_VERSION        Graph API version. Default below.
  SITE_URL              Absolute site base, for links.

If either credential is missing the script exits successfully without posting,
so the deploy does not fail on repositories that have not configured this.

Usage:
  python tools/announce.py                 announce anything new
  python tools/announce.py --dry-run       show what would be posted
  python tools/announce.py --seed          mark everything published as done,
                                           without posting. Run this once when
                                           first enabling, to avoid announcing
                                           the existing back catalogue.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402  — reuse the generator's parsing and publish rules

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "content" / "announced.json"

DEFAULT_API_VERSION = "v21.0"
GRAPH = "https://graph.facebook.com"


def load_ledger() -> dict:
    if not LEDGER.exists():
        return {"announced": {}}
    try:
        data = json.loads(LEDGER.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"announce: {LEDGER.name} is not valid JSON: {exc}")
    data.setdefault("announced", {})
    return data


def save_ledger(ledger: dict) -> None:
    LEDGER.write_text(
        json.dumps(ledger, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def published_posts(today: dt.date) -> list[dict]:
    """Posts the site is actually serving, using the generator's own rules."""
    posts = build.load_posts()
    live = [p for p in posts if not p["draft"] and p["date"] <= today]
    live.sort(key=lambda p: (p["date"], p["slug"]))
    return live


def compose(post: dict, site_url: str) -> tuple[str, str]:
    link = f'{site_url}/blog/{post["slug"]}.html'
    tag = post.get("tag", "")
    lines = [post["title"], "", post["description"]]
    if tag:
        hashtag = "#" + "".join(w.capitalize() for w in tag.replace("&", " ").split())
        lines += ["", f"{hashtag} #Espresso #CoffeeBar"]
    return "\n".join(lines), link


def post_to_facebook(
    page_id: str, token: str, api_version: str, message: str, link: str
) -> str:
    """POST to the Page feed. Returns the created post id."""
    url = f"{GRAPH}/{api_version}/{page_id}/feed"
    payload = urllib.parse.urlencode(
        {"message": message, "link": link, "access_token": token}
    ).encode()
    request = urllib.request.Request(url, data=payload, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        # Never echo the token, which is in the request body rather than here.
        raise RuntimeError(f"Graph API {exc.code}: {detail}") from None
    except urllib.error.URLError as exc:
        raise RuntimeError(f"network error contacting Graph API: {exc.reason}") from None

    if "id" not in body:
        raise RuntimeError(f"unexpected Graph API response: {body}")
    return body["id"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="do not post")
    parser.add_argument(
        "--seed",
        action="store_true",
        help="mark all published posts as announced without posting",
    )
    parser.add_argument("--max", type=int, default=5, help="max posts per run")
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=2,
        help="ignore posts published more than this many days ago",
    )
    args = parser.parse_args()

    today = dt.datetime.now(dt.timezone.utc).date()
    # Empty string, not absence, is what an unset Actions variable looks like.
    site_url = (os.environ.get("SITE_URL") or build.SITE_URL).strip().rstrip("/")
    ledger = load_ledger()
    already = ledger["announced"]

    live = published_posts(today)

    if args.seed:
        stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        added = 0
        for post in live:
            if post["slug"] not in already:
                already[post["slug"]] = {
                    "date": post["date"].isoformat(),
                    "announced_at": stamp,
                    "facebook_post_id": None,
                    "seeded": True,
                }
                added += 1
        save_ledger(ledger)
        print(f"announce: seeded {added} post(s) as already announced, none posted")
        return

    cutoff = today - dt.timedelta(days=args.max_age_days)
    candidates = [
        p for p in live if p["slug"] not in already and p["date"] >= cutoff
    ]

    skipped_old = [p for p in live if p["slug"] not in already and p["date"] < cutoff]
    if skipped_old:
        print(
            f"announce: {len(skipped_old)} unannounced post(s) older than "
            f"{args.max_age_days} day(s) skipped — use --seed to mark them done"
        )

    if not candidates:
        print("announce: nothing new to announce")
        return

    if len(candidates) > args.max:
        print(
            f"announce: {len(candidates)} candidates, capping at {args.max} this run"
        )
        candidates = candidates[: args.max]

    page_id = os.environ.get("FB_PAGE_ID", "").strip()
    token = os.environ.get("FB_PAGE_ACCESS_TOKEN", "").strip()
    api_version = os.environ.get("FB_API_VERSION", "").strip() or DEFAULT_API_VERSION

    if args.dry_run:
        for post in candidates:
            message, link = compose(post, site_url)
            print(f"\n--- would post ({post['date']}) ---\n{message}\n{link}")
        print(f"\nannounce: dry run, {len(candidates)} post(s) not sent")
        return

    if not page_id or not token:
        print(
            "announce: FB_PAGE_ID or FB_PAGE_ACCESS_TOKEN not set — skipping. "
            f"{len(candidates)} post(s) remain unannounced."
        )
        return

    stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    failures = []
    for post in candidates:
        message, link = compose(post, site_url)
        try:
            post_id = post_to_facebook(page_id, token, api_version, message, link)
        except RuntimeError as exc:
            print(f"announce: FAILED {post['slug']}: {exc}", file=sys.stderr)
            failures.append(post["slug"])
            continue

        already[post["slug"]] = {
            "date": post["date"].isoformat(),
            "announced_at": stamp,
            "facebook_post_id": post_id,
        }
        # Persist after each success so a later failure cannot cause a repost.
        save_ledger(ledger)
        print(f"announce: posted {post['slug']} -> {post_id}")

    if failures:
        sys.exit(f"announce: {len(failures)} post(s) failed: {', '.join(failures)}")


if __name__ == "__main__":
    main()
