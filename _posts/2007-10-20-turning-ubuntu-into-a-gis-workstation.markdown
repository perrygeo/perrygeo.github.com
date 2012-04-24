---
date: '2007-10-20 10:31:13'
layout: post
slug: turning-ubuntu-into-a-gis-workstation
status: publish
title: Turning Ubuntu into a GIS workstation
wpid: '10'
---

It just keeps getting easier and easier to get a fully functional open source GIS workstation up and running thanks to Ubuntu. The following instructions will take your vanilla installation of [Ubuntu 7.10](http://www.ubuntu.com/getubuntu) and add the following top-notch desktop GIS applications:





  * Postgresql/PostGIS : a relational database with vector spatial data handling 


  * GRASS : A full blown GIS analysis toolset 


  * Quantum GIS: A user-friendly graphical GIS application 


  * GDAL, Proj, Geos : Libraries and utilities for processing spatial data 


  * Mapserver : web mapping program and utilites


  * Python bindings for QGIS, mapserver and GDAL 


  * GPSBabel : for converting between various GPS formats 


  * R : a high-end statistics package with spatial capabilities 


  * GMT : the Generic Mapping Tools for automated high-quality map output 



While this is not a comprehensive list of open source GIS software, these packages cover most of my needs. If you want to live on the bleeding edge and have to have the absolute latest versions, you'll be better off installing these from source. But for those of us that want a stable and highly functional GIS workstation with minimal fuss, this is the way to go:



  1. Go to _ System > Administration > Software Sources _ and make sure the universe and multiverse repositories are turned on. Close the window and the list of available software packages will be refreshed.



  2. Open up a terminal (ie the command line) via _ Applications > Accessories > Terminal_ and type the following:



> sudo apt-get -y install qgis grass qgis-plugin-grass mapserver-bin gdal-bin cgi-mapserver \
     python-qt4 python-sip4 python-gdal python-mapscript gmt gmt-coastline-data \
     r-recommended gpsbabel shapelib libgdal1-1.4.0-grass



The _sudo_ part indicates that the command will be run as the administrator user, _ apt-get -y install_  is the command telling it to install the list of packages and answer yes to any questions that pop up. 



  3. There is one package that is worth upgrading to the latest and greatest - Quantum GIS. The latest version (0.9) is due out very shortly and has the ability to write plugins using the python programming language. A big plus! 

Download the latest build from [http://qgis.org/uploadfiles/testbuilds/qgis0.9.0.debs_ubuntu_gutsy.tar.gz](http://qgis.org/uploadfiles/testbuilds/qgis0.9.0.debs_ubuntu_gutsy.tar.gz) and extract it ( right-click > Extract Here ).  In the directory you'll see 4 .deb files, only 3 of which you'll need unless you plan on doing any development work.

Double click libqgis1_0.9.0_i386.deb and you'll get a message saying an older version is available from directly from ubuntu. We already know this so just close and ignore it.  Click _Install Package_ and wait for it to complete then close out.

Repeat for qgis_0.9.0_i386.deb and qgis-plugin-grass_0.9.0_i386.deb (in that order).




And there we have it,  about 15 minutes depending on your internet speed and you've installed a high-end GIS workstation built completely on free and open source software.
