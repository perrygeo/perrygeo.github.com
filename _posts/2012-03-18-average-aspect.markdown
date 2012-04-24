---
date: '2012-03-18 07:26:32'
layout: post
slug: average-aspect
status: publish
title: Average Aspect
wpid: '162'
---

Ever try to figure out what the average aspect of an area is? i.e. 



> What direction does this hillside face? 




Let's say we want to determine the average elevation of an area based on a raster DEM. Just take the arithmetic mean of all the elevation cells contained in the area - a simple zonal statistics problem.

Turns out that aspect is not quite as straightforward. True, we can easily use [gdaldem](http://www.gdal.org/gdaldem.html) to create an aspect map.

`
gdaldem aspect elevation.tif aspect.tif`

This gives a raster with values in degrees: 0 is north, 90 is east, 180 is south, etc... but note that 360 is north as well.  We're dealing with angular units, not linear units. 

For example, take a nearly North facing hillside; the left edge is facing slightly NW while the right edge faces slighty NE.







350° 


10° 






350° 


10° 




The arithmetic mean of the aspect values = (350+350+10+10)/4 = 180°. Due south? That's entirely wrong! It doesn't take into account the angular units. For that we need to create grids representing the _sin_ and _cos_ of the aspect. 

Luckily you can use the handy [gdal_calc.py](http://svn.osgeo.org/gdal/trunk/gdal/swig/python/scripts/gdal_calc.py) utility that comes with recent versions of gdal. This allows you to apply numpy's trigonometric functions to a raster...

`
gdal_calc.py -A aspect.tif --calc "cos(radians(A))" --format "GTiff" --outfile cos_aspect.tif  
gdal_calc.py -A aspect.tif --calc "sin(radians(A))" --format "GTiff" --outfile sin_aspect.tif`

Now we can look at the sum of the cos/sin grid cells for our area and take the arctangent according to this python code

`
import math
avg_aspect_rad = math.atan2(sum(cos_cells), sum(sin_cells))
avg_aspect_deg = math.degrees(avg_aspect_rad)
print avg_aspect_deg 
`

In our example avg_aspect_deg comes out to an aspect of 0 degrees (due north) which is exactly what we'd expect. 

Thanks to Dan Patterson for his [forum post](http://forums.esri.com/Thread.asp?c=3&f=40&t=119358&mc=8#343468) which clued me into this approach. 
