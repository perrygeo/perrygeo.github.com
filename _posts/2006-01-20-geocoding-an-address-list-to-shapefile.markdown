---
date: '2006-01-20 18:50:39'
layout: post
slug: geocoding-an-address-list-to-shapefile
status: publish
title: Geocoding an address list to shapefile
wpid: '5'
---

Most commercial software comes with fairly elaborate geocoding engines and there are nice geocoding services on the web that can do one-at-a-time geocoding but the [recent post](http://www.spatiallyadjusted.com/2006/01/20/batch-geocode-tabular-address-data-via-your-web-browser/) at Spatially Adjusted pointed out a great free resource for batch geocoding named, conveniently enough, [Batch Geocode](http://www.batchgeocode.com/). Just give it a list of tab or pipe delimited addresses and it outputs a table with your original data plus a lat/long for every row.

I have been working on a python script to convert text files into point shapefiles and thought this would be a great chance to put it to work. The only dependency is a recent version of python with the ogr module (see [FWTools](http://fwtools.maptools.org) for an easy to install package for windows or linux).

First, I take a list of cities and feed it to batchgeocode.com (a very nice feature is that the yahoo geocoder, on which batchgeocode is based, does not _require_ street level addresses):



> City|State
>     Santa Barbara|CA
>     Arcata|CA
>     New Milford|CT
>     Blacksburg|VA



After running the geocoder, I get back a table with lat/longs:



> 
>     City|State|lat|long|precision
>     Santa Barbara|CA|34.419769|-119.696747|city
>     Arcata|CA|40.866261|-124.081673|city
>     New Milford|CT|41.576599|-73.408821|city
>     Blacksburg|VA|37.229359|-80.413963|city



Copy and paste that into a text file and add a second header row that defines the data type for each column. It would be possible to autodetect the column types but there are cases where a string of numeric digits should be kept as a string (for instance the zipcode _06776_ would become _6776_ if it was read as an integer).The possible column types are _string, integer,real, x_ and _y_ with x and y representing the coordinates.



> 
>     City|State|lat|long|precision
>     string|string|y|x|string
>     Santa Barbara|CA|34.419769|-119.696747|city
>     Arcata|CA|40.866261|-124.081673|city
>     New Milford|CT|41.576599|-73.408821|city
>     Blacksburg|VA|37.229359|-80.413963|city



Now run the _txt2shp.py_ utility. The input and output parameters are self-explanatory and the d parameter defines the string used as a delimiter. Notice that the syntax follows the GRASS standard of _parameter=value_:



> 
>     txt2shp.py input=cities.txt output=cities.shp d='|'



And now you've got a shapefile of the geocoded cities! 

![Cities Shapefile](http://perrygeo.net/img/cities.png)

The txt2shp.py script can be downloaded [ here](http://perrygeo.net/download/txt2shp.py). Try it out and let me know how  it's working for you.

**Update:** In order to generate a .prj file for your output shapefile, you can use the epsg_tr.py utility if you know the EPSG code. Batch Geocoder returns everything in lat/long (presumably with a WGS84 datum?) so you can use EPSG code 4326:



> epsg_tr.py -wkt 4326 > cities.prj










