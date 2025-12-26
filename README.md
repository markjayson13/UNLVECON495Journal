# UNLV ECON 490 Journal / Proceedings

Public GitHub Pages site built with **Jekyll + Just-the-Docs**. Papers are organized by issue (semester + year), surfaced with search, and include citation-friendly metadata.

## Configuration

Key settings in `_config.yml`:

```yaml
url: https://markjayson13.github.io
baseurl: /UNLVECON490Journal
permalink: pretty
remote_theme: just-the-docs/just-the-docs
plugins:
  - jekyll-sitemap
```

Set **Settings → Pages → Source** to **GitHub Actions** to use the included workflow `.github/workflows/pages.yml`.

## Local development (macOS)

```bash
brew install ruby
gem install bundler
bundle install          # uses Gemfile with github-pages for compatibility

# Serve with live reload
make serve              # or: bundle exec jekyll serve --livereload

# Build the site
make build
```

Site output is written to `_site/`.

## Adding an issue and paper

Issues and papers live in parallel markdown files and PDFs:

```
issues/<issue-id>/index.md          # issue landing page
issues/<issue-id>/paper-001.md      # paper page
assets/papers/<issue-id>/paper-001.pdf
```

Front matter expected on paper pages:

```yaml
layout: default
title: Paper Title
issue_id: 2025-fall
paper_id: 001
authors: ["Author One", "Author Two"]
year: 2025
publication_date: 2025-12-01
keywords: ["economics", "policy"]
pdf: /assets/papers/2025-fall/paper-001.pdf
abstract: |
  Concise abstract here.
```

### Automation helpers

Create a new issue (also scaffolds paper-001 and the PDF folder):

```bash
python tools/new_issue.py 2026-spring --title "Spring 2026"
```

Add an additional paper to an existing issue:

```bash
python tools/new_paper.py 2026-spring 002 --title "New Paper" --authors "Author One,Author Two" --keywords "economics,markets"
```

Then place the corresponding PDF at `assets/papers/<issue-id>/paper-<paper_id>.pdf`.

## Deployment

The workflow `.github/workflows/pages.yml` builds with `actions/jekyll-build-pages` and deploys via `actions/deploy-pages`. Once enabled, commits to `main` will publish automatically to:

```
https://markjayson13.github.io/UNLVECON490Journal/
```

## Content and policies

- **Search & navigation:** Just-the-Docs sidebar + search are enabled site-wide.  
- **Metadata:** Paper pages emit Google Scholar–style `citation_*` meta tags via `_includes/head_custom.html`.  
- **Policies:** See `/policies/` for copyright, takedown, privacy, integrity, and AI-use guidance.  
- **Disclaimer:** Undergraduate proceedings; not peer-reviewed unless stated.
