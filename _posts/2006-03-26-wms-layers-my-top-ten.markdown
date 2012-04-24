---
date: '2006-03-26 20:25:26'
layout: post
slug: wms-layers-my-top-ten
status: publish
title: 'WMS layers: My Top Ten'
wpid: '35'
---

Web Mapping Services (WMS) are not always my prefered option for accessing data; relying on a remote server to generate a pretty picture of the data is hardly a substitute for having the raw data in hand. But for many cases, I just need a decent looking basemap image and don't want to download gigabytes of data, especially if that data is updated frequently. 

Software like GeoServer and Mapserver are making it easier to publish data via WMS and the number of WMS servers is surely growing... but how do you find them? There is no central registry for WMS servers but efforts like the [refractions research ogc survey](http://www.refractions.net/white_papers/ogcsurvey/), [mapdex](http://www.mapdex.org/wms_list.cfm) and a few [google tricks](http://chris.narx.net/2006/01/19/wms-service-mining/) are making it easier to find data distributed via WMS.  After many hours digging through WMS services to find the ones that suite my mapping needs, I've come across a number of gems that I use time and time again. Hopefully this will inspire some others to share their secret stash of WMS servers! 

(**Update:** [Anything Geospatial](http://my.opera.com/gisuser/blog/show.dml/199960) has a great link to a well-organized [ WMS server list](http://www.skylab-mobilesystems.com/en/wms_serverlist.html) for public use. Nice. )

You should be able to provide the online resource URL to your favorite WMS client software (my personal choice is  [openjump](http://openjump.org/wiki/show/HomePage)) and the client should display the list of layers available from that service. 

If you're contructing WMS URLs "by hand" or in a browser, you can do a capabilities request (the online resource URL with _service=WMS?request=GetCapabilities _ appended to it) which will return an XML document describing the available layers, image formats, projections,etc. Take a look at the image src for any of the thumbnails below to see how the map request is constructed.






  1. TerraServer Digital Raster Graphic (DRG): USGS Topo Quads
 ** Online Resource URL ** : _ http://terraservice.net/ogcmap.ashx? _   

 ** Layer Name ** : _DRG_
![](http://terraservice.net/ogcmap.ashx?VERSION=1.1.1&SERVICE=wms&request=GetMap&LAYERS=DRG&FORMAT=jpeg&styles=&SRS=EPSG:4326&BBOX=-124.1,41.2,-123.9,41.4&WIDTH=150&HEIGHT=150)


  2. TerraServer Digital Ortho Photo Quads (DRG): Black and white aerial photos for the US
 ** Online Resource URL ** : _ http://terraservice.net/ogcmap.ashx? _   

 ** Layer Name ** : _DOQ_
![](http://terraservice.net/ogcmap.ashx?VERSION=1.1.1&SERVICE=wms&request=GetMap&LAYERS=DOQ&FORMAT=jpeg&styles=&SRS=EPSG:4326&BBOX=-124.1,41.2,-123.9,41.4&WIDTH=150&HEIGHT=150)


  3. NASA Landsat Imagery
 The Landsat mosaic is available in fase color (default) or in natural color (style=visual) as shown below.   

 ** Online Resource URL ** : _http://onearth.jpl.nasa.gov/wms.cgi?_   

 ** Layer Name ** : _global_mosaic_ 
![](http://onearth.jpl.nasa.gov/wms.cgi?VERSION=1.1.1&SERVICE=wms&request=GetMap&LAYERS=global_mosaic&FORMAT=image/png&styles=visual&SRS=EPSG:4326&BBOX=-124.1,41.2,-123.9,41.4&WIDTH=150&HEIGHT=150)



  4. 45-minute Weather Radar Images (NEXRAD Base Reflectivity).
Since this is a dynamic data source, the image below may look really boring (ie blank) if there's no storms over the Continental US.   

 ** Online Resource URL ** : _http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi?_   

 ** Layer Name ** : _nexrad-n0r-m45m_ 

![](http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi?VERSION=1.1.1&SERVICE=wms&request=GetMap&LAYERS=nexrad-n0r-m45m&FORMAT=jpeg&styles=&SRS=EPSG:4326&BBOX=-125,25,-65,55&WIDTH=300&HEIGHT=150)


  5. USGS National Landcover
The 30-meter natial landcover dataset. USGS is nice enough to provide a legend, of course.   

 ** Online Resource URL ** : _http://gisdata.usgs.net/servlet/com.esri.wms.Esrimap?ServiceName=USGS_WMS_NLCD&_   

 ** Layer Name ** : _US_NLCD_ 








![](http://gisdata.usgs.net/servlet/com.esri.wms.Esrimap?ServiceName=USGS_WMS_NLCD&request=GetMap&LAYERS=US_NLCD&FORMAT=image/png&SRS=EPSG:4326&BBOX=-124.1,41.2,-123.9,41.4&WIDTH=150&HEIGHT=150)




![](http://gisdata.usgs.net/Image_Library/legends/Legend_NLCD5.png)





  6. USGS National Elevation - Shaded Relief
 ** Online Resource URL ** : _http://gisdata.usgs.net:80/servlet/com.esri.wms.Esrimap?servicename=USGS_WMS_NED&_   

 ** Layer Name ** : _US_NED_Shaded_Relief_ 
![](http://gisdata.usgs.net:80/servlet/com.esri.wms.Esrimap?servicename=USGS_WMS_NED&request=GetMap&LAYERS=US_NED_Shaded_Relief&FORMAT=image/jpeg&SRS=EPSG:4326&BBOX=-124.1,41.2,-123.9,41.4&WIDTH=150&HEIGHT=150)


  7. USGS Reference Maps 
 ** Online Resource URL ** : _http://gisdata.usgs.net:80/servlet/com.esri.wms.Esrimap?servicename=USGS_WMS_REF&_   

 ** Layer Names ** : _States,County,Roads,Route_Numbers,Streams,Federal_Lands_ 
![](http://gisdata.usgs.net:80/servlet/com.esri.wms.Esrimap?servicename=USGS_WMS_REF&request=GetMap&LAYERS=States,County,Roads,Route_Numbers,Streams,Federal_Lands&FORMAT=image/png&SRS=EPSG:4326&BBOX=-124.1,41.2,-123.9,41.4&WIDTH=150&HEIGHT=150)


  8. Life Mapper 
Besides the standard WMS paramters, some services can take extra parameters in order to render a map. In this excellent service, LifeMapper requires that you provide the species name and it will render maps of known species locations and modelled distributions. Here's an example of the distribution of Black Bear (ie. _Ursus americanus_) over central california   

 ** Online Resource URL ** : _http://www.lifemapper.org/Services/WMS/?ScientificName=Ursus%20americanus&_   

 ** Layer Names ** : _Species Distribution Models,Political Boundaries,Species Data Points_ 

![](http://www.lifemapper.org/Services/WMS/?Version=1.1.0&Request=GetMap&width=150&height=150&Bbox=-124.1,35.4,-118.1,41.4&Layers=Species%20Distribution%20Models,Political%20Boundaries,Species%20Data%20Points&Styles=&ScientificName=Ursus%20americanus&SRS=EPSG:4326&format=image/gif)


  9. MODIS Daily Satellite Imagery
 ** Online Resource URL ** : _http://wms.jpl.nasa.gov/wms.cgi?_   

 ** Layer Names ** : _daily_terra, daily_aqua_ 





Terra 
Aqua 






![](http://wms.jpl.nasa.gov/wms.cgi?request=GetMap&LAYERS=daily_terra&FORMAT=image/png&SRS=EPSG:4326&BBOX=-124.1,35.4,-118.1,41.4&WIDTH=150&HEIGHT=150&styles=)




![](http://wms.jpl.nasa.gov/wms.cgi?request=GetMap&LAYERS=daily_aqua&FORMAT=image/png&SRS=EPSG:4326&BBOX=-124.1,35.4,-118.1,41.4&WIDTH=150&HEIGHT=150&styles=)





  10. SRTMPlus 90 Meter DEM
The image below doesn't make for a very good basemap OR a very good DEM for analytical purposes since all the values are scaled to an 8-bit color depth. However, JPL also offers this layer as an integer (16bit) GeoTIFF (Use _format=image/geotiff_ and _styles=short_int_), so this can be a valuable way to quickly grab a DEM for a given region. 
 ** Online Resource URL ** : _http://wms.jpl.nasa.gov/wms.cgi?_   

 ** Layer Names ** : _srtmplus_ 
![](http://wms.jpl.nasa.gov/wms.cgi?request=GetMap&LAYERS=srtmplus&FORMAT=image/png&SRS=EPSG:4326&BBOX=-124.1,35.4,-118.1,41.4&WIDTH=150&HEIGHT=150&styles=)





* * *


If you'd like to view these layers interactively, here's a mapserver application which "cascades" the above WMS layers through a single interface. If you're interested in setting up these layers in a mapserver application, check out the [WMS Mapfile ](http://perrygeo.net/download/fav_wms.txt) for some examples.

