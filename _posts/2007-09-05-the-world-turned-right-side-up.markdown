---
date: '2007-09-05 14:45:25'
layout: post
slug: the-world-turned-right-side-up
status: publish
title: The world turned right-side up
wpid: '78'
---

I've been working alot in [Surfer](http://www.goldensoftware.com/products/surfer/surfer.shtml) these days; an excellent geostats and surface mapping package. I was very happy to find that GDAL read it's .grd binary format until I noticed the output from gdalinfo:



> C:\Workspace\Temp\interpolation>gdalinfo svpce_5.grd
Driver: GS7BG/Golden Software 7 Binary Grid (.grd)
Files: svpce_5.grd
Size is 555, 339
Coordinate System is `'
Origin = (383371.000000000000000,3764907.000000000000000)
Pixel Size = (0.500000000000000,0.500000000000000)
Corner Coordinates:
**Upper **Left  (  383371.000, **3764907.000**)
**Lower **Left  (  383371.000, **3765076.500**)
Upper Right (  383648.500, 3764907.000)
Lower Right (  383648.500, 3765076.500)
Center      (  383509.750, 3764991.750)
Band 1 Block=555x1 Type=Float64, ColorInterp=Undefined
 NoData Value=1.70141e+038



Notice that upper Y value is _south_ of the lower Y value! Basically the raster lines order is reversed (bottom-to-top instead of the normal raster orientation of top-to-bottom). I've also experienced the same issue with some NetCDF files so I thought it would be good to have a generic solution to the problem.

So I hacked up the gdal_merge.py script (distributed with gdal, fwtools, etc) and created a raster flip script that will invert the image along the y axis and retain the georeferencing and metadata. The resulting [flip_raster.py](http://perrygeo.googlecode.com/svn/trunk/gis-bin/flip_raster.py) script seems to work pretty well though it is far from tested.

Here's an example:

The standard gdal_translate method (which doesn't account for the inverted coordinate space):



> gdal_translate -of GTiff krig1.grd krig1_translate.tif


![](/assets/img/standard.jpg)

And the flipped raster method:



> flip_raster.py -o krig1_flip.tif -of GTiff krig1.grd 


![](/assets/img/flipped.jpg)

And we're good.  gdalinfo confirms that we have the same extents, pixel sizes, metadata, etc as the original dataset. 



