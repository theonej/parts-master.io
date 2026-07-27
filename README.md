# parts-master.io

Static site for parts-master.io, published to GitHub Pages by GitHub Actions on
every push to `develop`.

## Layout

| Path                                   | Purpose                                           |
| -------------------------------------- | ------------------------------------------------- |
| `site/`                                | Everything published. This directory is the web root. |
| `site/index.html`                      | Landing page.                                     |
| `site/styles.css`                      | Single stylesheet, light and dark.                |
| `site/404.html`                        | Served for unknown paths; styles are inlined on purpose. |
| `.github/workflows/deploy-pages.yml`   | Build and deploy pipeline.                        |

## First-time setup

Both steps need repo-admin access and are done once, in the GitHub UI.

1. **Settings → Pages → Build and deployment → Source: GitHub Actions.**
   Without this the workflow runs but has nothing to publish to.

2. **Settings → Environments → `github-pages` → add `develop` to the allowed
   deployment branches.** Enabling Pages creates this environment restricted to
   the default branch (`main`). Until `develop` is added, deploys fail with
   `Branch "develop" is not allowed to deploy to github-pages due to
   environment protection rules`.

Step 2 is only needed because the deploying branch differs from the default
branch. Making `develop` the default branch instead would also resolve it.

## How deployment works

A push to `develop` runs the workflow, which uploads `site/` as a Pages artifact
and publishes it. There is no build step — the files are served as authored.

Jekyll does not run. The Actions deployment path serves the uploaded artifact
verbatim, so a `.nojekyll` file is unnecessary and underscore-prefixed paths are
safe.

To deploy the current tip of `develop` without pushing, run the workflow
manually from the Actions tab (`workflow_dispatch` is enabled).

## Local preview

Open `site/index.html` directly, or serve it so paths behave like production:

```sh
python3 -m http.server -d site 8000   # http://localhost:8000
```

## Adding a build step later

Insert the build in the `build` job before the upload, and point the upload at
the generated directory:

```yaml
- run: npm ci && npm run build
- uses: actions/upload-pages-artifact@v5
  with:
    path: dist # was: site
```

Configure the generator's base path to `/parts-master.io/` unless a custom
domain is serving the site from the root.

## Custom domain

The site is currently served from the default Pages URL. To move it to
`parts-master.io`:

1. Add the DNS records at your registrar — four `A` records for the apex
   pointing at `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, and
   `185.199.111.153`, or a `CNAME` to `theonej.github.io` for a `www` subdomain.
2. Enter the domain under **Settings → Pages → Custom domain**. GitHub commits a
   `CNAME` file for you; keep it inside `site/` so the deploy preserves it.
3. Wait for the certificate, then enable **Enforce HTTPS**.

Set the DNS records before entering the domain in settings — doing it in the
other order leaves the site unreachable while DNS propagates.
