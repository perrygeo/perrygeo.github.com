---
date: '2006-05-17 23:37:30'
layout: post
slug: mapnik-wms-server
status: publish
title: Mapnik WMS Server
wpid: '49'
---

A few months ago, [ Mapnik](http://mapnik.org/) came onto my radar and I was immediately impressed with the [beautiful](http://mapnik.org/maps/) [cartography](http://static.flickr.com/35/106561736_afcdc30ddb_o.png). But, until recently, it was just a C++ libary with some python bindings that could be used to programmatically build nice map images from shapfiles, geotiffs or postgis layers. There were no common interfaces such as WMS to access mapnik... until last month. Jean Francois Doyon recently added [a prototype WMS interface](http://mapnik.org/news/2006/apr/18/wms/) to Mapnik. It runs as a fastcgi script under apache. It is still a bit rough around the edges but the result is well worth a little extra setup effort. 

I set up Mapnik as a WMS server recently and would like to share my process and results. This tutorial assumes you already have python, postgresql/postgis, proj4, python imaging library and apache2 already running. The examples are for Ubuntu Dapper Drake.. they may work well on other versions of Ubuntu and Debian but for other unixes (and certainly windows) many things may need to be tweaked.

First off, we have to install the base mapnik libs. These depend on the boost python bindings and the whole compile process is very simple (if a bit slow) in Ubuntu:



> 
>     sudo apt-get install \
>      libboost-python1.33.1 libboost-python-dev \
>      libboost-regex1.33.1 libboost-regex-dev \
>      libboost-serialization-dev \
>      libboost-signals1.33.1 libboost-signals-dev \
>      libboost-thread1.33.1 libboost-thread-dev \
>      libboost-program-options1.33.1 libboost-program-options-dev \
>      libboost-filesystem1.33.1 libboost-filesystem-dev \
>      libboost-iostreams1.33.1 libboost-iostreams-dev
>     cd ~/src
>     svn checkout svn://svn.berlios.de/mapnik/trunk mapnik
>     cd mapnik
>     python scons/scons.py PYTHON=/usr/bin/python PGSQL_INCLUDES=/usr/local/include/postgresql \
>       PGSQL_LIBS=/usr/local/lib/postgresql BOOST_INCLUDES=/usr/include/boost BOOST_LIBS=/usr/lib
>     sudo python scons/scons.py install PYTHON=/usr/bin/python PGSQL_INCLUDES=/usr/local/include/postgresql \
>       PGSQL_LIBS=/usr/local/lib/postgresql BOOST_INCLUDES=/usr/include/boost BOOST_LIBS=/usr/lib
>     sudo ldconfig




Now we have to set up some additional libs in order to run the WMS:



> 

>     
>     
>     cd ~/src
>     wget http://easynews.dl.sourceforge.net/sourceforge/jonpy/jonpy-0.06.tar.gz
>     tar -xzvf jonpy-0.06.tar.gz
>     cd jonpy-0.06/
>     sudo python setup.py install
>     
>     
> 
> 






> 

>     
>     
>     # copy the ogcserver stuff into its own dir
>     mkdir /opt/mapnik; cd /opt/mapnik
>     cp ~/src/mapnik/utils/ogcserver/* .
>     
>     
> 
> 




Now you'll want to edit the **ogcserver.conf** file and change the following lines. The _module_ is essentially the name of a python file (minus the .py extension) that we'll create later. The height and width just cutoff the maximum possible image size that can be requested.


> 

>     
>     
>     	module=worldMapFactory
>     	maxheight=2048
>     	maxwidth=2048
>     
> 
> 





Create our "map factory" module defining data sources, styles, etc.( **worldMapFactory.py** ). Most of this configuration is explained in the mapnik docs and well-commented examples. One thing to note is that the shapefile must be specified _without_ the .shp extension :



> 

>     
>     
>     from mapnik.ogcserver.WMS import BaseWMSFactory
>     from mapnik import *
>     
>     class WMSFactory(BaseWMSFactory):
>     
>             def __init__(self):
>                     BaseWMSFactory.__init__(self)
>                     sty = Style()
>     
>     		rl = Rule()
>     		rl.symbols.append(PolygonSymbolizer(Color(248,216,136)))
>     		rl.symbols.append(LineSymbolizer(Color(0,0,0),1))
>                     sty.rules.append( rl )
>     
>     		self.register_style('style1', sty)
>     
>                     lyr = Layer(name='world_borders', type='shape', \
>                                 file='/opt/data/world_borders/world_borders')
>     			
>                     lyr.styles.append('style1')
>                     self.register_layer(lyr)
>                     self.finalize() 
>     




Now we need to set up apache2 to handle fastcgi:




> 

>     
>     
>     sudo apt-get install libapache2-mod-fcgid
>     sudo a2enmod fcgid
>     
> 
> 





... and add some config lines to the apache config files, usually /etc/apache/httpd.conf but, in the case of this Ubuntu install, **/etc/apache2/sites-enabled/default** :



> 

>     
>     
>     
>             ScriptAlias /fcgi-bin/ /usr/lib/fcgi-bin/
>             < Directory "/usr/lib/fcgi-bin" >
>                     AllowOverride All
>                     Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
>                     Order allow,deny
>                     Allow from all
>                     SetHandler fastcgi-script
>             < Directory>
>     
>     
> 
> 





Create the fast-cgi directory refered to by apache



> 

>     
>     
>     sudo mkdir /usr/lib/fcgi-bin
>     
> 
> 





Now create the actual server script as **/usr/lib/fcgi-bin/wms**




> 

>     
>     
>     #!/usr/bin/env python
>     
>     # Your mapnik dir containing the map factory 
>     # must be in the python path!
>     
>     import sys
>     sys.path.append('/opt/mapnik')
>     
>     from mapnik.ogcserver.cgiserver import Handler
>     import jon.fcgi as fcgi
>     
>     class WMSHandler(Handler):
>         configpath = '/opt/mapnik/ogcserver.conf'
>     
>     fcgi.Server({fcgi.FCGI_RESPONDER: WMSHandler}).run()
>     
> 
> 




Finally restart the apache server 


> 

>     
>     
>     sudo /etc/init.d/apache2 force-reload
>     
> 
> 



Now you can access it with a WMS request like so:



> 

>     
>     
>     http://localhost/fcgi-bin/wms?VERSION=1.1.1&REQUEST;=GetMap&LAYERS;=world_borders&
>     FORMAT=image/png&SRS;=EPSG:4326&STYLES;=&BBOX;=-81.54375,-58.3125,-59.04375,-47.0625&
>     EXCEPTIONS=application/vnd.ogc.se_inimage&width;=600&height;=300
>     
> 
> 




![](/assets/img/mapnik.png)

Compare the linework with a comparable WMS service with UMN Mapserver on the backend. I'll let the results speak for themselves...

![](/assets/img/mapserv.png)

Even if it's map rendering is smooth, Mapnik's WMS server is still a bit rough around the edges:



	
  * It does not support GetFeatureInfo requests

	
  * The server has trouble with extra parameters. For instance some WMS clients like mapbuilder like to 
tag on an extra 'UNIQUEID' parameter to the URL and this causes an unnecessary error with mapnik's WMS server.

	
  * Mapnik intself does not support reprojection 

        
  * It only supports shapefiles, geotiffs and postgis layers.


The readme.txt file in docs/ogcserver/ directory of the recent mapnik SVN checkout has a full list of known features and caveats so refer to them for the complete story.

But, all in all, I am _very_ impressed with the quality of the Mapnik WMS server. I figured that, since Mapnik's goal has been high-quality cartographic output, speed would be sacrificed but I didn't notice any significant lag; on the contrary I think it was actually about on-par with Mapserver running as a CGI. If it was any slower, I didn' t notice it immediately. But then again it was only working with a relatively small shapefile and I was the only user. I'd like to do more rigourous stress tests on the Mapnik WMS to see how it compares to Mapserver and Geoserver under varying loads with greater volumes of data.




