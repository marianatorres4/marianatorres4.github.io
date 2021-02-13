---
permalink: /outreach/
title: "Science Outreach"
excerpt: "List of past and upcoming scientific talks, conference presentations, workshops, and taught courses."
author_profile: true
redirect_from: 
  - 
---

{% include base_path %}

## Conference Contributions & Talks
{% if site.talkmap_link == true %}
  You can also see a [map of all the places I've given a talk](/outreach/talkmap/).
{% endif %}

{% for post in site.talks reversed %}
  {% include archive-single-talk.html %}
{% endfor %}

## Workshops & Schools
<h2 class="archive__item-title" itemprop="headline">Criticality in Social Tipping Processes (DominoES Workshop III)</h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> December 4, 2020 | online</p>

<h2 class="archive__item-title" itemprop="headline"><a href="https://emps.exeter.ac.uk/mathematics/staff/pdlr201/ec_tp_workshop" title="https://emps.exeter.ac.uk/mathematics/staff/pdlr201/ec_tp_workshop" target="_blank">Emergent Constraints & Tipping Points Workshop (University of Exeter)</a></h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> November 23-26, 2020 | online</p>

<h2 class="archive__item-title" itemprop="headline"><a href="https://eveeno.com/frisp2020" title="https://eveeno.com/frisp2020" target="_blank">Forum for Research into Ice Shelf Processes (FRISP)</a></h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> June 16-25, 2020 | online</p>

<h2 class="archive__item-title" itemprop="headline">Social Tipping Elements relevant to stay within planetary boundaries (DominoES Workshop II)</h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> June 17-19, 2019 | GESIS Cologne, Germany</p>

<h2 class="archive__item-title" itemprop="headline"><a href="https://www.projects.science.uu.nl/iceclimate/karthaus/index.php" title="https://www.projects.science.uu.nl/iceclimate/karthaus/index.php" target="_blank">Ice Sheets and Glaciers in the Climate System (Karthaus School)</a></h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> September 11-22, 2018 | Karthaus, Italy</p>

<h2 class="archive__item-title" itemprop="headline">Social Tipping Elements Decisive for the Future of the Anthropocene (DominoES Workshop I)</h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> June 4-6, 2018 | GESIS Cologne, Germany</p><br /><br />

## Teaching
{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}
