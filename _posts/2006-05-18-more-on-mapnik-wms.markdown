---
date: '2006-05-18 15:38:49'
layout: post
slug: more-on-mapnik-wms
status: publish
title: More on Mapnik WMS
wpid: '50'
---

One of my initial complaints about the Mapnik WMS server was that it would not accept any parameters that were not in the OGC WMS spec. Some WMS clients will tag on extra parameters for various reasons and the OGC supports this in relation to vendor-specific parameters. The fix was pretty simple;in **mapnik/ogcserver/common.py** you can simply comment out         



> 

        #for paramname in params.keys():
        #    if paramname not in self.SERVICE_PARAMS[requestname].keys():
        #        raise OGCException('Unknown request parameter "%s".' % paramname)




to get the desired effect.



* * *



There was also the question of speed and how it compared to other WMS servers such as Mapserver. Since I already had both a Mapnik and Mapserver WMS set up using the exact same data source, styled in the same fashion, it was pretty simple to write a quick python script that would smack each WMS server with a given number of back-to-back WMS GetMap requests:




> 

>     
>     
>     #!/usr/bin/env python
>     import urllib
>     
>     server = sys.argv[1]
>     hits = int(sys.argv[2])
>     
>     if server == 'mapnik':
>         url = "http://localhost/fcgi-bin/wms?VERSION=1.1.1&REQUEST;=GetMap&SERVICE;=WMS&LAYERS;=world_borders&SRS;=EPSG:4326&BBOX;=-4.313249999999993,20.803500000000003,59.58675000000002,52.75350000000002&WIDTH;=800&HEIGHT;=400&FORMAT;=image/png&STYLES;=&TRANSPARENT;=TRUE&UNIQUEID;="
>     elif server == 'mapserver':
>         url = "http://localhost/cgi-bin/mapserv?map=/home/perrygeo/mapfiles/world.map&VERSION;=1.1.1&REQUEST;=GetMap&SERVICE;=WMS&LAYERS;=worldborders&SRS;=EPSG:4326&BBOX;=-4.313249999999993,20.803500000000003,59.58675000000002,52.75350000000002&WIDTH;=800&HEIGHT;=400&FORMAT;=image/png&STYLES;=&TRANSPARENT;=TRUE&UNIQUEID;="
>         
>     for i in range(0,hits):
>         urllib.urlretrieve(url)
>     



Then just run the script from the command line, specifying the server and number of hits, and wrap it in the _time_ command. Here are the results:

![](/img/manik_vs_mapserv_speed.png)

Pretty close. Mapserver was just slightly faster in every case. Now this is just a preliminary test and it would be interested to see a comparison:





  * With larger datasets and more complex styling including classification and text labelling


  * With data from other sources such as postgis where the connection overhead might be significant


  * With Mapserver running as a fastcgi 


  * With concurrent requests as opposed to back-to-back requests 



Overall though, my opinion of Mapnik WMS remains high and I'd love to put it in production use in the near future. Stay tuned...
