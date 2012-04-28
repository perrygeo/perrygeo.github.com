---
date: '2009-03-25 13:38:16'
layout: post
slug: the-magic-bullet
status: publish
title: The magic bullet
wpid: '132'
- ogr
---

Dealing with corrupted shapefiles can be a painful experience: programs crash for seemingly no reason, attribute tables get screwy, features get lost, queries results don't look right and ArcGIS processing tools fail with mysterious error codes:

![Dissolve error](/assets/img/uploads/2009/03/dissolve_error.jpg)

Never fear, OGR is here. The magic bullet for fixing corrupted shapefiles is, 90% of the time, accomplished by using ogr2ogr to convert the shapefile to another shapefile. 


`

> 
ogr2ogr -f "ESRI Shapefile"  shiny_new_clean_dataset.shp corrupted_dataset.shp corrupted_dataset

`



OGR's internal data model cleans it up and the output is a fresh shiny new shapefile that works without hassle. 




