---
permalink: /publications/
title: "Publications"
excerpt: "List of academic publications."
author_profile: true
redirect_from: 
  - 
---


{% include base_path %}

{% if author.googlescholar %}
  <p>IF: You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.</p>
{% endif %}
<p>You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.</p>


{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}