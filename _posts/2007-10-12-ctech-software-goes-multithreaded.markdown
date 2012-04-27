---
date: '2007-10-12 16:20:17'
layout: post
slug: ctech-software-goes-multithreaded
status: publish
title: CTech software goes multithreaded
wpid: '86'
---

CTech has announced that the next version of it's flagship software package,  [EVS (Environmental Visualization System)](http://www.ctech.com/index.php?page=evspro), will take full advantage of multiple processors. 

![](/assets/img/evs.gif)

My experience with EVS is mostly in the realm of 3-dimensional kriging and geostatistics. Given the amount of data crunching involved, it's always been sluggish when dealing with a non-trivial amount of data. Nothing is more frustrating that seeing one of your CPU cores cranking away while the others sit idle! But [some users are reporting](http://www.ctech.com/forum/viewtopic.php?pid=213#213) that the new multithreaded modules get nearly linear performance increases when adding more processing cores.

CTech is certainly not the first scientific/geostats application to go parallel. But it is the first program that I personally use on a regular basis that will take advantage of a multi-processor system. I hope this marks the beginning of an industry trend in that direction.

