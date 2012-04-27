---
date: '2010-02-18 09:16:43'
layout: post
slug: lazy-raster-processing-with-gdal-vrts
status: publish
title: Lazy raster processing with GDAL VRTs
wpid: '141'
---

No, not lazy as in REST :-) ... Lazy as in "[Lazy evaluation](http://en.wikipedia.org/wiki/Lazy_evaluation)":



> In computer programming, lazy evaluation is the technique of delaying a computation until the result is required.



Take an **example raster processing workflow** to go from a bunch of tiled, latlong, GeoTiff digital elevation models to a single shaded relief GeoTiff in projected space:






  1. Merge the tiles together 


  2. Reproject the merged DEM (using bilinear or cubic interpolation) 


  3. Generate the hillshade from the merged DEM 




Simple enough to do with GDAL tools on the command line. Here's the typical, **process-as-you-go** implementation:





```
  1. gdal_merge.py -of GTiff -o srtm_merged.tif srtm_12_*.tif 


  2. gdalwarp -t_srs epsg:3310 -r bilinear -of GTiff srtm_merged.tif srtm_merged_3310.tif 


  3. gdaldem hillshade srtm_merged_3310.tif srtm_merged_3310_shade.tif -of GTiff 
```



Alternately, we can simulate **lazy evaluation** by using [GDAL Virtual Rasters](http://www.gdal.org/gdal_vrttut.html) (VRT) to perform the intermediate steps, only outputting the GeoTiff as the final step. 





	
  1. gdalbuildvrt srtm_merged.vrt srtm_12_0*.tif

	
  2. gdalwarp -t_srs epsg:3310 -r bilinear -of VRT srtm_merged.vrt srtm_merged_3310.vrt 

	
  3. gdaldem hillshade srtm_merged_3310.vrt srtm_merged_3310_shade2.tif -of GTiff




So what's the advantage to doing it the VRT way? They both produce _exactly_ the same output raster. Lets compare:







Process-As-You-Go
"Lazy" VRTs



Merge (#1) time 
3.1 sec
0.05 sec 



Warp (#2) time 
7.3 sec 
0.10 sec 



Hillshade (#3) time
10.5 sec 
19.75 sec



Total processing time
20.9 sec
19.9 sec 



Intermediate files
2 tifs
2 vrts



Intermediate file size
261 MB
0.005 MB






  


The Lazy VRT method **delays all the computationally-intensive processing until it is actually required**. The intermediate files, instead of containing the raw raster output of the actual computation, are XML files which contain the _instructions_ to get the desired output. This allows GDAL to do all the processing in one step (the final step #3). The _total_ processing time is not significantly different between the two methods but in terms of the productivity of the GIS analyst, the VRT method is superior. Imagine working with datasets 1000x this size with many more steps - having to type the command, wait 2 hours, type the next, etc. would be a waste of human resources versus assembling the instructions into vrts then hitting the final processing step when you leave the office for a long weekend.

Additionaly, the VRT method produces only **small intermediate xml files** instead of having a potentially huge data management nightmare of shuffling around GB (or TB) of intermediate outputs! Plus those xml files serve as an excellent piece of metadata which describe the exact processing steps which you can refer to later or adapt to different datasets. 

So next time you have a multi-step raster workflow, use the GDAL VRTs to your full advantage - you'll save yourself time and disk space by being lazy. 



