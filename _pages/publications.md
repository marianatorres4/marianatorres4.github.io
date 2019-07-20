---
permalink: /publications/
title: "Publications"
excerpt: "List of academic publications."
author_profile: true
redirect_from: 
  - 
---


{% include base_path %}

{% if site.author.googlescholar %}
  <p>You can also find my articles on <a href="{{ site.author.googlescholar }}">my Google Scholar profile</a>.</p>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}