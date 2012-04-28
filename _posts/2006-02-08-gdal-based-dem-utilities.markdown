---
date: '2006-02-08 00:53:53'
layout: post
slug: gdal-based-dem-utilities
status: publish
title: GDAL-based DEM utilities
wpid: '7'
---

<div class="alert alert-error">These DEM tools have been incorporated into GDAL. The code referenced on this page is no longer maintained and I'd highly recommend using <a href="http://www.gdal.org/gdaldem.html">gdaldem</a> instead.</div>

A few months ago, I began looking for some efficient command-line tools to analyze and visualize DEMs. I typically use GRASS for such tasks but GRASS only works with it's native raster format. Sure you can import/export to common formats but that's not as efficient as a single command line tool that could work with the native DEM format, run on systems without GRASS installed and provide easy scriptablity.  

Not having found anything that fit the bill, I decided to port some of the common GRASS DEM modules to C++ using the GDAL libraries. For someone with very little experience with C++, this was surprisingly not that difficult though I learned quite alot along the way.  The result: 3 command line utilities to generate hillshades, slope and aspect maps and 1 excellent utility contributed by Paul Surgeon to apply color ramping to a DEM.



###  Installation 





#### Requirements



I built these utilities on Ubuntu Linux. I admittedly have no idea how to compile them on Windows but some folks have confirmed that the hillshade code compiles under VC++. So to get these running under Linux (and presumably other *nixes), there are very minimal requirements:




 
  1. GDAL shared libraries  

 
  2. GNU C++ Compiler





#### Download


Get the [current source](/download/gdaldemtools_20060207.zip) and unzip it.  _**EDIT **_: This code is now avaible through my SVN repository : [http://perrygeo.googlecode.com/svn/trunk/demtools/](http://perrygeo.googlecode.com/svn/trunk/demtools/),



#### Compiling


Alas there is no makefile but installation should be fairly painless. To compile the source code under linux, the following commands should take care of it:


    g++ hillshade.cpp -lgdal -o hillshade
    g++ color-relief.cxx -lgdal -o color-relief
    g++ aspect.cpp -lgdal -o aspect
    g++ slope.cpp -lgdal -o slope
     



The four binaries can then be placed wherever your local binaries reside (typically /usr/local/bin)



###  Examples 





#### The original DEM


In this particular example the input DEM is a GeoTIFF but these utilities can use any [GDAL-supported raster source](http://gdal.maptools.org/formats_list.html).

![](/assets/img/dem/dem.jpg)



####  Slope 


This command will take a DEM raster and output a 32-bit GeoTiff with slope values. You have the option of specifying the type of slope value you want: degrees or percent slope. In cases where the horizontal units differ from the vertical units, you can also supply a scaling factor.



    slope dem.tif slope.tif


![](/assets/img/dem/slope.jpg)



####  Aspect 


This command outputs a 32-bit GeoTiff with values between 0 and 360 representing the azimuth of the terrain.



    aspect dem.tif aspect.tif


![](/assets/img/dem/aspect.jpg)



####  Hillshade 


This command outputs an 8-bit GeoTiff with a nice shaded relief effect. It's very useful for visualizing the terrain. You can optionally specify the azimuth and altitude of the light source, a vertical exaggeration factor and a scaling factor to account for differences between vertical and horizontal units.



    hillshade dem.tif shade.tif


![](/assets/img/dem/shade.jpg)



####  Color ramps 



After I posted the hillshade utility to the gdal-dev mailing list, there was some discussion about creating color relief maps to supplement the hillshades. Paul Surgeon took up the challenge and created a gdal-based C++ utility to colorize DEMs (or any other single band raster data sources for that matter). The technique is simple and powerful; by using a text-based color configuration file, you can create any range of color ramps for your data. 



    color-relief dem.tif scale.txt colordem.tif


Where scale.txt is a text file containting 4 columns per line, the elevation value and the corresponding RGB values:


    3500   255 255 255
    2500   235 220 175
    1500   190 185 135
    700    240 250 150
    0      50  180  50
    -32768 200 230 255
     



The colors between the given elevation values are blended smoothly and the result is a nice colorized DEM:
![](/assets/img/dem/colordem.jpg)



####  Color Shaded Relief (blending hillshade and colorized DEM) 


There are two ways I've come up with to blend the hillshade and the colorized DEM:



 
  1. Using GIMP or Photoshop, open both images, copy the shaded relief, paste on top of the color DEM and adjust the opacity in the layers dialog.
 
  2. If you're publishing to the web with Mapserver, just stack the two images in your mapfile and set the TRANSPARENCY for the hillshade to a value between 30 and 70 depending on your preference



 Though both methods work nicely, neither is really ideal since they don't generate a georeferenced tiff.  You can get around this in the GIMP method by creating a [world file (.tfw)](http://gdal.maptools.org/frmt_various.html#WLD) for the output tiff. It might be nice, in the future, to do this step programatically but for now...
![](/assets/img/dem/combine.jpg)


Let me know if you've got any suggestions or comments. The technique for all of these utilities is a simple 3x3 moving window so this code might serve as a good template to develop other raster processing utilities... let me know what you come up with!
