---
date: '2008-04-15 20:43:09'
layout: post
slug: spatial-data-in-sqlite
status: publish
title: Spatial data in SQLite
wpid: '115'
---

Slashgeo pointed me to a very interesting set of projects - [SpatiaLite and VirtualShape](http://www.gaia-gis.it/spatialite/). They provide a spatial data engine for the [sqlite](http://www.sqlite.org/index.html) database. Think of it as the PostGIS of SQLite. It looks like this extends sqlite's spatial capabilities far beyond the [sqlite OGR driver](http://www.gdal.org/ogr/drv_sqlite.html).

SpatiaLite provides many of the basic OGC Simple Features functions - transforming geometries between projections, spatial operations of bounding boxes, and some basic functions to disect, analyze and export geometries. 

VirtualShape provides the really neat ability to access a shapefile using the SpatiaLite/SQlite interface without having to import a copy - it reads directly off the shapefile by exposing the shapefile and its attributes as a "virtual table". I can think of a million uses for this. For example, lets say you have a shapefile of US counties and the number of voter in the 2004 election as an attribute in the dbf. You want to find the total voter count in each state:

`
    
    
    $ ls -1 counties.*
    counties.dbf
    counties.prj
    counties.shp
    counties.shx
    $ sqlite3 test.db
    sqlite> .load 'SpatiaLite.so'
    sqlite> .load 'VirtualShape.so'
    sqlite> CREATE virtual table virtual_counties using VirtualShape(counties);
    sqlite> select sum(voters) as total_voters, state_name 
               from virtual_counties 
               group by state_name 
               order by total_voters desc;
    9830550.0|California
    7563055.0|Florida
    7346779.0|Texas
    ...
    
    


`
Now this is fairly straightforward non-spatial SQL but the ability to run it against a shapfile without having to export to an intermediate data format is a very valuable tool. 

Links: 
[When to use SQlite.](http://www.sqlite.org/whentouse.html)
A [video presentation](http://video.google.com/videoplay?docid=-5160435487953918649) by Richard Hipp (the author of sqlite).
