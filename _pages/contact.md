---
permalink: /contact/
title: "Contact"
excerpt: "Contact details and online profiles."
header:
  overlay_image: header/header5.jpg
  overlay_filter: 0.2 # same as adding an opacity of 0.2 to a black background
  caption: "Photo: A. Künstle"
author_profile: true
redirect_from: 
  - 
---

{% include base_path %}

### Office
<i class="fas fa-building" aria-hidden="true"></i>&nbsp;&nbsp;Telegrafenberg A62, Room S10, 14473 Potsdam<br />

<i class="fas fa-envelope" aria-hidden="true"></i>&nbsp;&nbsp;<a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a><br />
<i class="fas fa-desktop" aria-hidden="true"></i>&nbsp;&nbsp;<a href="{{ site.author.uri }}">{{ site.author.uri | remove: "https://" }}</a><br />
<i class="fas fa-phone" aria-hidden="true"></i>&nbsp;&nbsp;<a href="tel:{{ site.author.phone }}">{{ site.author.phone }}</a><br />

### Mailing Address
<address>
Potsdam Institute for Climate Impact Research<br />
P.O. Box 60 12 03<br />
14412 Potsdam<br />
Germany
</address><br />

<iframe src="/contact/contact-map.html" width="80%" height="400px" style="border: none;"></iframe> <!-- width="100%" height="520px" -->

### Scientific Profiles
<i class="ai ai-orcid" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://orcid.org/{{ site.author.orcid }}">ORCID</a><br />
<i class="ai ai-researcherid-square" aria-hidden="true"></i>&nbsp;&nbsp;<a href="{{ site.author.researcherid.url }}">WoS ResearcherID</a><br />
<i class="ai ai-scopus" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://www.scopus.com/authid/detail.uri?authorId={{ site.author.scopus }}">Scopus Author ID</a><br />
<i class="ai ai-researchgate-square" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://www.researchgate.net/profile/{{ site.author.researchgate }}">ResearchGate</a><br />
<i class="fas fa-graduation-cap" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://scholar.google.com/citations?user={{ site.author.googlescholar }}">Google Scholar</a><br />
<i class="fab fa-github" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://github.com/{{ site.author.github }}">Github</a><br />


### Social Media Profiles
<i class="fab fa-mastodon" aria-hidden="true"></i>&nbsp;&nbsp;<a href="{{ site.author.mastodon.url }}">Mastodon</a><br />
<i class="fab fa-twitter" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://twitter.com/{{ site.author.twitter }}">Twitter</a><br />
<i class="fab fa-linkedin" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://www.linkedin.com/in/{{ site.author.linkedin }}">LinkedIn</a><br />