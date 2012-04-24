---
date: '2007-12-06 23:57:01'
layout: post
slug: google-charts-their-latest-web-service
status: publish
title: Google Charts - their latest web service
wpid: '96'
---

Google Charts is a [web based API](http://code.google.com/apis/chart/) for generating charts/graphs. It supports alot of the common types of graphics including line, pie, bar, scatter plots and Venn diagrams. I've relied on a bunch of other server-side graph generators ([owtchart](http://www.maptools.org/owtchart/index.phtml), [jpgraph](http://www.aditus.nu/jpgraph/), [sparklines](http://www.perrygeo.net/wordpress/?p=64), [matplotlib](http://matplotlib.sourceforge.net/), etc) but this looks like it might be a contender.

Still there is no higher-level programming API yet ... but give it a few days (interface with numpy anyone?). [ExileJedi blog lists ](http://exilejedi.livejournal.com/189606.html)some other potential disadvantages:




> 
    * You are limited to 50,000 queries per user per day, which may pose some scalability concerns if you plan to build something big on this.
    * You have to be careful about the number of data points you submit in your request as you can quickly exceed the allowable URL length, and furthermore you might end up with illegibly smooshed-together data points due to the scale of your output.
    * There's always the "OMG Google will absorb all our data and become sentient, turn evil, and unleash an army of death robots on us all, run for your lives!" paranoia, but that's really just silly talk.





 EDIT:  It appears this service only support GET requests. On one hand you're adding new data so you should be POSTing it, right? On the other hand, you're asking to GET a graphical representation of a set of numerical values. What would a "restful" version of a web graphing API look like? Maybe some of the REST gurus can clear that up.






