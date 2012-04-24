---
date: '2008-05-14 10:36:29'
layout: post
slug: ubuntu-as-a-gis-workstation-updated-for-hardy-heron
status: publish
title: Ubuntu as a GIS workstation (updated for Hardy Heron)
wpid: '119'
---

As a followup to my previous post on [turning Ubuntu Gutsy into a GIS workstation](http://www.perrygeo.net/wordpress/?p=10), Here are the revised instructions for Ubuntu 8.04 (The Hardy Heron). 

Note that there are a few additonal apps and changes in here:




  * Postgis


  * Mapnik


  * New version of QGIS installed via repository


  * OpenStreetMap tools (JOSM and osm2pgsql)


  * Geotiff utilities


  * Some nice python spatial libs (shapely, owslib, geopy and pyproj) 



Run the following as root on your new Hardy installation, answer a few configuration questions and you'll be ready to go.

    
     
    echo 'deb http://ppa.launchpad.net/qgis/ubuntu hardy main' >> /etc/apt/sources.list
    
    apt-get update
    
    apt-get -y --force-yes install grass mapserver-bin \
    gdal-bin cgi-mapserver python-qt4 python-sip4 python-gdal \
    python-mapscript gmt gmt-coastline-data r-recommended gpsbabel \
    shapelib qgis qgis-plugin-grass python-setuptools \
    python-mapnik mapnik-plugins mapnik-utils osm2pgsql josm postgresql-8.3-postgis \
    python-dev build-essential libgdal-dev geotiff-bin sun-java6-jre
    
    easy_install shapely geopy owslib pyproj
    



EDIT: If you're looking for more up to date packages for geos, gdal, etc, try adding ` deb http://les-ejk.cz/ubuntu/ hardy multiverse ` to your /etc/apt/sources.list 
