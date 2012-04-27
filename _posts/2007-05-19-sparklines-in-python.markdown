---
date: '2007-05-19 15:56:07'
layout: post
slug: sparklines-in-python
status: publish
title: Sparklines in python
wpid: '64'
---

Edward Tufte, the outspoken guru of data visualization, has long been an advocate of clear and concise (almost minimalist) graphical representations of data. He's got a lot of great ideas relevant to cartography (my cartography course at Humboldt State used his book "The Visual Display of Quantitative Information" as our text). 

One of the coolest ideas are "sparklines" which he describes as "data-intense, design-simple, word-sized graphics". Instead of standalone charts that are often placed on their own and separate from the text that discusses them, sparklines are meant to be placed in-line with the text and provide memorable, simple and contextually-relevant data to support the surrounding text. For example:




 _The US National Debt as a percentage of GDP increased during the Reagan and Bush presidencies ![](/assets/img/reaganbush.GIF) but dropped off slightly during the Clinton administration  ![](/assets/img/clinton.GIF) . _




Now of course I had to figure out how to produce these in python.  Theres a great [cgi application](http://bitworking.org/projects/sparklines/#source), written in python by Joe Gregorio, that does sparklines. I needed something that was abstracted away from the CGI framework, more of a proper python module. Replacing all the CGI-specific code was straightforward and I came up with a standalone sparkline python module ([ View / Download the Source Code. ](http://perrygeo.googlecode.com/svn/trunk/gis-bin/spark.py) ) The only dependencies are python and the python imaging library.

In the minimalist spirt of sparklines, the interface was kept simple. First you create a list of data values then simply pass the list to one of the sparkline generators:



> import spark
a = [32.5,35.2,39.9,40.8,43.9,48.2,50.5,51.9,53.1,55.9,60.7,64.4]
spark.sparkline_smooth(a).show()



Or if you prefer a more discrete, bar-graph-style ![](/assets/img/discrete.GIF) instead of a smooth line:



> spark.sparkline_discrete(a).show()



There's plenty of room for configuration. For example, in the national debt example above I wanted to keep the y axis at the same scale (instead of the default min-max scaling) and make each step 6 pixels wide:



> spark.sparkline_smooth(a, dmin=30,dmax=70, step=6).show()



How does this relate to cartography? GIS typically takes a snapshot representation of earth, frozen in time. Since sparklines seem particularly good at representing change-over-time, it could be an interesting way to add a time dimension to a 2-D map. For example, instead of just displaying country polygons with labels, you could place a sparkline right under the label showing the population changes over the last century. It seems like it would be an ideal way to embed alot of useful information into a small map. 

Anyone know of any good examples?


