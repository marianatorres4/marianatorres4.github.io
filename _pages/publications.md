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
  - /publications/preprints/
  - /publications/theses/
  - /publications/data/
---

{% include base_path %}

{% include toc title="Jump to" icon="fas fa-file-alt" %}

<div class="notice--info social-icons">
  <h4 class="no_toc" style="padding-bottom: 6px;">You can also find my articles on:</h4>
  {% if site.author.googlescholar %}<a href="https://scholar.google.com/citations?user={{ site.author.googlescholar }}" class="btn btn--inverse"><i class="fas fa-graduation-cap"></i> Google Scholar</a>{% endif %}
  {% if site.author.researchgate %}<a href="https://www.researchgate.net/profile/{{ site.author.researchgate }}" class="btn btn--inverse"><i class="ai ai-researchgate-square" aria-hidden="true"></i> ResearchGate</a> {% endif %}
  {% if site.author.orcid %}<a href="https://orcid.org/{{ site.author.orcid }}" class="btn btn--inverse"><i class="ai ai-orcid"></i> ORCID</a> {% endif %}
  {% if site.author.scopus %}<a href="https://www.scopus.com/authid/detail.uri?authorId={{ site.author.scopus }}" class="btn btn--inverse"><i class="ai ai-scopus"></i> Scopus</a> {% endif %}
  {% if site.author.researcherid %}<a href="{{ site.author.researcherid.url }}" class="btn btn--inverse"><i class="ai ai-researcherid-square"></i> ResearcherID</a> {% endif %}
</div>

## Submitted Articles & Preprints
{% for post in site.publications_preprints reversed %}
  {% include archive-single.html %}
{% endfor %}

## Peer-Reviewed Publications
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

## Policy Reports
<div class="list__item">
<h2 class="archive__item-title" itemprop="headline"><a href="https://global-tipping-points.org" title="https://global-tipping-points.org" target="_blank">The Global Tipping Points Report 2023</a></h2>
<p class="page__meta"><i class="fa fa-book-open" aria-hidden="true"></i> University of Exeter | 2023</p>
Lenton, T.M., Armstrong McKay, D.I., Loriani, S., Abrams, J.F., Lade, S.J., Donges, J.F., Milkoreit, M., Powell, T., Smith, S.R., Zimm, C., Buxton, J.E., Laybourn, L., Ghadiali, A., Dyke, J.G. (eds): <i>The Global Tipping Points Report 2023</i>, University of Exeter, Exeter, UK, <a href="https://global-tipping-points.org" title="https://global-tipping-points.org" target="_blank">https://global-tipping-points.org</a>, in press, 2023.
</div>

## Non-Peer-Reviewed Publications
<div class="list__item">
<h2 class="archive__item-title" itemprop="headline"><a href="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/" title="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/" target="_blank">Hysteresis For Dummies – Why history matters</a></h2>
<p class="page__meta"><i class="fa fa-book-open" aria-hidden="true"></i> EGU Blogs | 2020</p>
<b>Garbe, J.</b>: <i>Hysteresis For Dummies – Why history matters</i>, EGU Blogs, <a href="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/" title="https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/" target="_blank">https://blogs.egu.eu/divisions/cr/2020/12/04/hysteresis-for-dummies-why-history-matters/</a>, 2020.
</div>

## Academic Theses
{% for post in site.publications_theses reversed %}
  {% include archive-single.html %}
{% endfor %}

## Data & Code
{% for post in site.publications_data reversed %}
  {% include archive-single.html %}
{% endfor %}