---
layout: default
title: Issues
nav_order: 2
has_children: true
permalink: /issues/
---

# Issues

Browse our collection of academic papers organized by semester and year. New issues appear automatically when you add a folder under `issues/` with an `index.md` file.

{% assign sorted_pages = site.pages | sort: 'issue_id' | reverse %}
{% assign issue_pages = "" | split: "" %}
{% for p in sorted_pages %}
  {% if p.name == "index.md" and p.issue_id and p.path contains "issues/" %}
    {% assign issue_pages = issue_pages | push: p %}
  {% endif %}
{% endfor %}

{% if issue_pages and issue_pages.size > 0 %}
<ul>
  {% for issue in issue_pages %}
    <li>
      <a href="{{ issue.url | relative_url }}">{{ issue.title }}</a>
      {% if issue.description %}
        — {{ issue.description }}
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% else %}
No issues published yet. Add a new issue directory under `issues/` to get started.
{% endif %}
