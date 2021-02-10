---
permalink: /publications/
title: "Publications"
excerpt: "List of academic publications."
author_profile: true
redirect_from: 
  - 
---

{% include base_path %}

## Peer-Reviewed Publications
{% if site.author.researchgate and site.author.googlescholar and site.author.orcid %}
  You can also find my articles on: <a href="{{ site.author.researchgate }}">ResearchGate</a> &#124; <a href="{{ site.author.googlescholar }}">Google Scholar</a> &#124; <a href="{{ site.author.orcid }}">ORCID</a>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

## Academic Theses
{% for post in site.publications_theses reversed %}
  {% include archive-single.html %}
{% endfor %}

## Data
{% for post in site.publications_data reversed %}
  {% include archive-single.html %}
{% endfor %}

## Popular Science
<h2 class="archive__item-title" itemprop="headline"><a href="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/" title="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/">Hysteresis For Dummies – Why history matters</a></h2>
<p class="page__meta"><i class="fa fa-book-open" aria-hidden="true"></i> EGU Blogs | 2020</p>