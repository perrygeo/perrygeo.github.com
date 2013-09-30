---
layout: post
title: "Leaflet Simple CSV"
description: "Super-simple way to plot tabular data on a slippy map"
category: 
tags:
- javascript
- leaflet
---

#### Simple leaftlet-based template for mapping tabular point data on a slippy map

Anyone who's worked with spatial data and the web has run across the need to take 
some simple tabular data and put points on an interactive map. 
It's the fundamental "*Hello World*" of web mapping. Yet I always find myself spending way too much time
solving this seemingly simple problem. When you consider zoom levels, attributes,
interactivity, clustering, querying, etc... it becomes apparent that interactive maps
require a bit more legwork. But that functionality is fairly consistent case-to-case so I've developed a generalized solution that works for the majority of basic use cases out there: 

<p><a class="btn btn-primary" href="https://github.com/perrygeo/leaflet-simple-csv">leaftlet-simple-csv on github</a></p>

The idea is pretty generic but useful for most point marker maps:
* Data is in tabular delimited-text (csv, etc.) with two required columns: `lat` and `lng`
* Points are plotted on full-screen [Leaflet](https://github.com/Leaflet/Leaflet) map
* Point markers are clustered dynamically based on zoom level.
* Clicking on a point cluster will zoom into the extent of the underlying features.
* Hovering on the point will display the name. 
* Clicking will display a popup with columns/properties displayed as an html table.
* Full text filtering with typeahead
* Completely client-side javascript with all dependencies included or linked via CDN

Of course this is mostly just a packaged version of existing work, namely [Leaflet](https://github.com/Leaflet/Leaflet) with the [geoCSV](https://github.com/joker-x/Leaflet.geoCSV) and [markercluster](https://github.com/Leaflet/Leaflet.markercluster) plugins.


## Usage
 
1. Grab the [leaflet-simple-csv zip file](https://github.com/perrygeo/leaflet-simple-csv/archive/master.zip) and unzip it to a location accessible through a web server. 
2.  Copy the `config.js.template` to `config.js`
3.  Visit the [index.html](assets/leaflet-simple-csv/index.html) page to confirm everything is working with the built-in example.
4.  Customize your `config.js` for your dataset.

An example config:

    var dataUrl = 'data/data.csv';
    var maxZoom = 9;
    var fieldSeparator = '|';
    var baseUrl = 'http://otile{s}.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.jpg';
    var baseAttribution = 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>, <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/" target="_blank">CC-BY-SA</a>';
    var subdomains = '1234';
    var clusterOptions = {showCoverageOnHover: false, maxClusterRadius: 50};
    var labelColumn = "Name";
    var opacity = 1.0;

The example dataset:

    Country|Name|lat|lng|Altitude
    United States|New York City|40.7142691|-74.0059738|2.0
    United States|Los Angeles|34.0522342|-118.2436829|115.0
    United States|Chicago|41.8500330|-87.6500549|181.0
    United States|Houston|29.7632836|-95.3632736|15.0
    ...

I make no claims that this is the "right" way to do it but leveraging
100% client-side javascript libraries and native delimited-text formats seems like the simplest approach. 
Many of the features included here (clustering, filtering) are useful enough
to apply to most situations and hopefully you'll find it useful.

<hr>
<div><iframe src="/assets/leaflet-simple-csv/index.html" height="450" width="740"></iframe></div>
