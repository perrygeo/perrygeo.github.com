---
date: '2008-07-15 15:01:27'
layout: post
slug: r-is-for-radiohead
status: publish
title: R is for Radiohead
wpid: '128'
---

Radiohead realeased their video for [House of Cards](http://code.google.com/creative/radiohead/) yesterday. Besides being a big radiohead fan, I was also loving the [LIDAR ](http://www.velodyne.com/lidar/)[technology ](http://www.geometricinformatics.com/)behind the video. 

If you want to check it out yourself, there are code samples on the site as well as access to the raw data. The csv files have four columns (x, y, z, and intensity). For me the quickest way to visualize the data was through R and it's OpenGL interface called rgl (which is a wonderful high-level 3D data visualization environment). 

Assuming you have R installed, rgl is a simple add on through the CRAN repositories:


    
    install.packages("rgl")



Then you need to load the library, load the csv, scale the intensity values from 0 to 1. Then it's a simple rgl.points command to get an interactive 3D rendering:

    
    
    library(rgl)
    d < - read.csv("C:/temp/radiohead/22.csv", header=FALSE)
    
    # scale intensity values from 0 to 1
    d$int <- d[,4] / 255
    
    # rgl.points(x,y,z,size=__,color=__)
    # note y value is inverted
    # color is a grayscale rgb based on intensity
    rgl.points(d[,1],d[,2]*-1,d[,3], size=3, color=rgb(d$int,d$int,d$int))
    
    



That's all it takes to render Thom Yorke in all his 3D digital glory:

![](/assets/img/radiohead2.jpg)
