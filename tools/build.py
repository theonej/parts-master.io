#!/usr/bin/env python3
"""
Static site generator for parts-master.io.

Renders content/posts/*.md into dist/, skipping any post whose date is in the
future. That skip is the whole scheduling mechanism: the deploy workflow runs
once a day, and each morning the next post simply becomes eligible. Nothing
needs to be merged or edited to release it.

Environment:
  PUBLISH_DATE   ISO date to treat as today (default: today's date in UTC).
  PUBLISH_ALL    Set to 1 to render future posts too, for local preview.
"""

from __future__ import annotations

import datetime as dt
import html
import math
import os
import re
import shutil
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "content" / "posts"
STATIC_DIR = ROOT / "static"
OUT_DIR = ROOT / "dist"

SITE_TITLE = "parts-master.io"
# Absolute base for canonical and Open Graph URLs. Facebook and other scrapers
# resolve link previews from these, so they cannot be relative. Override with
# the SITE_URL environment variable once a custom domain is in use.
DEFAULT_SITE_URL = "https://theonej.github.io/parts-master.io"
# An unset GitHub Actions variable arrives as an empty string rather than being
# absent, so fall back on falsiness rather than on os.environ.get's default.
SITE_URL = (os.environ.get("SITE_URL") or DEFAULT_SITE_URL).strip().rstrip("/")
# Optional absolute URL of a preview image used in link cards.
OG_IMAGE = os.environ.get("OG_IMAGE", "").strip()
TAGLINE = (
    "Field notes on high-end coffee bar design, espresso machine installation "
    "and service. Written from behind the bar and under the panels — "
    "specifications, commissioning, and the failures that keep repeating."
)
FAVICON = (
    "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' "
    "viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚙️</text></svg>"
)
WORDS_PER_MINUTE = 220

FRONT_MATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)
DATE_PREFIX = re.compile(r"^(\d{4}-\d{2}-\d{2})-")

warnings: list[str] = []


def fail(message: str) -> None:
    sys.exit(f"build: error: {message}")


def warn(message: str) -> None:
    warnings.append(message)


def parse_post(path: Path) -> dict:
    """Split a post into its front matter and rendered-ready body."""
    match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        fail(f"{path.name}: missing '---' front matter block")

    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            fail(f"{path.name}: front matter line is not 'key: value': {line!r}")
        key, value = line.split(":", 1)
        value = value.strip()
        # Titles containing a colon are often quoted out of YAML habit. Front
        # matter here is parsed on the first colon only, so the quotes would
        # otherwise render literally.
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1].strip()
        meta[key.strip().lower()] = value

    for required in ("title", "date", "description"):
        if not meta.get(required):
            fail(f"{path.name}: front matter is missing {required!r}")

    try:
        date = dt.date.fromisoformat(meta["date"])
    except ValueError:
        fail(f"{path.name}: date must be YYYY-MM-DD, got {meta['date']!r}")

    # The filename prefix is what sorts the directory for a human; a mismatch
    # against the real date means one of the two is a typo.
    prefix = DATE_PREFIX.match(path.stem)
    if not prefix:
        fail(f"{path.name}: filename must start with YYYY-MM-DD-")
    if prefix.group(1) != meta["date"]:
        warn(f"{path.name}: filename date differs from front matter {meta['date']!r}")

    body = match.group(2)
    words = len(re.findall(r"[\w'’-]+", body))

    return {
        "slug": path.stem[len(prefix.group(0)) :],
        "title": meta["title"],
        "date": date,
        "tag": meta.get("tag", ""),
        "description": meta["description"],
        "body": body,
        "minutes": max(1, math.ceil(words / WORDS_PER_MINUTE)),
        # Scaffolded posts carry draft: true so an unwritten stub can never be
        # published by the daily cron just because its date arrived.
        "draft": meta.get("draft", "").lower() in ("true", "yes", "1"),
    }


def load_posts() -> list[dict]:
    files = sorted(POSTS_DIR.glob("*.md"))
    if not files:
        fail(f"no posts found in {POSTS_DIR.relative_to(ROOT)}")

    posts = [parse_post(path) for path in files]

    by_slug: dict[str, str] = {}
    by_date: dict[dt.date, str] = {}
    for post in posts:
        if post["slug"] in by_slug:
            fail(f"duplicate slug {post['slug']!r} (also in {by_slug[post['slug']]})")
        by_slug[post["slug"]] = post["title"]
        if post["date"] in by_date:
            warn(
                f"two posts share {post['date']}: {by_date[post['date']]!r} "
                f"and {post['title']!r} — both publish that day"
            )
        by_date[post["date"]] = post["title"]

    return posts


def report_coverage(posts: list[dict], today: dt.date) -> None:
    """Compare the editorial calendar against posts that actually exist.

    The calendar is a planning document, not an input to the build — a dated row
    with no written post simply means no post that day. This prints what is
    missing so the gap is visible rather than discovered on the morning.
    """
    calendar = ROOT / "content" / "calendar.tsv"
    if not calendar.exists():
        return

    scheduled: dict[dt.date, str] = {}
    for line in calendar.read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        fields = line.split("\t")
        if len(fields) < 4:
            continue
        try:
            scheduled[dt.date.fromisoformat(fields[0])] = fields[3]
        except ValueError:
            continue

    if not scheduled:
        return

    have = {p["date"] for p in posts if not p["draft"]}
    missing = sorted(d for d in scheduled if d not in have)
    if not missing:
        print(f"build: calendar fully written ({len(scheduled)} entries)")
        return

    overdue = [d for d in missing if d <= today]
    horizon = today + dt.timedelta(days=14)
    imminent = [d for d in missing if today < d <= horizon]

    print(
        f"build: calendar {len(scheduled) - len(missing)}/{len(scheduled)} written, "
        f"{len(missing)} unwritten"
    )
    if overdue:
        print(
            f"build: WARNING {len(overdue)} calendar date(s) already passed with no "
            f"post — earliest {overdue[0]} {scheduled[overdue[0]]!r}"
        )
    if imminent:
        print(f"build: next 14 days needs {len(imminent)} post(s):")
        for d in imminent:
            print(f"build:   {d}  {scheduled[d]}")


def fmt_date(date: dt.date) -> str:
    return f"{date.day} {date:%B %Y}"


def render_markdown(body: str) -> str:
    md = markdown.Markdown(extensions=["tables", "smarty"])
    rendered = md.convert(body)
    # Wide tables scroll inside their own box so the page never scrolls sideways.
    return rendered.replace('<table>', '<div class="table-scroll"><table>').replace(
        "</table>", "</table></div>"
    )


def layout(
    *,
    title: str,
    description: str,
    body: str,
    depth: int,
    path: str = "",
    og_type: str = "website",
    published: dt.date | None = None,
    og_title: str | None = None,
) -> str:
    """Wrap page content in the shared shell.

    depth = directories below root, for relative asset links.
    path   = this page's location below the site root, for absolute URLs.
    """
    up = "../" * depth
    canonical = f"{SITE_URL}/{path}" if path else f"{SITE_URL}/"
    esc = lambda s: html.escape(s, quote=True)

    image_tags = ""
    if OG_IMAGE:
        image_tags = f"""
    <meta property="og:image" content="{esc(OG_IMAGE)}" />
    <meta name="twitter:card" content="summary_large_image" />"""
    else:
        image_tags = """
    <meta name="twitter:card" content="summary" />"""

    article_tags = ""
    if published is not None:
        article_tags = (
            f'\n    <meta property="article:published_time" '
            f'content="{published:%Y-%m-%d}" />'
        )

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(title)}</title>
    <meta name="description" content="{esc(description)}" />
    <link rel="canonical" href="{esc(canonical)}" />
    <meta property="og:site_name" content="{esc(SITE_TITLE)}" />
    <meta property="og:type" content="{esc(og_type)}" />
    <meta property="og:title" content="{esc(og_title or title)}" />
    <meta property="og:description" content="{esc(description)}" />
    <meta property="og:url" content="{esc(canonical)}" />{article_tags}{image_tags}
    <link rel="stylesheet" href="{up}styles.css" />
    <link rel="icon" href="{esc(FAVICON, )}" />
  </head>
  <body>
    <div class="wrap">
{body}
    </div>
  </body>
</html>
"""


def post_meta_line(post: dict) -> str:
    bits = [f'<time datetime="{post["date"]:%Y-%m-%d}">{fmt_date(post["date"])}</time>']
    if post["tag"]:
        bits.append(html.escape(post["tag"]))
    bits.append(f'{post["minutes"]} min read')
    return " · ".join(bits)


def render_post(post: dict, newer: dict | None, older: dict | None) -> str:
    nav = ""
    if newer or older:
        links = []
        if older:
            links.append(
                f'<a class="prev" href="{older["slug"]}.html">'
                f'<span class="meta">Previous</span>{html.escape(older["title"])}</a>'
            )
        if newer:
            links.append(
                f'<a class="next" href="{newer["slug"]}.html">'
                f'<span class="meta">Next</span>{html.escape(newer["title"])}</a>'
            )
        nav = f'\n      <nav class="post-nav">{"".join(links)}</nav>'

    body = f"""      <p><a class="backlink" href="../">← {SITE_TITLE}</a></p>

      <article class="prose">
        <header>
          <p class="meta">{post_meta_line(post)}</p>
          <h1 class="post-title">{html.escape(post["title"])}</h1>
          <p class="standfirst">{html.escape(post["description"])}</p>
        </header>

{render_markdown(post["body"])}
      </article>{nav}

      <footer>
        <p><a class="backlink" href="../">← All posts</a></p>
      </footer>"""

    return layout(
        title=f'{post["title"]} — {SITE_TITLE}',
        description=post["description"],
        body=body,
        depth=1,
        path=f'blog/{post["slug"]}.html',
        og_type="article",
        published=post["date"],
        # Link cards show og:site_name separately, so the suffix is redundant.
        og_title=post["title"],
    )


def render_index(published: list[dict], pending: int) -> str:
    items = []
    for post in published:
        items.append(
            f"""          <li>
            <a href="blog/{post["slug"]}.html">
              <span class="meta">{post_meta_line(post)}</span>
              <h3>{html.escape(post["title"])}</h3>
              <p>{html.escape(post["description"])}</p>
            </a>
          </li>"""
        )

    note = ""
    if pending:
        word = "post" if pending == 1 else "posts"
        note = (
            f'\n        <p class="pending">{pending} more {word} scheduled — '
            "a new one publishes each morning.</p>"
        )

    body = f"""      <header>
        <span class="mark" aria-hidden="true">⚙</span>
        <h1>parts&#8209;master<span class="tld">.io</span></h1>
        <p class="lede">{TAGLINE}</p>
      </header>

      <main>
        <h2 class="meta">Latest</h2>
        <ul class="posts">
{chr(10).join(items)}
        </ul>{note}
      </main>

      <footer>
        <p>Coffee bar installation and service notes.</p>
      </footer>"""

    return layout(
        title=SITE_TITLE, description=TAGLINE, body=body, depth=0, path=""
    )


def main() -> None:
    if os.environ.get("PUBLISH_DATE"):
        try:
            today = dt.date.fromisoformat(os.environ["PUBLISH_DATE"])
        except ValueError:
            fail(f"PUBLISH_DATE must be YYYY-MM-DD, got {os.environ['PUBLISH_DATE']!r}")
    else:
        today = dt.datetime.now(dt.timezone.utc).date()

    publish_all = os.environ.get("PUBLISH_ALL") == "1"

    posts = load_posts()
    # Newest first, and stable for same-day posts.
    posts.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)

    drafts = [p for p in posts if p["draft"]]
    finished = [p for p in posts if not p["draft"]]

    published = (
        finished if publish_all else [p for p in finished if p["date"] <= today]
    )
    pending = len(finished) - len(published)

    if not published:
        fail(f"no posts are published as of {today} — nothing to deploy")

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)
    shutil.copytree(STATIC_DIR, OUT_DIR, dirs_exist_ok=True)

    blog_dir = OUT_DIR / "blog"
    blog_dir.mkdir()
    for index, post in enumerate(published):
        newer = published[index - 1] if index > 0 else None
        older = published[index + 1] if index + 1 < len(published) else None
        (blog_dir / f'{post["slug"]}.html').write_text(
            render_post(post, newer, older), encoding="utf-8"
        )

    (OUT_DIR / "index.html").write_text(
        render_index(published, pending), encoding="utf-8"
    )

    for message in warnings:
        print(f"build: warning: {message}")
    print(
        f"build: {len(published)} published, {pending} scheduled"
        f"{f', {len(drafts)} draft' if drafts else ''} "
        f"(as of {today}{' — PUBLISH_ALL' if publish_all else ''})"
    )
    if published:
        print(f"build: newest is {published[0]['date']} {published[0]['title']!r}")
    report_coverage(posts, today)


if __name__ == "__main__":
    main()
