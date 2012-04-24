---
date: '2007-10-19 15:00:35'
layout: post
slug: update-to-qgis-geocoding-plugin
status: publish
title: Update to QGIS Geocoding plugin
wpid: '88'
---

With the release of QGIS 0.9 imminent , I decided to install in on Windows XP and noticed that [the geocoding plugin ](http://www.perrygeo.net/wordpress/?p=60)was failing... sure enough I had hardcoded linux temporary directories. So I reworked the python code to determine the temp dir in a more cross-platform way (using tempfile.gettempdir() ) and it works fine.

The update can be downloaded [here](http://perrygeo.googlecode.com/svn/trunk/qgis/geocode.zip).

Assuming you've installed qgis in the standard location, just unzip this into C:\Program Files\Quantum GIS\python\plugins (windows) or /usr/share/qgis/python/plugins (Linux)  and you should be good to go.  Note that you'll have to create the "plugins" directory if it doesn't exist.

