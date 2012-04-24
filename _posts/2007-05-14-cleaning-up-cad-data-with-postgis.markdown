---
date: '2007-05-14 11:58:28'
layout: post
slug: cleaning-up-cad-data-with-postgis
status: publish
title: Cleaning up CAD data with postgis
wpid: '66'
---

Don't you just love getting CAD data into GIS! I received a .dwg file with study areas delineated as polylines which we needed as polygons for analysis purposes. And it wasn't just one polyline surrounding each study area ... there were hundreds of little line segments which outlined a couple dozen areas (what was this CAD tech thinking?) . Luckily each segment had a name to associate it with the proper area.

I found that ArcMap's tools for doing this are painfully inadequate so I turned to postgis. After converting the dataset to a shapefile, the solution was simple:



> shp2pgsql "study_areas.shp" areas | psql -d gisdata
pgsql2shp -f "study_areas_poly.shp" gisdata \
   "SELECT BuildArea(collect(the_geom)) AS the_geom, name 
    FROM areas 
    GROUP by name"



Viola... a new shapefile with my proper polygons instead of CAD chicken scratch. 
