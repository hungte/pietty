# PieTTY project website

Static site for PieTTY, migrated from Google Sites
(`https://sites.google.com/view/pietty-project/`) to GitHub Pages (Jekyll).

## Layout

- `index.md`, `download.md`, `faq.md`: page content (Markdown, kramdown/GFM).
  Side-by-side English / 中文 sections use
  `<div class="row" markdown="1">` + `<div class="col" markdown="1">`.
- `_layouts/default.html`: header, navigation and footer.
- `assets/css/style.css`: styles.
- `assets/images/`: images downloaded from the original site.
- `_config.yml`: site title, navigation and `baseurl`.
- `_tools/convert.py`: one-off converter used for the migration (re-fetches
  the Google Sites pages and regenerates the Markdown). Not part of the site.
- `_tools/preview.rb`: rough local preview without Jekyll
  (`ruby _tools/preview.rb`, then open `_preview/index.html`).

## Deploy

The default `baseurl` is `/pietty`, i.e. the site is served at
`https://hungte.github.io/pietty/` as the project page of `hungte/pietty`.

1. Put these files in a `gh-pages` branch (or a `docs/` folder on the default
   branch) of the `hungte/pietty` repository.
2. In GitHub: Settings → Pages → Source: "Deploy from a branch", pick the
   branch and folder.
3. For a custom domain, add a `CNAME` file with the domain name, set
   `baseurl: ""` in `_config.yml`, and update DNS.

## Local preview with Jekyll

```sh
gem install bundler jekyll
jekyll serve
```
