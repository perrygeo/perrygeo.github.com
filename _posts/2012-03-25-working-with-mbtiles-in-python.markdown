---
date: '2012-03-25 11:42:48'
layout: post
slug: working-with-mbtiles-in-python
status: publish
title: Working with mbtiles in python
tldr: Python code for working with mbtiles databases
wpid: '163'
tags:
- mbtiles
- utfgrid
- tilestream
- python
- tornado
---

[python-mbtiles](https://github.com/perrygeo/python-mbtiles). Check it out.

I've been working a bit with Tilemill lately and love the Carto css styling, iteractivity through UTFGrids and being able to export the whole deal as a single [mbtiles](http://mapbox.com/mbtiles-spec/) sqlite database. But when it comes to working with the mbtiles databases, I've found both Tilestache and Tilestream to be fairly limiting:

Tilestache serves images but does not (yet) serve up UTFGrids _directly from mbtiles _ while Tilestream hardcodes a "grid()" JSONP callback around the returned json data making it fairly specific to Wax client libraries.

So I went down two paths, first trying to export all the tiles out of mbtiles to json and png files (for those times when you just want to serve static files), then trying to write a simple server that would do dynamic jsonp callbacks. Turns out that in the process, I was able to abstract a lot of the python< ->sqlite interaction into some generic python classes.

Thus [python-mbtiles](https://github.com/perrygeo/python-mbtiles) was born. It provides a simple mbtiles web server, a conversion script, and some python classes to work with. No frills, no anything really at this point. More an experiment gone right that might be useful to someone out there in GeoPython land.  Enjoy and let me know if you have any ideas!
