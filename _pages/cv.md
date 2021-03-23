---
permalink: /cv/
title: "Curriculum Vitae"
excerpt: "Education, scientific background, research interests & skills, and more."
author_profile: true
redirect_from:
  - 
---

{% include base_path %}

<!-- Click [here](/cv-print/) for a printable version or [download a PDF](/files/cv-print.pdf).<br /><br /><br /> -->

<h2 align="center">{{ site.author.name }}</h2>
<h3 align="center" style="margin: 0px auto 20px;">M.Sc.</h3>
<p align="center" style="margin: auto; width: 80%">{{ site.author.bio }}</p>

<p align="center"><i class="fas fa-envelope" aria-hidden="true"></i>&nbsp;<a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a> &#124; <i class="fas fa-desktop" aria-hidden="true"></i>&nbsp;<a href="{{ site.author.uri }}">{{ site.author.uri | remove: "https://" }}</a> &#124; <i class="fab fa-twitter" aria-hidden="true"></i>&nbsp;<a href="https://twitter.com/{{ site.author.twitter }}">@{{ site.author.twitter }}</a></p>

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
  - Embedded within the working group on [Ice Dynamics](https://www.pik-potsdam.de/en/institute/departments/earth-system-analysis/research/ice-dynamics/ "https://www.pik-potsdam.de/en/institute/departments/earth-system-analysis/research/ice-dynamics/") led by Prof. Ricarda Winkelmann and PIK's FutureLab on [Earth Resilience in the Anthropocene](https://www.pik-potsdam.de/earthresilience "https://www.pik-potsdam.de/earthresilience")
  - *Funding:*
    - Since 2020: [TiPACCs](https://www.tipaccs.eu "https://www.tipaccs.eu") (Horizon 2020 / European Union)
    - 2017--2020: [DominoES](https://www.pik-potsdam.de/dominoes "https://www.pik-potsdam.de/dominoes") (Leibniz Association)
  - *Methods:* numerical simulations with the Parallel Ice Sheet Model ([PISM](http://pism-docs.org/ "http://pism-docs.org/")), model development and implementation with focus on ice-ocean / ice-atmosphere interactions
- **M.Sc. student**, Potsdam Institute for Climate Impact Research, Potsdam, Germany (2016-2017)
  - Embedded within the working group on [Earth System Modes of Operation](https://www.pik-potsdam.de/en/institute/departments/earth-system-analysis/research/earth-system-modes-of-operation "https://www.pik-potsdam.de/en/institute/departments/earth-system-analysis/research/earth-system-modes-of-operation") led by Dr. habil. Georg Feulner
  
## Scientific Background
- **Physics courses:** classical/analytical/fluid mechanics, thermodynamics, electrodynamics, optics, special relativity, quantum mechanics, particle physics, solid-state physics
- **Mathematics courses:** analysis, complex analysis, linear algebra
- **Climate physics courses:** ocean physics and modeling, atmospheric physics, ice dynamics, sea-ice physics and modeling
- **Programming languages:** Python, R, Matlab, C++, Fortran, Bash/Unix, LaTeX, HTML, CSS, Markdown
- **Tools:** CDO, NCO, Conda, Git

## Peer-Reviewed Publications
<ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
{% endfor %}</ul>

## Academic Theses
<ul>{% for post in site.publications_theses reversed %}
    {% include archive-single-cv.html %}
{% endfor %}</ul>

## Data & Code
<ul>{% for post in site.publications_data reversed %}
    {% include archive-single-cv.html %}
{% endfor %}</ul>

## Conference Contributions & Talks
<ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
{% endfor %}</ul>
  
## Teaching
<ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
{% endfor %}</ul>
