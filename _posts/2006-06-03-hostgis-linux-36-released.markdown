---
date: '2006-06-03 15:15:31'
layout: post
slug: hostgis-linux-36-released
status: publish
title: HostGIS Linux 3.6 Released
wpid: '51'
---

Though probably not as big of a news item as this week's [release of Ubuntu Dapper](http://www.ubuntu.com/news/606released), there's another Linux release that might be of interest to us GIS folk:

Built off of a [Slackware](http://www.slackware.com/) base (one of the oldest, most stable linux distros), [HostGIS Linux](http://www.hostgis.com/linux/) aims to be a "minimal yet complete" distribution specifically built with GIS in mind. It is first and foremost a server platform; it does not include any window system at all. If you're looking for desktop GIS applications out-of-box, it might not be the best for you. 

But for a GIS server, it comes with most of the open source stack preinstalled and configured. This latest release has [a few changes](http://www.hostgis.com/linux/manual/changes.html) and version upgrades for most of the components.




 
  * PHP, Python and Perl Mapscript 

 
  * GDAL/OGR with PHP, Python and perl bindings 

 
  * Postgresql 8.1 with PostGIS 1.1 

 
  * drivers for many extra formats including jpeg2000 and ecw 

 
  * Apache web server with Mapserver CGI 



 The primary motivation for creating HGL was to speed up the installation of new gis-enabled servers. Gregor Mosheh, the head programmer for HostGIS, has done an excellent job pretty much single-handedly putting this together. ( In full disclosure, I do consulting work for HostGIS, though I wasn't really involved in the creation of HostGIS Linux. )

The setup is your standard text-based install and is a piece of cake if you've ever installed Linux before. When you're through, you have the good ole' black and white text console staring at you. Not very interesting... But the really satisfying part is to fire up a web browser after the install and be able to point it to a working webGIS application. Anyone who has spent the time to set up the mapserver stack and its seemingly infinite dependencies can appreciate the amount of work this saves! 


If you're not into learning a new distro, there is always the [FGS](http://www.maptools.org/fgs/) linux installer which will set up a similar software stack on pretty much any linux.

And for Desktop GIS, many linux distros have a selection of GIS apps in their package repositories (You'll want to certainly grab GRASS, GDAL and QGIS) . [FWTools](http://fwtools.maptools.org/) can be a good option on both Linux and Windows to get you up and running quickly. Finally there are a number of other more desktop-oriented distros for GIS including [ Knoppix GIS](http://www.sourcepole.com/gis-knoppix/) and [GeoLivre](http://www.geolivre.org.br/modules/news/), both of which run as a live-cd so you can check it out before you install.

Anyways, back to sum up HostGIS Linux: 

If you need to set up a GIS server with minimal fuss and you have some experience with Linux, you might like to try it out. It will save lots of time. 

If you're a GIS user who needs a graphic windows environment to do GIS work on the Desktop, HostGIS Linux will not really make you happy out-of-the-box. Of course, since HGL is slackware based, you _can_ use the slackware package management system to build an impressive Desktop system. But if you don't need to run a server or really care about having the latest versions, Ubuntu comes with a solid desktop environment and packages for alot of good GIS apps. 



