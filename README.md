# parts-master.io

Static site for parts-master.io. Posts are written in Markdown and published to
GitHub Pages by GitHub Actions. **A post goes live on the date in its front
matter** — the daily workflow run releases it, with nothing to merge or edit.

## Layout

| Path | Purpose |
| --- | --- |
| `content/posts/*.md` | One file per post. Filename must start `YYYY-MM-DD-`. |
| `static/` | Copied to the site root as-is (`styles.css`, `404.html`). |
| `tools/build.py` | Generator. Renders posts, skips future dates, writes `dist/`. |
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

## Current schedule

32 posts, one per day, 27 July – 27 August 2026. Themes run roughly as
installation and site services → equipment specification and commissioning →
routine maintenance → diagnostics and faults → operations.

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
