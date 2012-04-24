---
date: '2010-03-31 14:06:11'
layout: post
slug: distributed
status: publish
title: Distributed
wpid: '142'
---

I've been playing around with some distributed version control systems (DVCS) to replace svn. 

First, the _why_: I'll leave the details up to Joel in his excellent [HgInit tutorial](http://hginit.com/). Its mercurial-specific but the general concepts apply to any DVCS. The takeaway message for any project with > 1 developer is this:



> Mercurial [ed: DVCS] separates the act of committing new code from the act of inflicting it on everybody else.



Next, the _implementation_: I'm using **git** to work on another project ([Golden Cheetah](http://goldencheetah.org/)) and its been a tough learning curve. Git is no doubt the most powerful DVCS out there. You can do magical things with it like combine commits and mess with history trees. And you can also screw things up pretty badly if you misinterpret the esotric docs for some non-intuitive piece of the workflow. 

I just tried **mercurial** this morning - hg seems to fit my mind well. There is less power but the workflow is very clear and intuitive. And there are docs written for people who don't want to do an in-depth study of their version control software. It stays out of the way. 

Long story short, I'm going to use mercurial/hg for my new projects. Ah what the heck my old/ongoing projects as well. My [googlecode repository](http://code.google.com/p/perrygeo/) has been converted over to Mercurial. Svn will stick around but wont be updated.
