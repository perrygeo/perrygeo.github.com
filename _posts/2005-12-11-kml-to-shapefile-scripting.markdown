---
date: '2005-12-11 22:26:56'
layout: post
slug: kml-to-shapefile-scripting
status: publish
title: KML to Shapefile Scripting
wpid: '3'
---

Christian Spanring has been doing some great work with Google Earth's KML data format. The latest offering is a fairly robust [XSLT stylesheet for transforming KML into GML](http://spanring.name/blog/2005/12/11/kml2gml/). 

In the article, he mentions ogr2ogr as a method to convert GML to shapefiles so I immediately had to try it out! I came up with a simple bash script, **kml2shp.sh**, that provides a quick command-line interface:



> kml2shp.sh input.kml output.shp



Here's the step-by-step:





  1. Make sure you have xsltproc (the command-line xslt processor) and OGR installed.



  2. Copy the [xslt stylesheet ](http://spanring.name/blog/wp-content/files/kml2gml.xsl) to /usr/local/share/kml2gml/



  3. Create the kml2shp.sh script below (make sure to change the paths to reflect your system, chmod +x it, etc)







> #!/bin/bash

if [ $# -ne 2 ]; then
  echo "usage: kml2shp.sh input.kml output.shp"
  exit
fi

echo "Processing KML file"
sed 's/ xmlns=\"http\:\/\/earth.google.com\/kml\/2.0\"//' $1 > /tmp/temp.kml
xsltproc -o /tmp/temp.gml /usr/local/share/kml2gml/kml2gml.xsl /tmp/temp.kml

echo "Creating new Shapefile"
ogr2ogr $2 /tmp/temp.gml myFeature

echo "Cleaning up temp files"
rm /tmp/temp.gml
rm /tmp/temp.kml

echo "New shapefile has been created:"
echo $2




Now as far as I can tell, the XSLT is fairly robust although I've only tested it on a few datasets. The wrapper script, however, could use alot of work. Type and error checking would be nice for starters and a better method to remove the xml namespace might be necessary. This is really meant as a starting point.

 One potential problem with this technique is that you will most likely get a 3D shapefile (x, y AND z coordinates). Many applications can handle 3D shapefiles but some (QGIS, others?) cannot at the present time. Once the geometry type is known, one could always specify the ogr2ogr "-nlt" parameter to force 2D output. But that's all for now... let me know if anyone has any suggestions on improving this technique.
