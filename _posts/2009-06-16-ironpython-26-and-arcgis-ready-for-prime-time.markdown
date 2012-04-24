---
date: '2009-06-16 14:43:08'
layout: post
slug: ironpython-26-and-arcgis-ready-for-prime-time
status: publish
title: IronPython (2.6) and ArcGIS - ready for prime time!!
wpid: '136'
---

Not sure why this didn't occur to me _before_ I wrote [that last post](http://www.perrygeo.net/wordpress/?p=135) but I tried the "pythonic" version of the code under the [IronPython 2.6 Beta 1](http://ironpython.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=25126) release and it works!


    
    lyr = Carto.LayerFileClass()
    lyr.Open('C:\\test.lyr')
    print lyr.Filename
    



Works perfectly now. So IronPython **2.6** promises to be a viable option for extending ArcGIS. My enthusiasm has been renewed.


