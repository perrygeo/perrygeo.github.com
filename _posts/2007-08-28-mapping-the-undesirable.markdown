---
date: '2007-08-28 22:35:21'
layout: post
slug: mapping-the-undesirable
status: publish
title: Mapping the Undesirable
wpid: '75'
---

While by no means a new phenomenon, [ Vision 20/20](http://www.thevision2020.com/LocateSexOffenders.aspx) is offering a service allowing you to see a map of the registered sex offenders in your area. WorldChanging, one of my favorite blogs on emerging technologies, has a great article discussing the issues surrounding [ mapping of sex offenders ](http://www.worldchanging.com/archives/007189.html).  



> Is this sort of service, based on powerful networked technologies -- and one being sold on the basis of fear -- an appropriate use of the technology? Where is the data being sourced from? How are the people inputting it being supervised? And what rights to privacy and presumptions of innocence are the people it tracks entitled to? 



These are good points, but even more disturbing to me as a citizen and a GIS professional, is that these maps use geocoding services that are [ not nearly accurate enough](http://www.ij-healthgeographics.com/content/2/1/10/abstract/) for the scale at which they are being viewed. Even in suburban areas, using linear-referenced geocoding techniques can still yield errors of 100s of meters! The margin of error in the geocoding engine alone is enough to place the sex offender icon directly on an innocent citizens' home.

For instance, which of the homes in the map below is the residence of a sex offender? Does the ambiguity bother you? Would it matter more if _you_ were the innocent person living next door?

![](/img/offender.png)

For maps with this much social weight, I think that a bit more diligence is due to ensure that this data is as accurate as it needs to be! 



