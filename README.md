# parts-master.io

Static site for parts-master.io. Posts are written in Markdown and published to
GitHub Pages by GitHub Actions. **A post goes live on the date in its front
matter** — the daily workflow run releases it, with nothing to merge or edit.

## Layout

| Path | Purpose |
| --- | --- |
| `content/posts/*.md` | One file per post. Filename must start `YYYY-MM-DD-`. |
| `content/calendar.tsv` | Editorial calendar: one planned topic per day. Planning only — not a build input. |
| `static/` | Copied to the site root as-is (`styles.css`, `404.html`). |
| `tools/build.py` | Generator. Renders posts, skips future dates and drafts, writes `dist/`. |
| `tools/scaffold.py` | Creates draft post files from calendar rows. |
| `dist/` | Build output. Git-ignored; never edit by hand. |
| `.github/workflows/deploy-pages.yml` | Build and deploy pipeline. |

## How scheduling works

`tools/build.py` omits any post dated later than today from the build entirely.
The workflow runs on a daily cron, so each morning the next post becomes
eligible and gets published.

Future posts are therefore **absent from the deployed site**, not hidden in it —
there is no URL to guess and nothing in the HTML. Note the one caveat: this
repository is public, so scheduled posts are readable in `content/posts/` on
GitHub before their release date. Make the repository private if that matters.

The date comparison uses **UTC**. A post dated `2026-08-05` publishes on the
first run at or after 00:00 UTC that day — in practice the 13:05 UTC run.

### Two things the cron depends on

1. **GitHub only fires `schedule` from the workflow file on the default
   branch.** The default branch is currently `main`, and deploys come from
   `develop`. So either make `develop` the default branch, or keep this workflow
   file present on `main` too. The checkout step is pinned to `ref: develop`, so
   a cron firing from `main` still builds `develop`'s content.
2. **Scheduled runs are queued and can be delayed** during periods of high load
   on GitHub's infrastructure. Treat 13:05 UTC as "shortly after", not exact.

Making `develop` the default branch is the simpler path — it also resolves the
environment restriction in first-time setup below.

## First-time setup

Both steps need repo-admin access and are done once, in the GitHub UI.

1. **Settings → Pages → Build and deployment → Source: GitHub Actions.**
   Without this the workflow runs but has nothing to publish to.

2. **Settings → Environments → `github-pages` → add `develop` to the allowed
   deployment branches.** Enabling Pages creates this environment restricted to
   the default branch. Until `develop` is added, deploys fail with
   `Branch "develop" is not allowed to deploy to github-pages due to
   environment protection rules`. Making `develop` the default branch also
   resolves this.

## Writing a post

Create `content/posts/YYYY-MM-DD-some-slug.md`:

```markdown
---
title: Water Is the Install: Specifying Treatment
date: 2026-07-27
tag: Installations
description: One sentence. Used as the standfirst and the meta description.
---

Body in Markdown. `##` and `###` for headings — `#` is not used, the title
comes from the front matter.

Blockquotes render as callouts:

> The point worth pulling out of the surrounding paragraphs.

Tables are supported and scroll horizontally on narrow screens.
```

- `title`, `date` and `description` are required; `tag` is optional.
- The filename date must match the `date` field — the build warns if not.
- Colons in the title are fine and do not need quoting; front matter is parsed
  as `key: value` on the first colon only, not as real YAML.
- The URL is the filename with the date prefix stripped:
  `content/posts/2026-07-27-water-treatment.md` → `/blog/water-treatment.html`.
- Reading time is computed from word count. Previous/next links are generated
  across published posts only.

The build fails loudly on a missing required field, a bad date, or a duplicate
slug, and warns on two posts sharing a date.

## Local preview

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

.venv/bin/python tools/build.py                    # as it will look today
PUBLISH_ALL=1 .venv/bin/python tools/build.py       # including scheduled posts
PUBLISH_DATE=2026-08-15 .venv/bin/python tools/build.py   # as of a given date

python3 -m http.server -d dist 8000                # http://localhost:8000
```

`PUBLISH_DATE` is the useful one for checking that a future post renders
correctly before its release date.

## Changing the schedule

- **Move a post:** rename the file and edit its `date`. Both must agree.
- **Publish early:** set the date to today and push, or run the workflow
  manually from the Actions tab.
- **Hold a post:** push its date into the future. It disappears from the site on
  the next build.
- **Change the daily release time:** edit the `cron` expression in the workflow.
  It is UTC.

## The editorial calendar

`content/calendar.tsv` plans one topic per day for a full year — 2026-08-28 to
2027-07-26 — with a date, tag, slug, title and a one-line angle for each. It is
a **planning document**: the build never reads it as content. A calendar row
with no corresponding post simply means no post that day.

The build reports coverage against it on every run:

```
build: calendar 11/333 written, 322 unwritten
build: next 14 days needs 14 post(s):
build:   2026-09-08  Sulphate, Silica and the Minor Ions
```

It also warns if a calendar date has passed with nothing written, so the gap
surfaces in the deploy log rather than on the morning.

### Drafting from the calendar

```sh
.venv/bin/python tools/scaffold.py --list          # what is unwritten
.venv/bin/python tools/scaffold.py --next 7        # scaffold the next 7
.venv/bin/python tools/scaffold.py 2026-09-08      # one specific date
.venv/bin/python tools/scaffold.py 2026-09-01 2026-09-30   # a range
```

Scaffolded files carry `draft: true`. **A draft is never published, even once
its date has passed** — so an unwritten stub cannot be pushed live by the daily
cron. Delete the `draft: true` line when the post is finished and it publishes
on its date. Existing files are never overwritten.

## Current state

- **Written and scheduled:** 66 posts, one per day, 27 July – 30 September 2026.
- **Planned, not yet written:** 299 calendar entries, 1 October 2026 onward.

Monthly themes across the year: water chemistry and treatment (Sep) → the brew
group and brew path (Oct) → boilers and thermal systems (Nov) → grinders (Dec) →
electrics and control (Jan) → steam, milk and hot water (Feb) → plumbing, pumps
and pressure (Mar) → bar design and installation engineering (Apr) → diagnostics
and fault-finding (May) → service business and compliance (Jun) → extraction
science and dial-in (Jul).

## Facebook announcements

Every post that goes live is announced to a Facebook Page by the `announce`
job, which runs **only after a successful deploy** so the link cannot 404.

### Setup

1. **You need a Facebook Page.** Meta removed the ability to publish to
   personal profiles via the Graph API, so a Page is the only option.

2. **Create a Meta app** at developers.facebook.com and add the Pages API
   product.

3. **Generate a long-lived Page access token** with the `pages_manage_posts`
   and `pages_read_engagement` permissions. Short-lived tokens expire in about
   an hour; exchange for a long-lived user token, then request the Page token
   from it. Verify with the Access Token Debugger that it says
   `Expires: Never` and is a **Page** token, not a user token.

4. **Add repository secrets** — Settings → Secrets and variables → Actions:

   | Secret | Value |
   | --- | --- |
   | `FB_PAGE_ID` | Numeric Page id |
   | `FB_PAGE_ACCESS_TOKEN` | Long-lived Page access token |

5. **Optional repository variables:**

   | Variable | Purpose |
   | --- | --- |
   | `SITE_URL` | Absolute site base. Set when a custom domain is live. |
   | `OG_IMAGE` | Absolute URL of a link-card image. |
   | `FB_API_VERSION` | Graph API version. Defaults to `v21.0`. |

6. **Seed the ledger before enabling**, or the next run will announce recent
   back-catalogue posts:

   ```sh
   .venv/bin/python tools/announce.py --seed
   ```

   Then commit `content/announced.json`.

Until the secrets exist the job runs, reports that it is skipping, and exits
successfully — it never fails the deploy.

### Why it cannot double-post

The workflow runs on every push *and* daily on cron, so the same post is
evaluated many times. `content/announced.json` records every slug that has
been announced, with its Facebook post id, and is committed back to `develop`
by the job. Anything already in it is skipped.

Two further guards limit the damage if that ledger is ever lost or reset:

- `--max-age-days` (default 2) ignores posts published longer ago than that,
  so a reset ledger cannot republish the whole archive.
- `--max` (default 5) caps posts per run.

The ledger is saved after **each** successful post, so a failure partway
through a batch cannot cause the earlier ones to be sent again.

The commit is made with `GITHUB_TOKEN`, and commits made with that token do
not trigger workflows, so writing the ledger cannot cause a loop. The message
also carries `[skip ci]`.

### Testing without posting

```sh
.venv/bin/python tools/announce.py --dry-run      # print what would be sent
.venv/bin/python tools/announce.py --seed         # mark done, post nothing
```

### Permissions note

The `announce` job is the only one granted `contents: write`, and only so it
can commit the ledger. The workflow default remains `contents: read`.

### Open Graph

Post pages emit `og:title`, `og:description`, `og:url`, `og:type=article`,
`article:published_time` and a canonical link, so the Facebook link card
renders properly rather than as a bare URL. Set the `OG_IMAGE` variable to get
a large image card instead of a small one.

Graph API versions are deprecated roughly every two years. When `v21.0` is
retired, set the `FB_API_VERSION` variable rather than editing the script.

## Custom domain

The site is served from the default Pages URL. To move it to `parts-master.io`:

1. Add DNS at your registrar — four apex `A` records pointing at
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and
   `185.199.111.153`, or a `CNAME` to `theonej.github.io` for a `www` subdomain.
2. Enter the domain under **Settings → Pages → Custom domain**. GitHub commits a
   `CNAME` file; move it into `static/` so the build preserves it.
3. Wait for the certificate, then enable **Enforce HTTPS**.

Set the DNS records before entering the domain in settings — the other order
leaves the site unreachable while DNS propagates.
