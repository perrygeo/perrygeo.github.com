---
date: '2006-04-23 12:23:21'
layout: post
slug: the-distinction-between-open-source-and-open-standards
status: publish
title: The distinction between open source and open standards
wpid: '42'
---

Time and time again I see _open source_ and _open standards_ mentioned in the [same](http://veryspatial.com/?p=802) [sentence](http://www.ced.org/projects/ecom.shtml#open). While I'm a strong proponet of both, it is a bit disheartening to see how closely intertwined the two concepts are in the eyes of many GIS folks. 

Open source refers to _software_ distributed with a license that allows access to view and modify the source code. There are also some [other criteria](http://www.opensource.org/index.php) but unrestricted access to the source code is the key component. 

Open standards refers to _software-neutral_ specifications, usually developed collaboratively,  to accomplish a technical goal. In the GIS world, this typically means [OpenGIS specifications](http://www.opengeospatial.org/specs/?page=specs) for sharing data across a network (WMS/ WFS/ WCS), data formats (GML), or for working with spatial data in a relational database (Simple Features Spec for SQL).  We could arguably include pseudo-open specifications for data such as [shapfiles](http://www.esri.com/library/whitepapers/pdfs/shapefile.pdf) and [KML](http://earth.google.com/kml/kml_intro.html).

Open source applications do not always conform to open standards. Standards-compliant software does not necessarily have to be open source. So why are the two often mentioned in the same breath as though they were synonymous? Perhaps open source software is perceived as being "ahead" of other types of software in terms of adoption of standards; and maybe that's true. But there are many proprietary software companies that have devoted alot of effort towards making their software communicate via open standards and their efforts should not go unnoticed ([ESRI](http://www.esri.com/software/standards/ogc-support.html) and [Cadcorp](http://www.cadcorp.com/) just to name the two I'm familiar with). 

 The promise of open standards is that anyone can develop and use compliant applications that can easily interoperate regardless of the chosen software package. While that promise is far from being fully realized, associating open standards with a particular type of software will not get us any closer.  

**Update**: Or maybe we _are_ getting close... check out [Geoff Ziess' post](http://geospatial.blogs.com/geospatial/2006/04/interoperabilit.html) on the OGC interoperability demonstration in Tampa. Ten vendors interoperating and sharing data in real time... this is what it's all about.
