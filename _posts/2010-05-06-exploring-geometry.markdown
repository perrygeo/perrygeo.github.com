---
date: '2010-05-06 18:35:54'
layout: post
slug: exploring-geometry
status: publish
title: Exploring Geometry
wpid: '143'
---

I don't know how I let this gem slip past my radar for so long. It was only via [a post by Dr. JTS](http://lin-ear-th-inking.blogspot.com/2010/05/random-points-in-polygon-in-jts.html) himself (aka Martin Davis) that I saw a screenshot of JTS TestBuilder and decided to check it out. 

I was actually just talking with someone about a tool that could provide simple visualization of WKT geometries;  JTS Test Builder does that and much more. 

You can input geometries (graphically or by well-known text) and compare two geometries based on spatial predicates:

[![spatial predicates](/assets/img/uploads/2010/05/screen-shot-2010-05-06-at-81418-pm.png)](/assets/img/uploads/2010/05/screen-shot-2010-05-06-at-81418-pm.png)

Do overlay analyses with the two geometries. Note that you can see the result as WKT below.

[![overlay](/assets/img/uploads/2010/05/screen-shot-2010-05-06-at-81502-pm.png)](/assets/img/uploads/2010/05/screen-shot-2010-05-06-at-81502-pm.png)

And there are a host of other spatial operations to generate geometries using buffers...
[![buffers](/assets/img/uploads/2010/05/screen-shot-2010-05-06-at-81602-pm.png)](/assets/img/uploads/2010/05/screen-shot-2010-05-06-at-81602-pm.png)

... convex hulls ...
[![convex hull](/assets/img/uploads/2010/05/screen-shot-2010-05-06-at-81716-pm.png)](/assets/img/uploads/2010/05/screen-shot-2010-05-06-at-81716-pm.png)

This app provides a very nice and user-friendly way to quickly and simply explore and test geometric operations. To try it out, [download JTS](http://sourceforge.net/projects/jts-topo-suite/) and unzip the contents somewhere. If you're on windows, the .bat file is provided. If you're running anything else, you have to cook up a shell script that will set up the environment and run JTS TestBuilder:



> 
>     JTS_HOME=/usr/share/java/jts-1.11
>     CP=$CLASSPATH
>     for i in $JTS_HOME/lib/*.jar; do CP=$i:$CP; done
>     java -Xmx256m -cp $CP com.vividsolutions.jtstest.testbuilder.JTSTestBuilder $*
>     






