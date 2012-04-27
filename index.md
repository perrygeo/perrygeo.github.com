---
layout: page
tagline: Selected ramblings of a geospatial tech nerd
---
{% include JB/setup %}

<div class="posts">
  {% for post in site.posts limit:5 %}
  <div class="box">
    <h2><a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></h2>
    <span>posted by {{post.author}} on {{ post.date | date_to_string }}</span>
    <p>{{ post.content }}</p> 
  </div>
  {% endfor %}
</div>
<a href="/archive.html">Older Posts</a>
