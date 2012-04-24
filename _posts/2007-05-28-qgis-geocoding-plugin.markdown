---
date: '2007-05-28 10:11:23'
layout: post
slug: qgis-geocoding-plugin
status: publish
title: QGIS Geocoding plugin
wpid: '60'
---

A few weeks back, I decided to take the plunge and learn the python bindings for QGIS 0.9. My first experiment was to implement a geocoder plugin. What started mostly as a learning experiment turned into something that might actually be useful!

The idea was to use web services to do all the actual geocoding work (the hard part!) and the delimited text provider to load the results into qgis. Right now it's built on top of the [Yahoo geocoder](http://developer.yahoo.com/maps/rest/V1/geocode.html) which is, IMO, the best out there.. very flexible about the input format. The [geopy module](http://exogen.case.edu/projects/geopy/) is used to interact with the geocoding services so it could potentially support other engines such as geocoder.us, virtual earth, google, etc. 

 The user interface is very straightforward; enter list of addresses/placenames seperated by a line break, pick an output file and go. To be legitimate, you should also sign up for a yahoo api key, though the 'YahooDemo' key will work ok for testing purposes.

[![](/img/dialog_thumb.jpg)](/img/dialog.jpg)

[![](/img/result_thumb.jpg)](/img/result.jpg)

Here's the install process (assuming you already have [python, pyqt4, qgis 0.9, qgis bindings, etc. set up](http://www.reprojected.com/presentations/Videos/qgis_install_051407/install_qgis.txt)):



>  svn checkout http://perrygeo.googlecode.com/svn/trunk/qgis/geocode
>      cd geocode
>      emacs Makefile # change install directory if needed
>      sudo make install



This is just a rough cut and it's my first attempt at using the qgis and qt apis so there are probably many things that could be improved upon. Ideally this plugin could:




  * Parse text files as input 


  * Allow for a choice of geocoding engine 


  * ??? 



Feedback (and patches) welcome ;-)
