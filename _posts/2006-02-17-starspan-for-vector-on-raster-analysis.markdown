---
date: '2006-02-17 21:07:44'
layout: post
slug: starspan-for-vector-on-raster-analysis
status: publish
title: StarSpan for vector-on-raster analysis
wpid: '30'
---

It's amazing how many excellent open source GIS applications are out there just waiting to be discovered. I've been working with open source GIS for over 3 years now and I still find new and interesting software on a regular basis. The latest "Why haven't I heard of this before?" discovery came from the GRASS mailing list discussion on [StarSpan](http://starspan.casil.ucdavis.edu/), a tool developed at University of California at Davis "_designed to bridge the raster and vector worlds of spatial analysis using fast algorithms for pixel level extraction from geometry features_". 

Our research project for the [Ecosystem Based Management group at UCSB](http://ebm.nceas.ucsb.edu) is in need of this exact tool in order to extract raster statistics based on a vector watersheds layer. ArcGIS and GRASS both have _some_ of the capabilities we need through the Zonal_Statistics and v.rast.stats functions respectively. However they have their limitations and neither really handles categorical raster summaries by polygon. StarSpan looks like a more efficient option in terms of speed, scriptability and capabilities.

Installation is very smooth. It requires a recent version of GDAL (>= 1.2.6) and GEOS (>= 2.1.2). Once the dependencies are met, compilation on a *nix system is as easy as configure, make, make install (There are also Windows binaries available). There is a single command line interface for all the functionality and StarSpan is able to handle all [GDAL rasters](http://www.gdal.org/formats_list.html) and [OGR vectors](http://www.gdal.org/ogr/ogr_formats.html).

For classified rasters such as a land cover raster, we'd like to get the number of pixels for each landcover class by watershed. StarSpan creates a nice, normalized csv with three columns; The vector feature id, the raster value, and the number of pixels. There will be up to  (number of features X number of classes) rows.



> starspan --vector watershed.shp --raster landcover.tif --count-by-class landcover_by_watershed.csv



In order to find the percentage of a given raster class for each watershed, you can bring the csv into a relational database and do a quick SQL query. Here's an example of finding the percentage of cropland (class value is 12) for each watershed:



> 
>     SELECT t.fid AS fid, (t.count::numeric / s.total::numeric) * 100 AS percentage_cropland
>     FROM landcover_by_watershed t,
>                    (SELECT fid, sum(count) AS total 
>                     FROM lancover_by_watershed 
>                     GROUP BY fid) as s 
>     WHERE t.fid = s.fid
>     AND t.class = 12; 
>     



Which gives us...



> 
>      fid |      percentage_cropland
>     -----+------------------------------------------------
>        1 | 28.571428571428571429
>        2 | 71.428571428571428571
>        3 | 36.363636363636363636
>        4 | 63.636363636363636364
>     



For continuous surfaces such as elevations and slopes, we'll need to get quantitative statistics of those rasters by watershed. StarSpan can easily generate averages, mode, standard deviation, min and max:





> starspan --vector watershed.shp --raster slope.tif --stats slope_stats.csv avg mode stdev min max





Which outputs a csv with one row per feature identified by feature id and each stat as a column:




> 
>     FID,numPixels,avg_Band1,mode_Band1,stdev_Band1,min_Band1,max_Band1
>     1,25921,34.694822,38.917000,14.491952,0.347465,66.241035
>     2,21755,7.965552,0.000000,5.484245,0.000000,42.017155
>     ...
>     





While I can confirm that these small test cases work very quickly and give us pretty much the exact outputs we need, it will be interesting to see how well it stacks up to ArcGIS and GRASS when it comes to cranking out the big datasets. We'll likely try all three methods and I'll make sure to post the results. 

Oh and the comparison between StarSpan and GRASS may become at moot point in the future since there is talk about integrating it with the GRASS project. While a GRASS module would be nice, not everyone has GRASS installed so I would hope the stand-alone version is still maintained since it can deal with pretty much any vector or raster data source.
