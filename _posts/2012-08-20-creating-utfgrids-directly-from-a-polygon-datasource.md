---
layout: post
title: "Creating UTFGrids directly from a polygon datasource"
description: "Simple command line script to create UTFGrid json files from a polygon shapefile."
category: 
tags:
- python
- utfgrid
- mapnik
---

We've begun to rely on the interactivity provided by [UTFGrids](http://mapbox.com/mbtiles-spec/utfgrid/) in many of our recent web maps. (Quick recap: UTFGrids are "invisible" map tiles that allow direct interactivity with feature attributes without querying the server.) Earlier this year, I created the [initial OpenLayers UTFGrid support](/2012/02/24/utfgrids-with-openlayers-and-tilestache/) and was glad to see it accepted into OpenLayer 2.12 (with some enhancements). 

With the client-side javascript support in place, the only missing piece in the workflow was to create the UTFGrid .json files. 
We had expirimented with several alternate [UTFGrid renderers](https://github.com/springmeyer/utfgrid-example-writers) but Mapnik's rendering was by far the fastest and produced the best results. 
Using Tilemill was a convenient way to leverage the Mapnik UTFGrid renderer but it came at the cost of a somewhat circuitious and manual workflow: 

1. Load the data up into [Tilemill](http://mapbox.com/tilemill/),
1. Configure interactivity fields
1. Export to .mbtiles
1. [Convert to .json files](http://blog.perrygeo.net/2012/03/25/working-with-mbtiles-in-python/)

What we really needed was a **script to take a polygon shapefile and render the UTFGrids directly to files**. [Mapnik](http://mapnik.org) would provide the rendering while the [Global Map Tiles](http://www.maptiler.org/google-maps-coordinates-tile-bounds-projection/globalmaptiles.py) python module would provide the logic for going back and forth between geographic coordinates and tile grid coordinates. From there it's just a matter of determining the extent of the data set and, for a specified set of zoom levels, looping through and using Mapnik to render the UTFGrid to a .json file in `Z/X/Y.json` directory structure.  

<p><a href="https://github.com/Ecotrust/create-utfgrids" class="btn btn-primary">Get `create-utfgrids` on github</a></p>

If we have a mercator polygon shapefile of ecoregions and want to render UTFGrids for zoom levels 3 through 5 using the `dom_desc` and `div_desc` attributes, we could use a command like

    $ ./create_utfgrids.py test_data/bailey_merc.shp 3 5 ecoregions -f dom_desc,div_desc

    WARNING:
    This script assumes a polygon shapefile in spherical mercator projection.
    If any of these assumptions are not true, don't count on the results!
     * Processing Zoom Level 3
     * Processing Zoom Level 4
     * Processing Zoom Level 5

and inspect the output (e.g. zoom level 5, X=20, Y=18)

    $ cat ecoregions/5/20/18.json | python -mjson.tool
    {
        "data": {
            "192": {
                "div_desc": "RAINFOREST REGIME MOUNTAINS", 
                "dom_desc": "HUMID TROPICAL DOMAIN"
            }, 
    ...
        "grid": [
            "  !!!!!!!!!#####$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%", 
    ...


Some caveats:

* This currently only works for polygon datasets in a Web Mercator projection.
* It's only tested with shapefiles as it assumes a single-layer datasource at the moment. Full OGR Datasource support would not be too difficult to add for PostGIS, etc.
* It assumes a top-origin tile scheme (as do OSM and Google Maps). Supporting TMS bottom-origin schemes in the future should be straightforward. 
* Requires OGR and Mapnik >= 2.0 with python bindings. Finding windows binaries for the required version of Mapnik may be difficult so using OSX/Linux is recommended at this time. 

Many thanks to Dane Springmeyer for his help on UTFGrid related matters and 
and to  Klokan Petr Přidal for his [MapTiler docs](http://www.maptiler.org/google-maps-coordinates-tile-bounds-projection/)

