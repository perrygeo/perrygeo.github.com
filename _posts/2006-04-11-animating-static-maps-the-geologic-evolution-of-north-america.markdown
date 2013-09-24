---
date: '2006-04-11 18:24:53'
layout: post
slug: animating-static-maps-the-geologic-evolution-of-north-america
status: publish
title: Animating Static Maps - The Geologic Evolution of North America
wpid: '39'
---

The Cartography blog [ recently talked about ](http://ccablog.blogspot.com/2006/04/paleogeographic-maps.html) a series of [excellent Paleogeographic maps](http://jan.ucc.nau.edu/%7Ercb7/nam.html) developed by Dr. Ron Blakey at Northern Arizona University.  Ever since I first studied geology, I had dreamed of an atlas that would clearly and visually demostrate how our current land masses came to be.  This time series of maps focuses on North America and the geologic events that shaped have shaped it for the last 500 million years. Truly fascinating and excellent work. I encourage everyone to check out the site and read a little about it as well as [ the narrative by Geoff Manaugh](http://bldgblog.blogspot.com/2006/04/assembling-north-america_11.html) . 

![](/assets/img/29.gif)

Now it occured to me that a time series of maps lends itself very well to an animated sequence. While I am no graphic artist, I have done a few projects in the past that required stiching together a time-series of maps into an animated gif. The process is fairly simple:





  1. Download or create each map you want to include in the series. For best results, all maps should have the same size and extents.


  2. Rename the images in alpha-numeric order (001.jpg, 002.jpg.... 045.jpg) 


  3. Install [ImageMagick](http://www.imagemagick.org/script/index.php) - a collection of efficient command line tools for image processing. It supports almost every common image format available these days.


  4. run the _convert_ command to create the animated gif:

```
convert -geometry 500x483 -delay 200 -loop 0 *.jpg mymovie.gif
```


The geometry is simply the WIDTHxHEIGHT dimensions of the output image (it helps if this is proportional to the original image dimensions). 

The delay parameter specifies how many hundreths of a second delay occurs between each frame. 

The loop parameter, when set to zero, indicates the gif will loop infinitely.

The \*.jpg, if your operating environment supports wildcards, will take each of the jpg images in the current directory and stich them into an animated gif named mymovie.gif





Viola! An animated movie from a series of static maps. In the case of the Paleogeologic maps, there were 41 maps which produced a sizable animated gif (about 7.5 MB). You can [check out the results here](/assets/img/geo_evolution.gif). I could watch this play for hours!! Really fascinating stuff.. many thanks to Dr. Ron Blakey for putting this project together.
 


