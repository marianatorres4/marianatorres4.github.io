---
permalink: /cv/
title: "CV"
excerpt: "Education, scientific background, research interests & skills, and more."
author_profile: true
redirect_from:
  - 
---

{% include base_path %}

<!-- Click [here](/cv-print/) for a printable version or [download a PDF](/files/cv-print.pdf).<br /><br /><br /> -->

<h1 align="center">{{ site.author.name }}</h1>
<p><h3 align="center">Curriculum Vitae</h3></p>

<p align="center">{{ site.author.bio }}</p>

<p align="center"><i class="fas fa-envelope" aria-hidden="true"></i>&nbsp;<a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a> &#124; <i class="fas fa-desktop" aria-hidden="true"></i>&nbsp;<a href="{{ site.author.uri }}">www.pik-potsdam.de/members/garbe/</a> &#124; <i class="fab fa-twitter" aria-hidden="true"></i>&nbsp;<a href="https://twitter.com/{{ site.author.twitter }}">@{{ site.author.twitter }}</a></p>

## Education
- **Ph.D. in Climate Physics**, University of Potsdam
  - *Date:* expected
  - *Doctoral Thesis:* "Interactions of the Greenland and Antarctic ice sheets"
  - *Advisors:* Prof. Ricarda Winkelmann & Dr. Jonathan F. Donges

- **M.Sc. in Integrated Climate System Sciences**, School of Integrated Climate System Sciences at the University of Hamburg
  - *Date:* March 2017
  - *Master's Thesis:* "Long-term evolution and critical thresholds of the Antarctic Ice Sheet"
  - *Advisors:* Dr. habil. Georg Feulner, Prof. Ricarda Winkelmann, & Prof. Lars Kaleschke

- **B.Sc. in Physics (major) and Mathematics (minor)**, Humboldt University of Berlin
  - *Date:* December 2013
  - *Bachelor's Thesis:* "An overview of explanations for the problem of weak temperature gradients in warm climates in Earth history"
  - *Advisors:* Prof. Jürgen Kurths & Dr. habil. Georg Feulner

## Relevant Academic Positions
- **PhD candidate and researcher**, Potsdam Institute for Climate Impact Research, Potsdam, Germany (since 2017)
  - Embedded within the working group on [Ice Dynamics](https://ricarda.science/group "https://ricarda.science/group") led by Prof. Ricarda Winkelmann and PIK's FutureLab on [Earth Resilience in the Anthropocene](https://www.pik-potsdam.de/earthresilience "https://www.pik-potsdam.de/earthresilience")
  - *Funding:*
    - Since 2020: [TiPACCs](https://www.tipaccs.eu "https://www.tipaccs.eu") (Horizon 2020 / European Union)
    - 2017--2020: [DominoES](https://www.pik-potsdam.de/dominoes "https://www.pik-potsdam.de/dominoes") (Leibniz Association)
  - *Methods:* numerical simulations with the Parallel Ice Sheet Model ([PISM](http://pism-docs.org/ "http://pism-docs.org/")), model development and implementation with focus on ice-ocean interactions
  
## Scientific Background
- **Physics courses:** classical/analytical/fluid mechanics, thermodynamics, electrodynamics, optics, special relativity, quantum mechanics, particle physics, solid-state physics
- **Mathematics courses:** analysis, complex analysis, linear algebra
- **Climate physics courses:** ocean physics and modeling, atmospheric physics, ice dynamics, sea-ice physics and modeling
- **Programming languages:** Python, R, Matlab, C++, Fortran, Bash/Unix, LaTeX, HTML, CSS, Markdown

## Research Interests
- Ice sheet / ice shelf modelling (co-development of [PISM](http://pism-docs.org/ "http://pism-docs.org/"))
- Antarctic ice sheet stability and future sea-level change
- Hysteresis behavior of the Antarctic ice sheet and Antarctic tipping points
- Climate and socio-economic tipping interactions ([DominoES](https://www.pik-potsdam.de/dominoes "https://www.pik-potsdam.de/dominoes"))
- Earth system resilience ([ERAlab](https://www.pik-potsdam.de/earthresilience "https://www.pik-potsdam.de/earthresilience"))

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
