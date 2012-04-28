---
date: '2008-04-02 22:26:05'
layout: post
slug: working-hard-for-some-rest
status: publish
title: Working hard for some REST
wpid: '111'
tags:
- ajax
- django
- rest
- web.py
- python
---

I don't spend much time with web programming these days but I decided to give [web.py](http://webpy.org/) (the minimalist python web framework) a shot and, while I was at it, try implementing a simple REST api.

First of all, web.py is truly everything it claims to be - small, light and easy to deploy behind [lighttpd](http://www.lighttpd.net/). It gives you a ton of flexibility to implement anything however you want - which is a plus or minus depending on how you look at it. I liked the inifinte flexibility but I can see alot of refactoring taking place and features needing to be implemented just to match the functionality built into a more structured framework like Django.

Back to the REST side of things. So I created a url-mapping to my "resources" or "nouns" and used the HTTP verbs (POST,GET,PUT,DELETE) to supply the interface. This was a joy to do in web.py which made it easy.

    urls = ("/thing/(\d+)", "thing")
    ...
    class thing:
        def GET(self, thingid):
            # select query and render to template
            ....
        def POST(self, thingid):
            # insert query and redirect to /thing/thingid
            ....
        def DELETE(self, thingid):
            # delete query
            ....
        def PUT(self, thingid):
            # use cgi args to run update query on specified thing
            ....

The hard part came when I realized that HTML forms do not implement DELETE or PUT methods! 2 of the 4 cornerstone HTTP verbs are not implemented in HTML forms? 

Surely this can be accomplished with a top-notch AJAX library. I tried Prototype.js and it appears that the PUT and DELETE methods are simply tunneled over POST with an extra arg attached and the server side has to handle it accordingly. So I ended up just using a straight XMLHttpRequest which works but has it's own problems.

How are you supposed to call PUT or DELETE through a web page? Is XMLHttpRequest the only way? What about browsers without javascript?


