---
layout: single
title: Categories
permalink: /categories/
---

<section class="container-wide content-section page-header">
  <p class="page-subtitle">Choose a category to view all working papers tagged for that topic.</p>
</section>

<section class="container-wide content-section">
  <div class="cat-grid">
    {% for category in site.data.categories %}
      <a class="cat-box" href="{{ '/categories/' | append: category.slug | append: '/' | relative_url }}">
        <span class="cat-name">{{ category.name }}</span>
        <span class="hint">View papers</span>
      </a>
    {% endfor %}
  </div>
</section>
