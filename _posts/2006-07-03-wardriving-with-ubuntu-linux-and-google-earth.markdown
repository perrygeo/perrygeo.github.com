---
date: '2006-07-03 22:24:56'
layout: post
slug: wardriving-with-ubuntu-linux-and-google-earth
status: publish
title: Wardriving with Ubuntu Linux and Google Earth
wpid: '55'
---

Wardriving is fun. Going around the neighborhood and mapping all the wireless networks may be nothing more than a geeky hobby but it can sure teach you alot. And viewing the results in Google Earth is icing on the cake.

I've used NetStumbler on windows and this works great but since my computers at home are now nearly Microsoft-free, I had to relearn the process on Linux. It breaks down into a few easy steps:





  1. Install the **drivers** for you wireless card. On my HP laptop with a Broadcom card, I followed the instructions on the [ ubuntu forums ](http://ubuntuforums.org/showthread.php?p=1071920&mode=linear) which worked great with one exception: the driver link on that page doesn't have a valid md5 sum so you can download it from [this url](http://forums.fedoraforum.org/forum/attachment.php?attachmentid=7759) instead


  2. 
Install **gpsd.** This is the software that talks to your gps unit and is available in the ubuntu packages through apt. The one hitch is that I had to set up my Magellan GPS unit up for the correct baud rate and NMEA output. Once installed, I connected the GPS unit via a serial port, turned it on and ran _ gpsd /dev/ttyS0 _ to start the gpsd server.



  3. 
Install **kismet,** the wireless packet sniffer. The version in the ubuntu repository is not recent enough to support my Broadcom driver so I had to download the latest source and compile it with the standard _ configure, make, sudo make install _.  Then I had to edit the /usr/local/etc/kismet.conf to reflect my system configuration; I changed the _suiduser_, _source_ and _logtemplate_ variables. Once configured, you can start it with the command _sudo kismet_.



  4. 
Now **drive/bike/walk around** for a bit with your laptop and gps unit. When you're done, shutdown kismet and you'll have a bunch of fresh logfiles to work with.



  5. 
 The main kismet log is an xml file containing all the info on the available wireless networks including their SSID, their encryption sheme, transfer rater and their geographic position via gpsd. I worked up a small python script, [kismet2kml.py](http://perrygeo.googlecode.com/svn/trunk/gis-bin/kismet2kml.py) (based on a blog entry at [jkx@Home](http://www.larsen-b.com/Article/204.html)), to **parse the logfile into a KML file** for use with Google Earth. It could certainly use some tweaking but it's a start. To run it, give it the kismet logfile and pipe the output to a kml file:  
_ kismet2kml.py kismet-log-Jul-03-2006-1.xml > wardrive.kml _


  6. 
 Now fire up **Google Earth** (Linux version now available!) and load your KML file.




![](/assets/img/kismetkml.jpg)
  

Also, as James Fee [points out](http://www.spatiallyadjusted.com/2006/07/03/help-me-think-of-a-good-mashup-to-create/), posting your data as KML files means that the data can be integrated into a growing number of kml-ready apps including google maps (just upload the kml and point your browser to _http://maps.google.com/maps?q=http://your.server/wardrive.kml_).  
  

Another neat application I've found for dealing with kismet logs is the [kismet2gpx script](http://wiki.openstreetmap.org/index.php/User:Dutch#Converting_Kismet_.gps_files_to_gpx) for converting the kismet gps tracklog into gpx. Since most gps units have pretty tight limitations on the length of stored tracks, logging them to your laptop with kismet could be an effective way of creating detailed tracks on very long trips.
