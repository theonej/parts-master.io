#!/usr/bin/env python3
"""
Create draft post files from rows in content/calendar.tsv.

Scaffolded files carry `draft: true`, so the daily cron can never publish an
unwritten stub just because its date arrived. Remove that line when the post is
finished and it will publish on its date.

Usage:
  python tools/scaffold.py 2026-08-28              one date
  python tools/scaffold.py 2026-09-01 2026-09-30   inclusive range
  python tools/scaffold.py --next 7                next 7 unwritten entries
  python tools/scaffold.py --list                  unwritten entries, no files

Existing files are never overwritten.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CALENDAR = ROOT / "content" / "calendar.tsv"
POSTS = ROOT / "content" / "posts"

TEMPLATE = """---
title: {title}
date: {date}
tag: {tag}
description: {angle}
draft: true
---

<!-- Angle: {angle} -->
<!-- Delete the `draft: true` line above to publish this on {date}. -->

Opening paragraph: the concrete situation this post is about.

## First section

Body.

> A point worth pulling out of the surrounding paragraphs.

## Second section

Body.

## Closing

What to actually do.
"""


def load_calendar() -> list[dict]:
    if not CALENDAR.exists():
        sys.exit(f"scaffold: {CALENDAR.relative_to(ROOT)} not found")

    rows = []
    for number, line in enumerate(
        CALENDAR.read_text(encoding="utf-8").splitlines()[1:], start=2
    ):
        if not line.strip():
            continue
        fields = line.split("\t")
        if len(fields) < 5:
            sys.exit(f"scaffold: {CALENDAR.name} line {number}: expected 5 columns")
        date, tag, slug, title, angle = (f.strip() for f in fields[:5])
        try:
            dt.date.fromisoformat(date)
        except ValueError:
            sys.exit(f"scaffold: {CALENDAR.name} line {number}: bad date {date!r}")
        rows.append(
            {"date": date, "tag": tag, "slug": slug, "title": title, "angle": angle}
        )
    return rows


def written_dates() -> set[str]:
    """Dates that already have a post file, draft or not."""
    found = set()
    for path in POSTS.glob("*.md"):
        match = re.match(r"^(\d{4}-\d{2}-\d{2})-", path.stem)
        if match:
            found.add(match.group(1))
    return found


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__.strip())

    rows = load_calendar()
    have = written_dates()
    unwritten = [r for r in rows if r["date"] not in have]

    if args[0] == "--list":
        for row in unwritten:
            print(f"{row['date']}  {row['tag']:<14} {row['title']}")
        print(f"\n{len(unwritten)} unwritten of {len(rows)} calendar entries")
        return

    if args[0] == "--next":
        count = int(args[1]) if len(args) > 1 else 1
        selected = unwritten[:count]
    elif len(args) == 2:
        start, end = args
        selected = [r for r in rows if start <= r["date"] <= end]
    else:
        selected = [r for r in rows if r["date"] == args[0]]
        if not selected:
            sys.exit(f"scaffold: no calendar entry for {args[0]}")

    created = skipped = 0
    for row in selected:
        target = POSTS / f"{row['date']}-{row['slug']}.md"
        if target.exists():
            skipped += 1
            continue
        target.write_text(TEMPLATE.format(**row), encoding="utf-8")
        print(f"created {target.relative_to(ROOT)}")
        created += 1

    print(f"scaffold: {created} created, {skipped} already existed")
    if created:
        print("scaffold: these are drafts — remove `draft: true` to publish")


if __name__ == "__main__":
    main()
