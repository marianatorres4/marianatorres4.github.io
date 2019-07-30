---
permalink: /cv-print/
title: "Curriculum Vitae"
layout: splash
author_profile: false

---

<script type="text/javascript">
      window.onload = function() { window.print(); }
</script>


{% include base_path %}

<h1 align="center">{{ site.author.name }}</h1>

<p align="center">{{ site.author.bio }}</p>

<p align="center"><i class="fas fa-envelope" aria-hidden="true"></i>&nbsp;<a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a> &#124; <i class="fas fa-desktop" aria-hidden="true"></i>&nbsp;<a href="{{ site.url }}">{{ site.url }}</a> &#124; <i class="fab fa-twitter" aria-hidden="true"></i>&nbsp;<a href="https://twitter.com/{{ site.author.twitter }}">@{{ site.author.twitter }}</a></p>

## Education
- **Ph.D. in Climate Physics**, University of Potsdam
  - **Date:** expected
  - **Dissertation:** "Interactions of the Greenland and Antarctic ice sheets"
  - **Advisors:** Prof. Ricarda Winkelmann and Dr. Jonathan F. Donges

- **M.Sc. in Integrated Climate System Sciences**, School of Integrated Climate System Sciences at the University of Hamburg
  - **Date:** March 2017
  - **Thesis:** "Long-term evolution and critical thresholds of the Antarctic Ice Sheet"
  - **Advisors:** Dr. Georg Feulner, Prof. Ricarda Winkelmann, and Prof. Lars Kaleschke

- **B.Sc. in Physics (major) and Mathematics (minor)**, Humboldt University of Berlin
  - **Date:** December 2013
  - **Thesis:** "An overview of explanations for the problem of weak temperature gradients in warm climates in Earth history"
  - **Advisors:** Prof. Jürgen Kurths and Dr. Georg Feulner

## Relevant Academic Positions
- **PhD candidate and researcher**, Potsdam Institute for Climate Impact Research, Potsdam, Germany (since 2017)
  - Embedded within the Leibniz project [DominoES](https://www.pik-potsdam.de/dominoes "https://www.pik-potsdam.de/dominoes") and the FutureLab on [Earth Resilience in the Anthropocene](https://www.pik-potsdam.de/earthresilience "https://www.pik-potsdam.de/earthresilience")
  - *Methods:* numerical simulations with the Parallel Ice Sheet Model ([PISM](http://pism-docs.org/ "http://pism-docs.org/")), model development and implementation with focus on ice-ocean interaction
  
## Scientific Background
- **Physics courses:** classical/analytical/fluid mechanics, thermodynamics, electrodynamics, optics, special relativity, quantum mechanics, particle physics, solid-state physics
- **Mathematics courses:** analysis, complex analysis, linear algebra
- **Climate physics courses:** ocean physics and modeling, atmospheric physics, ice dynamics, sea-ice physics and modeling
- **Programming languages:** Python, R, Matlab, C++, Fortran, Bash/Unix, LaTeX, HTML, CSS, Markdown

## Research Interests
- Climate and social tipping interactions
- Antarctic ice-sheet / ice-shelf stability and future sea-level change
- Hysteresis behavior of the Antarctic Ice Sheet and Antarctic tipping points
- Response of the Antarctic Ice Sheet to Greenland ice loss via ocean dynamics

## Publications
<ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
{% endfor %}</ul>

## Talks and Conference Presentations
<ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
{% endfor %}</ul>
  
## Teaching
<ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
{% endfor %}</ul>
