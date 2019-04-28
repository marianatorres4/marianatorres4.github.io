---
permalink: /sitemap/
title: "Sitemap"
excerpt: "List of all the posts and pages found on the site."
author_profile: true
redirect_from:
  - 
---

{% include base_path %}

A list of all the posts and pages found on the site. For you robots out there is an [XML version]({{ base_path }}/sitemap.xml) available for digesting as well.

## Pages (in alphabetical order)
{% for post in site.pages %}
{% unless post.sitemap == false %}
  {% include archive-single.html %}
{% endunless %}
{% endfor %}

## Posts (in chronological order by collection)
{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}

{% capture written_label %}'None'{% endcapture %}

{% for collection in site.collections %}
{% unless collection.output == false or collection.label == "posts" %}
  {% capture label %}{{ collection.label }}{% endcapture %}
  {% if label != written_label %}
  <h2>{{ label }}</h2>
  {% capture written_label %}{{ label }}{% endcapture %}
  {% endif %}
{% endunless %}
{% for post in collection.docs %}
  {% unless collection.output == false or collection.label == "posts" %}
  {% include archive-single.html %}
  {% endunless %}
{% endfor %}
{% endfor %}