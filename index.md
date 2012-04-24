---
layout: page
title: Welcome to the Perrygeo blog!
tagline: Adventures in geospatial tech
---
{% include JB/setup %}

<div class="posts">
  {% for post in site.posts limit:5 %}
  <h2><a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></h2>
    <span>posted by {{post.author}} on {{ post.date | date_to_string }}</span>
    <p>{{ post.content }}</p> 
  {% endfor %}
</div>
<a href="/archive.html">Older Posts</a>
