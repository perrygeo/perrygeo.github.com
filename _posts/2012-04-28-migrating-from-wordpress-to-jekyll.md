---
layout: post
title: "Migrating from Wordpress to Jekyll"
description: ""
category: 
tldr: static file blogging 
tags:
- jekyll
- git
---
{% include JB/setup %}

I just switched this blog from an ancient version of wordpress running on a VPS 
to a static-file [jekyll bootstrap](http://jekyllbootstrap.com/) site 
(hosted by [github](http://github.com/perrygeo/perrygeo.github.com)). 
Let me know if you experience any wierdness on the site or feeds. I've taken good measures to make sure links don't break (old URLS should get a 301 permanent redirect to blog.perrygeo.net) but let me know if you get any 404s.

### So why do it? 

1. Having a PHP-MySQL app running on a VPS just to serve up a bunch of blog posts seemed excessive. I don't have the desire to maintain that sort of infrastructure for a simple blog!
2. Wordpress' editing and admin interface suck. I prefer vim and bash.
3. Markdown is a great language for quickly banging out blog posts.
4. Static files just make sense for what is basically static content.
5. Github pages provides the hosting for me and even handles CNAMEs for DNS.
6. Managing revisions with `git`.

### The conversion process

It was not an entirely smooth transition, most of which can be traced directly to dumb decisions on my part. I won't recount the entire process (there are plenty of guides on internets) but I'll outline the major steps here:

1. Export the wordpress blog to an xml file. I has to use `xmllint` to clean it up a bit. 
2. Set up a [disqus](http://disqus.com) account and import my wordpress file. Disqus will handle all the comments which are the only dynamic content on the page. 
3. Use [exitwp.py](https://github.com/thomasf/exitwp) to convert the xml to jekyll markdown files. This worked OK. Not great. Tags and formatting did not come through as expected and I had to wrestle the script a bit. Tables were destroyed and some iframes (youtube links) were lost. 
4. Forked Jekyll Bootstrap and brought in my posts. 
5. Started tweaking of css and markdown to get formatting right. Still have a ways to go on this front - let me know if there is any content you'd like me to restore faster than others.
6. Had to write a little web service to redirect posts; the old blog stupidly used the default wordpress URLS like `/wordpress/?p=4` which needed to go to `/2010/01/01/blah`
7. My images were all over the place; some I had in wordpress uploads, others on various servers, some were absolute links, others relative. Gathering them all in one place and using some sed-fu to get the paths right was essential.
8. Retagged some posts - still working on tags.
9. Set up Google Analytics to track usage. 

I think that's about it. There are still some big formatting problems on older posts (mostly due to the fact that I used blockquotes for code). And tables are still destroyed. I'll be working on cleaning these up as I go along. 

Overall impression of Jekyll-Bootstrap and hosting with Github pages? **Awesome**. I would highly recomend it to anyone starting a new blog or converting a smaller/better-behaved wordpress site. 
It is so much better than having to deal with PHP and MySQL (hopefully the last time I'll ever see them!). But the conversion was a bit tricky and took way more of my Friday and Saturday than I'd like to admit. I would not want to do that again... But I'm glad did. 

What do you think of the new digs?
 
