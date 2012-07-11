---
layout: post
title: "Introducing the Madrona framework"
description: ""
category: 
tags:
- python
- madrona
- ecotrust
- marinemap
---

{% include JB/setup %}

### [Madrona](http://madrona.ecotrust.org): A software framework for effective place-based decision making

![Madrona](http://madrona.ecotrust.org/assets/img/madrona-logo.png)

My work at [Ecotrust](http://www.ecotrust.org/) mainly revolves around creating web-based spatial analysis tools - software to bring data-driven science to the place-based descision making process. This began several years ago when I joined the MarineMap team. Since working with Ecotrust, we've taken the MarineMap software far beyond it's original niche. What was once a specific tool for marine protected area planning has now become a powerful framework for [all sorts of web-based spatial tools](http://madrona.ecotrust.org/experience/) in the realms of marine, forestry, conservation planning, aquatic habitat restoration, etc. So, in a sense, [Madrona](http://madrona.ecotrust.org) is a recognition of that evolution. 

From the official [Madrona](http://madrona.ecotrust.org) release announcement from the [Ecotrust blog post](http://blog.ecotrust.org/software-for-21st-century-decisions-2/):

> Over the last year we’ve distilled the best ideas from our most successful tools into a suite of software building blocks that can be mixed and matched to create cutting-edge software for decision support and spatial planning at any scale. These building blocks are already at the heart of our work and now we’re ready to share them with you.

So what is [Madrona](http://madrona.ecotrust.org) from a developer's perspective? 

* A set of _python_ _django_ apps that provide models, views and templates for representing spatial features and solving problems specific to spatial decision tools.
* A RESTful _API_ for accessing spatial features
* A collection of _javascript_ libraries (based on JQuery) to provide a web-based interface to the API.
 
In short, we think its a great platform for spatial tools and we want to open it up to the wider developer audience. Ecotrust already has many [madrona-based apps](http://madrona.ecotrust.org/experience/) in the wild (with many more in development) but we're hoping to get other folks using (and contributing to) the Madrona framework in the future. 

I know this post is short on technical details but there will more to come ... for now, check out the [technology page](http://madrona.ecotrust.org/technology/) for an overview or the [developer's page](http://madrona.ecotrust.org/developer/) to dive in. 

