---
date: '2007-09-04 00:19:42'
layout: post
slug: performance-testing-rasters-with-mapserver
status: publish
title: Performance testing rasters with mapserver
wpid: '76'
---

There's been some good talk on the mapserver list (thanks to Gregor's diligent testing) about performance related to serving up raster imagery. 

First off, comparisons of [image](http://lists.umn.edu/cgi-bin/wa?A2=ind0709&L=mapserver-users&T=0&O=D&P=1526) [formats. ](http://lists.umn.edu/cgi-bin/wa?A2=ind0709&L=mapserver-users&T=0&O=D&P=1526)Then a look at some TIFF [optimization](http://lists.umn.edu/cgi-bin/wa?A2=ind0709&L=mapserver-users&T=0&O=D&P=2214) [techniques](http://lists.umn.edu/cgi-bin/wa?A2=ind0709&L=mapserver-users&T=0&O=D&P=4492) like overviews (similar to "pyramids" in ESRI land) and internal tiling to boost rendering speed. 

Most of the conclusions are not all that staggering: 




  * TIFF is fastest but takes up more space compared to ECW and JPEG2000. 


  * Overviews speed up TIFFs tremendously when zoomed out (ie when mapserver would otherwise have to perform some heavy downsampling) 


  * Internal tiles in GeoTIFF format give a boost when zoomed in (only the necessary tiles are read from disk) 


  * The TIFF comparison was run on two setups; a monsterous 8-core, RAID-5 equipped beast and a low-memory virtual machine on low-end PC hardware. The TIFF optimizations are very noticeable on the lesser machine but almost completely negligible on the high-end machine. 

> Both tiling and overviews are useful, but only on machines with resource 
shortages, such as slow disks or a lack of spare RAM for caching.





Nothing earth-shattering (these techniques are often mentioned as best practices) but is very nice to see some hard numbers to back it up.  Plus the verbose test logs provide a good example for a newbie trying to implement them. Good stuff Gregor!



