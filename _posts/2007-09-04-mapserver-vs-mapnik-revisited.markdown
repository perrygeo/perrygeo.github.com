---
date: '2007-09-04 20:12:02'
layout: post
slug: mapserver-vs-mapnik-revisited
status: publish
title: Mapserver vs Mapnik revisited
wpid: '77'
---

A while ago, I was enamored with mapnik's image quality despite it's limitations compared to the vast configurability of the mapserver mapfile. Now that mapserver uses the AGG rendering library,  it might not be necessary to compromise configurability in order to get beautiful linework. I just installed the recent beta of mapserver 5.0 and the image quality is very crisp... but this comes at the expense of rendering speed.

All the times below are the average of ten runs using a full global view of a simplified shapefile of country borders. 








![](/assets/img/mapserver_gd_test.jpg)



**mapserver (gd) : 0.082 sec , 18kb**


> OUTPUTFORMAT
  NAME "GD_JPEG"
  DRIVER "GD/JPEG"
  MIMETYPE "image/jpeg"
  IMAGEMODE RGB
  EXTENSION "jpg"
END


shp2img -m test.map -o mapserver_gd_test.jpg








![](/assets/img/mapserver_agg_test.jpg)



**mapserver (agg) : 0.188 sec , 16kb**


> 
IMAGEQUALITY 80 
OUTPUTFORMAT
  NAME 'AGG_JPEG'
  DRIVER AGG/JPEG
  IMAGEMODE RGB
END


* Note that if we bump up imagequality to 90% to (roughly) match the mapnik image, the rendering time and size increase a bit (.201 sec, 25kb)

shp2img -m test.map -o mapserver_agg_test.jpg









![](/assets/img/mapnik_output.jpg)



**mapnik (agg) : 0.282 sec, 23kb**
python test_mapnik.py

* Running this through the python interpreter is likely to interfere with the speed of the results so these times may not be very comparable to shp2img.





Using these preliminary results, it looks like mapserver 5.0 with AGG rendering is roughly equal to mapnik based on a balance of quality/speed/image size. But since I'd prefer to use mapfiles over the undocumented mapnik xml format any day, I think I'll stick with my beloved mapserver. Kudos to the mapserver developers for raising the bar once again.
