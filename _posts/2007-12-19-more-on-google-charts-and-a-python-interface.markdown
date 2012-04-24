---
date: '2007-12-19 22:39:29'
layout: post
slug: more-on-google-charts-and-a-python-interface
status: publish
title: More on Google Charts and a python interface
wpid: '99'
---

Well it's been almost a full two weeks since [google charts API](http://code.google.com/apis/chart/) came out.  A really nice service but it's only going to be useful with a high-level programming API. Enter [PyGoogleChart](http://pygooglechart.slowchop.com/) .. a python interface to generate google chart urls. 

Taking one of my [previous example datasets](http://www.perrygeo.net/wordpress/?p=64), here's the 10-second howto:

    
    <blockquote>from pygooglechart import SimpleLineChart
    chart = SimpleLineChart(400,200)
    data = [32.5,35.2,39.9,40.8,43.9,48.2,50.5,51.9,53.1,55.9,60.7,64.4]
    chart.add_data(data)
    url = chart.get_url()
    print url
    </blockquote>



which gives us:



> http://chart.apis.google.com/chart?cht=lc&chs;=400x200&chd;=t:32.5,35.2,39.9,40.8,43.9,48.2,50.5,51.9,53.1,55.9,60.7,64.4



and our chart image:

![](http://chart.apis.google.com/chart?cht=lc&chs=400x200&chd=t:32.5,35.2,39.9,40.8,43.9,48.2,50.5,51.9,53.1,55.9,60.7,64.4)

