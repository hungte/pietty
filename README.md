# PieTTY project website

Static site for PieTTY, migrated from Google Sites
(`https://sites.google.com/view/pietty-project/`) to GitHub Pages (Jekyll).

## Layout

- `index.md`, `faq.md`: page content (Markdown, kramdown/GFM). Each
  `<section class="...">` is a full-width band; the class sets the background
  (`hero`, `title`, `plain`, `emph1` = dark blue, `emph2` = light grey).
  Side-by-side English / 中文 uses `<div class="row">` + `<div class="col">`.
- `download.html`: generated from the
  [GitHub Releases](https://github.com/hungte/pietty/releases) of
  `hungte/pietty` (via `site.github.releases`, which GitHub Pages provides
  through `jekyll-github-metadata`):
  - Each release shows its name, release date (unless the notes already contain
    "Release date"), "Released by" (the release author) and its uploaded
    assets. The automatic "Source code" archives are not listed.
  - Release notes containing `## English` and `## 繁體中文` are shown in two
    columns.
  - The `OldReleases` pre-release is shown as "Legacy Non-PieTTY Builds".
  - 0.3.25 - 0.3.11 have no GitHub Release; they are kept by hand in
    `_includes/legacy-03x.md` and shown before the `0.3` release.
  - Per-release markup: `_includes/release.html`.
- `_layouts/default.html`: header, navigation and footer.
- `assets/css/style.css`: styles. `assets/images/`: images.
- `_tools/convert.py`: one-off converter used for the migration (re-fetches
  the Google Sites pages and regenerates `index.md` and `faq.md`).
- `_tools/preview.rb`: local preview without Jekyll, using Liquid 4.0.4 (same
  version as GitHub Pages) and the live GitHub Releases API:
  `ruby _tools/preview.rb --refresh`, then open `_preview/index.html`.
- `_tools/pages-rebuild.yml`: workflow that rebuilds the site when a release is
  published (see below).

## Deploy

The default `baseurl` is `/pietty`, i.e. the site is served at
`https://hungte.github.io/pietty/` as the project page of `hungte/pietty`.

1. Push these files to the `gh-pages` branch of `hungte/pietty`.
2. In GitHub: Settings → Pages → Source: "Deploy from a branch", pick
   `gh-pages` / `(root)`.
3. For a custom domain, add a `CNAME` file with the domain name, set
   `baseurl: ""` in `_config.yml`, and update DNS.

## Keeping the download page up to date

The release list is fetched when the site is built, not when it is viewed.
The site is rebuilt on every push to `gh-pages`. To also rebuild when a release
is published or edited, copy `_tools/pages-rebuild.yml` to
`.github/workflows/pages-rebuild.yml` on the default branch. It can also be run
by hand from the Actions tab ("Run workflow").
