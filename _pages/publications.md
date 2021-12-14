---
permalink: /publications/
title: "Publications"
excerpt: "List of academic publications."
header:
  overlay_image: header/header3.jpg
  overlay_filter: 0.2 # same as adding an opacity of 0.2 to a black background
  caption: "Photo: J. Garbe"
author_profile: true
redirect_from: 
  - /publications/articles/
  - /publications/theses/
  - /publications/data/
---

{% include base_path %}

## Peer-Reviewed Publications
{% if site.author.researchgate and site.author.googlescholar and site.author.orcid %}
  <div class="notice--info social-icons">You can also find my articles on: <a href="https://scholar.google.com/citations?user={{ site.author.googlescholar }}"><i class="fas fa-graduation-cap"></i> Google Scholar</a> &#124; <a href="https://www.researchgate.net/profile/{{ site.author.researchgate }}"><i class="ai ai-researchgate-square" aria-hidden="true"></i> ResearchGate</a> &#124; <a href="https://orcid.org/{{ site.author.orcid }}"><i class="ai ai-orcid"></i> ORCID</a></div>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

## Academic Theses
{% for post in site.publications_theses reversed %}
  {% include archive-single.html %}
{% endfor %}

## Data & Code
{% for post in site.publications_data reversed %}
  {% include archive-single.html %}
{% endfor %}

## Popular Science
<div class="list__item">
<h2 class="archive__item-title" itemprop="headline"><a href="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/" title="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/" target="_blank">Hysteresis For Dummies – Why history matters</a></h2>
<p class="page__meta"><i class="fa fa-book-open" aria-hidden="true"></i> EGU Blogs | 2020</p>
<b>Garbe, J.</b>: <i>"Hysteresis For Dummies – Why history matters"</i>, EGU Blogs, <a href="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/" title="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/" target="_blank">https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/</a>, 2020.
</div>
