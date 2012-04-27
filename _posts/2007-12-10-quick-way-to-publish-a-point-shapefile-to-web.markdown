---
date: '2007-12-10 20:14:14'
layout: post
slug: quick-way-to-publish-a-point-shapefile-to-web
status: publish
title: Quick way to publish a point shapefile to html
wpid: '97'
---

There are better ways to put data on the web but my latest little project wasn't about the _best_ way but the quickest way to get some spatial data into the hands of those unfortunate souls who don't have GIS software. The goals were pretty simple:





  * Take a single point shapefile (or other OGR readable vector data source)


  * Convert it into html/js that would use one of the web mapping APIs to display the points and all their attributes. 


  * The output had to be a standalone, self-contained html file that could be emailed. No server side anything required.




I came up with a quick python hack to do the job ([source code](http://perrygeo.googlecode.com/svn/trunk/gis-bin/shp2Mapstraction.py)). [Mapstraction](http://www.mapstraction.com/), with it's goal of providing a common javascript API for a number of map providers, seemed like an obvious choice.  The python portion of the code reads the shapefile using OGR (you will need the python-gdal bindings, see FWTools) and constructs the html/js. All the javascript is sourced to external URLs so there is no software dependency except for a working network connection. 

This allows for a single command:


> shp2Mapstraction.py bearboxes.shp bearboxes.html Yahoo



![](/assets/img/bearboxes.jpg)

which produces [an html file](/assets/img/bearboxes.html) providing a Yahoo maps interface to the data; in this case the point location of all the bear boxes (food storage lockers to keep your stuff separated from the bears) in the Sierra Nevada. 

Currently it just supports Microsoft Virtual Earth and Yahoo. I had to bypass Google because their key system is restricted by URL. And the mapstraction-to-openlayers connection wasn't working too well though I haven't really investigated.

Anyways, it provides a quick and easy way to deliver spatial data to anyone with a browser and internet connection. 

