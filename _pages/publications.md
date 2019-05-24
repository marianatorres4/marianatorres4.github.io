---
permalink: /publications/
title: "Publications"
excerpt: "List of academic publications."
author_profile: true
redirect_from: 
  - 
---


{% include base_path %}

You can also find my articles on [my Google Scholar profile](https://scholar.google.com/citations?user=PHdduOoAAAAJ "https://scholar.google.com/citations?user=PHdduOoAAAAJ").
<!-- {% if author.googlescholar %}
  <p>You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.</p>
{% endif %} -->

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}