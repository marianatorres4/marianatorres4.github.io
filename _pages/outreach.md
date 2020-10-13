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
  You can also see a [map of all the places I've given a talk](talkmap).
{% endif %}

{% for post in site.talks reversed %}
  {% include archive-single-talk.html %}
{% endfor %}

## Workshops & Schools
<h2 class="archive__item-title" itemprop="headline">Forum for Research into Ice Shelf Processes (FRISP)</h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> June 16-25, 2020 | online</p>

<h2 class="archive__item-title" itemprop="headline">Social Tipping Elements relevant to stay within planetary boundaries (DominoES Workshop II)</h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> June 17-19, 2019 | GESIS Cologne, Germany</p>

<h2 class="archive__item-title" itemprop="headline">Ice Sheets and Glaciers in the Climate System (Karthaus School)</h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> September 11-22, 2018 | Karthaus, Italy</p>

<h2 class="archive__item-title" itemprop="headline">Social Tipping Elements Decisive for the Future of the Anthropocene (DominoES Workshop I)</h2>
<p class="page__meta"><i class="fa fa-calendar" aria-hidden="true"></i> June 4-6, 2018 | GESIS Cologne, Germany</p><br /><br />

## Teaching
{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}
