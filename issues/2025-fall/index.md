---
layout: default
title: Fall 2025
parent: Issues
nav_order: 1
has_children: true
permalink: /issues/2025-fall/
issue_id: 2025-fall
description: Student research from the Fall 2025 ECON 490 cohort.
---

# Fall 2025 Issue

This issue features research papers from the Fall 2025 semester of UNLV ECON 490.

## Papers in this Issue

Browse the papers below or use the navigation menu to explore individual submissions.

{% assign papers = site.pages | where: "issue_id", page.issue_id | where_exp: "p", "p.paper_id" | sort: "paper_id" %}
{% if papers and papers.size > 0 %}
<ul>
  {% for paper in papers %}
    <li>
      <a href="{{ paper.url | relative_url }}">{{ paper.title }}</a><br />
      <small>Authors: {{ paper.authors | join: ", " }}</small><br />
      {% if paper.abstract %}
        <small>{{ paper.abstract | strip_html | truncatewords: 30 }}</small>
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% else %}
No papers have been added to this issue yet. Use the submission instructions to contribute.
{% endif %}
