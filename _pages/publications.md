---
permalink: /publications/
title: "Publications"
excerpt: "List of academic publications"
layout: archive
author_profile: true
redirect_from: 
  - /publications.html
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
