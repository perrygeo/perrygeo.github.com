---
date: '2007-09-18 21:23:51'
layout: post
slug: parallel-python-and-gis
status: publish
title: Parallel python and GIS
wpid: '82'
---

Let's face it - processing speeds aren't going to be increasing according to Moore's Law anymore; Instead of faster CPUs, [we'll be getting more of them](http://www.gotw.ca/publications/concurrency-ddj.htm). The future of programming, it seems to me, lies in the ability to leverage multiple processors. In other words, we have to write parallel code. Until I read [Seans' post](http://zcologia.com/news/571/catching-up-with-python/), I was unware that there was a viable python solution. I had been growing quite dissillusioned by python's dreaded [Global Interpreter Lock](http://www.pyzine.com/Issue001/Section_Articles/article_ThreadingGlobalInterpreter.html) which confines python to a single processing core. I've even started learning [Erlang](http://www.erlang.org/) to leverage SMP processing  (until I realized that Erlang and it's standard libraries are virtually useless for anything that needs to handle geospatial data).

So I gave [Parallel Python](http://www.parallelpython.com/) (pp) a shot. Since Sean also offered up a bounty for the first GIS application that used pp, I thought it might be a good time to try ;-)

A good candidate for parallel processing is any application that has to crunch away on lists/arrays of data and whose individual members be handled independently (see [pmap in Erlang](http://www.erlang.org/ml-archive/erlang-questions/200606/msg00130.html)). I have been working on [an application to smooth linework using bezier curves](http://perrygeo.googlecode.com/svn/trunk/gis-bin/bezier_smooth_pp.py). It's not quite polished yet but the image below shows the before and after

![](/assets/img/smoothed.jpg)

... but [bezier curves](http://en.wikipedia.org/wiki/B%C3%A9zier_curve) aren't quite the subject of this post. Let's just say the algorithm takes some time to compute (if you're using a high density of verticies) and can be handled one LineString feature at a time. This makes it a prime candidate for parallelization.

Given a list of input LineStrings, I could process them the sequential way:


    
    <blockquote>smooth_lines = []
    for line in lines:
        smooth_lines.append( calcBezierFromLine( line, num_bezpts, beztype, t) )</blockquote>



Or use pp to start up a "job server" which doles the tasks out to as many "workers". A busy worker utilizes a single processing core so a good rule of thumb would be to start up as many workers as you have CPU cores:


    
    <blockquote>numworkers = 2 # dual-core machine
    job_server = pp.Server(numworkers, ppservers=ppservers)
    smooth_lines = []
    jobs = [(line, job_server.submit(calcBezierFromLine, (line, num_bezpts, beztype, t), \
                                 (computeBezier, getPointOnCubicBezier), ("numpy",) ))  for line in lines]
    for input, job in jobs:
        smooth_lines.append( job() )</blockquote>



Theoretically the parellized version should run twice as fast as the sequential version on my core2 duo machine. And reality was pretty darn close to that:


    
    <blockquote>$ time python bezier_smooth_pp.py 2
    Shapefile contains 1114 lines
    Starting pp with 2 workers
    Completed 1114 new lines with 8 additional verticies for each line segment along a cubic bezier curve
    
    real    0m10.908s
    ...
    
    $ time python bezier_smooth_pp.py 1
    Shapefile contains 1114 lines
    Starting pp with 1 workers
    Completed 1114 new lines with 8 additional verticies for each line segment along a cubic bezier curve
    
    real    0m20.007s
    ...
    </blockquote>



Just think of the possibilities. In the forseeable future, the average computer might have 8+ cores to work with. This could mean that your app will move 8x faster if you parallize the code (assuming there are no IO or bandwidth bottlenecks). I'd love to test it out on a system with more than 2 processing cores but, unfortunately, I don't have access to any [beowulf clusters](http://www.calvin.edu/~adams/research/microwulf/), [ Sun UltraSparc servers,](http://www.sun.com/processors/UltraSPARC-T1/) or [8-core Xeon Mac Pros](http://www.apple.com/macpro/). This is what I _really need_ to complete my research ;-) So if anyone want to donate to the cause, send me an email! 

And to answer Sean's bounty, I don't consider this an actual application (yet) but I hope it can spur some interest and move things in that direction. But if you feel the need to send me some New Belgium swag (or one of the machines listed above), feel free ;-)


