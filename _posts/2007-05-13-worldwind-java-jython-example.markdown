---
date: '2007-05-13 14:32:53'
layout: post
slug: worldwind-java-jython-example
status: publish
title: Worldwind Java - Jython example
wpid: '59'
---

The [ worldwind java sdk ](http://worldwind.arc.nasa.gov/java/index.html) has finally been released.  It's a neat SDK, well organized, [easy to bring into Eclipse](http://tleilax.chinoy.com/worldwind/articles/20070510-FirstImpressions.html) with some good examples to start hacking away.

The only problem is the examples are written in Java  ;-) . If braces make you cringe but you still want to work with all the excellent Java libraries out there, you'll want to take a look at Jython. Taking the AWT1Up.java code and porting a subset of the functionality to Jython was surprisingly easy and yielded much more readable code in my opinion. And the ability to manipulate objects at the interactive prompt is just so sweet. 


[ ![](/assets/img/wwj_jython_thumb.jpg) ](/assets/img/wwj_jython.jpg)
  

[ View the Source Code ](http://perrygeo.googlecode.com/svn/trunk/gis-bin/wwj_demo.py)

Setup is not too terrible:



 
  1. Get a Java JDK (I'm using sun java 6) 

 
  2. Download and install Jython 2.2b2 

 
  3. Download and unzip the worldwind java sdk (ex: /opt/wwj )

 
  4. Set your LD_LIBRARY_PATH variable to /opt/wwj

 
  5. Set your CLASSPATH variable to /opt/wwj/worldwind.jar

 
  6. Run `jython wwj_demo.py`



One thing that is a bit disappointing with the WorldWind SDK in general is the lack of support for rendering common formats. Maybe I missed something but I couldn't get gpx or georss feeds working properly.  It is version 0.2 so I expect support for GeoRSS and GPX to improve and for GML, KML, GeoJSON, Shapefiles, Rasters, WMS, etc to be included eventually.

Anyone else out there started playing with Jython / Worldwind yet?


