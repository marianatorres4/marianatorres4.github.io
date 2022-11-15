---
permalink: /contact/
title: "Contact"
excerpt: "Contact details and some links."
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

### Mailing address
<address>
Potsdam Institute for Climate Impact Research<br />
P.O. Box 60 12 03<br />
14412 Potsdam<br />
Germany
</address><br />

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2435.4380679053866!2d13.062056015952251!3d52.38060855430227!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47a8f5966fb9462f%3A0xb7e9d470cb3893f8!2sPotsdam+Institute+for+Climate+Impact+Research!5e0!3m2!1sen!2sde!4v1549109494023" width="80%" height="360" frameborder="0" style="border:0" allowfullscreen></iframe>

### Online
<i class="fab fa-twitter" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://twitter.com/{{ site.author.twitter }}">Twitter</a><br />
<i class="fab fa-mastodon" aria-hidden="true"></i>&nbsp;&nbsp;<a href="{{ site.author.mastodon.url }}">Mastodon</a><br />
<i class="fab fa-linkedin" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://www.linkedin.com/in/{{ site.author.linkedin }}">LinkedIn</a><br />
<i class="ai ai-researchgate-square" aria-hidden="true"></i>&nbsp;&nbsp;<a href="https://www.researchgate.net/profile/{{ site.author.researchgate }}">ResearchGate</a><br />
<i class="fas fa-graduation-cap"></i>&nbsp;&nbsp;<a href="https://scholar.google.com/citations?user={{ site.author.googlescholar }}">Google Scholar</a><br />
<i class="ai ai-orcid"></i>&nbsp;&nbsp;<a href="https://orcid.org/{{ site.author.orcid }}">ORCID</a><br />
<i class="ai ai-scopus"></i>&nbsp;&nbsp;<a href="https://www.scopus.com/authid/detail.uri?authorId={{ site.author.scopus }}">Scopus</a><br />
<i class="fab fa-github"></i>&nbsp;&nbsp;<a href="https://github.com/{{ site.author.github }}">Github</a><br />