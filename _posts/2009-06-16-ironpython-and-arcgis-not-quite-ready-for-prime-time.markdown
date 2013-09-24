---
date: '2009-06-16 13:25:46'
layout: post
slug: ironpython-and-arcgis-not-quite-ready-for-prime-time
status: publish
title: IronPython and ArcGIS - not quite ready for prime time
wpid: '135'
---

Occasionally I find myself in the C#/.NET world in order to write code using ESRI ArcObjects. Today I was toying with the idea of automating the creation of ESRI Layer files (a file which defines the cartographic styling of a dataset). Of course they are in an undocumented binary file format, [inaccessible to anything but ESRI software](http://blog.cleverelephant.ca/2009/04/esri-formats-back-to-future.html). So I pop open Visual Studio .... 

I feel a nagging unease every time I type a set of curly braces. And VB just makes me insane. I prefer, of course, to use python. Luckily there is [IronPython](http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython) which runs on .NET - which means I could theoretically use it to interact with ArcGIS. 

I only found a [single working example](http://moreati.org.uk/blog/2009/01/27/from-esriarcgis-import-geodatabase/) of using ArcObjects through IronPython. But it looked promising enough to close Visual Studio and give it a go. 

The first nagging problem is an IronPython-specific one. Relatively minor annoyance but you have to add the reference to a .NET assembly (library) before you can load it. 



    
    
    import clr
    clr.AddReference('ESRI.ArcGIS.System')
    clr.AddReference('ESRI.ArcGIS.Carto')
    from ESRI.ArcGIS import esriSystem
    from ESRI.ArcGIS import Carto
    




Now there is the issue of grabbing an ESRI license. A little verbose IMO but it could easily be encapsulated in a helper function to clean things up. 




    
    
    aoc = esriSystem.AoInitializeClass()
    res = esriSystem.IAoInitialize.IsProductCodeAvailable(aoc, 
             esriSystem.esriLicenseProductCode.esriLicenseProductCodeArcView)
    if res == esriSystem.esriLicenseStatus.esriLicenseAvailable:
        esriSystem.IAoInitialize.Initialize(aoc, 
          esriSystem.esriLicenseProductCode.esriLicenseProductCodeArcView)





Now that we've satisfied the demands of our proprietary license overlords, we can proceed with the real work .. in this case I just want to open an existing Layer file and see if the resulting object knows it's own file path. Really simple, right?




    
    lyr = Carto.LayerFileClass()
    if "Open" in dir(lyr): print "The Layer object has an Open method but...."
    lyr.Open('C:\\test.lyr')
    print lyr.Filename


    
    The Layer object has an Open method but....
    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
    AttributeError: 'GenericComObject' object has no attribute 'Open'</module></stdin>


Hrm. Looks like we've run across [bug 1506](http://www.codeplex.com/IronPython/WorkItem/View.aspx?WorkItemId=1506) which doesn't allow access to the properties and methods of a given instance - instead your have to work through the functions provided by the implementation. Grr...


    
    Carto.ILayerFile.Open(lyr, 'C:\\test.lyr')
    print Carto.ILayerFile.Filename.GetValue(lyr)



That is unwieldy, ugly and [unpythonic](http://shalabh.infogami.com/Be_Pythonic2). What's the point of object oriented programming if you can't access the methods and properties of an object directly? Since all ArcObjects applications are based on extending COM interfaces, this would be a major pain in any non-trivial application. Basically, until these .NET-accessible COM objects can be treated in a pythonic way,  I don't see any compelling reason to pursue IronPython and ArcGIS integration. Looks like its back to C# for the moment ... (/me take a deep sigh and opens Visual Studio)  ... unless of course anyone has some brilliant solution to share!!






