#!/usr/bin/env python3
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slugify_title(title: str) -> str:
    return title.strip()


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Created {path.relative_to(ROOT)}")


def load_issue_title(issue_id: str) -> str:
    index_path = ROOT / "issues" / issue_id / "index.md"
    if not index_path.exists():
        return issue_id.replace("-", " ").title()
    inside_front_matter = False
    with index_path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip() == "---":
                inside_front_matter = not inside_front_matter
                continue
            if inside_front_matter and line.lower().startswith("title:"):
                return line.split(":", 1)[1].strip()
    return issue_id.replace("-", " ").title()


def paper_template(issue_id: str, paper_id: str, title: str, authors, keywords, parent_title: str) -> str:
    author_lines = "\n".join([f"  - {a.strip()}" for a in authors])
    keyword_lines = "\n".join([f"  - {k.strip()}" for k in keywords]) if keywords else "  - Keyword 1\n  - Keyword 2"
    return f"""---
layout: default
title: {slugify_title(title)}
issue_id: {issue_id}
paper_id: {paper_id}
authors:
{author_lines or '  - Author Name'}
year: 2025
publication_date: 2025-12-01
keywords:
{keyword_lines}
pdf: /assets/papers/{issue_id}/paper-{paper_id}.pdf
abstract: |
  Add a concise abstract (150–300 words) summarizing the research question, methods, and findings.
parent: {parent_title}
grand_parent: Issues
nav_order: {int(paper_id)}
---

# {{ '{{' }} page.title {{ '}}' }}

**Authors:** {{ '{{' }} page.authors | join: ", " {{ '}}' }}  
**Publication date:** {{ '{{' }} page.publication_date | default: page.year {{ '}}' }}  
**Issue:** {parent_title}

## Abstract

{{ '{{' }} page.abstract {{ '}}' }}

## Download

[Download PDF]({{ '{{' }} page.pdf | relative_url {{ '}}' }}){{ '{{' }}: .btn .btn-primary {{ '}}' }}

## Citation

```
{{ '{{' }} page.authors | join: "; " {{ '}}' }} ({{ '{{' }} page.year {{ '}}' }}). {{ '{{' }} page.title {{ '}}' }}. UNLV ECON 490 Journal, {parent_title}. Retrieved from {{ '{{' }} page.pdf | relative_url {{ '}}' }}
```

## Keywords

{{ '{{' }} page.keywords | join: ", " {{ '}}' }}
"""


def main():
    parser = argparse.ArgumentParser(description="Create a new paper markdown template for an existing issue.")
    parser.add_argument("issue_id", help="Issue identifier, e.g., 2025-fall")
    parser.add_argument("paper_id", help="Paper number, e.g., 003")
    parser.add_argument("--title", default="Placeholder Title", help="Paper title")
    parser.add_argument("--authors", default="Author Name", help="Comma-separated authors")
    parser.add_argument("--keywords", default="", help="Comma-separated keywords")
    args = parser.parse_args()

    issue_id = args.issue_id.rstrip("/")
    paper_id = args.paper_id.zfill(3)
    authors = [a for a in args.authors.split(",") if a.strip()]
    keywords = [k for k in args.keywords.split(",") if k.strip()]
    parent_title = load_issue_title(issue_id)

    paper_path = ROOT / "issues" / issue_id / f"paper-{paper_id}.md"
    if paper_path.exists():
        print(f"{paper_path} already exists; no changes made.")
        return

    write_file(
        paper_path,
        paper_template(issue_id, paper_id, args.title, authors, keywords, parent_title),
    )

    assets_dir = ROOT / "assets" / "papers" / issue_id
    assets_dir.mkdir(parents=True, exist_ok=True)
    print(f"Ensured PDF directory: {assets_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
