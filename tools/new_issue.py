#!/usr/bin/env python3
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Created {path.relative_to(ROOT)}")


def issue_front_matter(issue_id: str, title: str) -> str:
    return f"""---
layout: default
title: {title}
parent: Issues
has_children: true
permalink: /issues/{issue_id}/
issue_id: {issue_id}
description: Issue {issue_id} of the UNLV ECON 490 Journal.
---

# {title}

This issue features research papers from {title}.

## Papers in this Issue

{{% assign papers = site.pages | where: "issue_id", page.issue_id | where_exp: "p", "p.paper_id" | sort: "paper_id" %}}
{{% if papers and papers.size > 0 %}}
<ul>
  {{% for paper in papers %}}
    <li>
      <a href="{{{{ paper.url | relative_url }}}}">{{{{ paper.title }}}}</a><br />
      <small>Authors: {{{{ paper.authors | join: \", \" }}}}</small><br />
      {{% if paper.abstract %}}
        <small>{{{{ paper.abstract | strip_html | truncatewords: 30 }}}}</small>
      {{% endif %}}
    </li>
  {{% endfor %}}
</ul>
{{% else %}}
No papers have been added to this issue yet.
{{% endif %}}
"""


def paper_template(issue_id: str, paper_id: str, parent_title: str) -> str:
    return f"""---
layout: default
title: Placeholder Title
issue_id: {issue_id}
paper_id: {paper_id}
authors:
  - Author Name
year: 2025
publication_date: 2025-12-01
keywords:
  - Keyword 1
  - Keyword 2
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
Author Name ({{ '{{' }} page.year {{ '}}' }}). {{ '{{' }} page.title {{ '}}' }}. UNLV ECON 490 Journal, {issue_id.replace('-', ' ').title()}. Retrieved from {{ '{{' }} page.pdf | relative_url {{ '}}' }}
```

## Keywords

{{ '{{' }} page.keywords | join: ", " {{ '}}' }}
"""


def main():
    parser = argparse.ArgumentParser(
        description="Create a new issue directory with an index and starter paper."
    )
    parser.add_argument("issue_id", help="Issue identifier, e.g., 2025-fall")
    parser.add_argument(
        "--title",
        help="Issue title (default derived from issue_id)",
        default=None,
    )
    args = parser.parse_args()

    issue_id = args.issue_id.rstrip("/")
    title = args.title or issue_id.replace("-", " ").title()

    issue_dir = ROOT / "issues" / issue_id
    assets_dir = ROOT / "assets" / "papers" / issue_id

    issue_index = issue_dir / "index.md"
    paper_path = issue_dir / "paper-001.md"

    if issue_index.exists():
        print(f"{issue_index} already exists; no changes made.")
        return

    write_file(issue_index, issue_front_matter(issue_id, title))
    write_file(paper_path, paper_template(issue_id, "001", title))
    assets_dir.mkdir(parents=True, exist_ok=True)
    print(f"Ensured PDF directory: {assets_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
