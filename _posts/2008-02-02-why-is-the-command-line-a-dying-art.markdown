---
date: '2008-02-02 20:50:19'
layout: post
slug: why-is-the-command-line-a-dying-art
status: publish
title: Why is the command line a dying art?
wpid: '105'
---

Sadly, a lot of GIS folks have never come into contact with a command line interface (CLI) . I've met even experienced computer users who, when faced with a command-line prompt, experience some autonomous nervous system lock up that causes their eyes to glaze over and prevents any knowledge from entering their brain from that moment forward. The all-Windows, all-GUI mentality of the current GIS market leaders just doesn't expose you to it (if you remember working with coverages at the ESRI Arc/Info command line, you official qualify as an "old-timer"). And the DOS command line is virtually invisible to XP and vista users. Linux users are more CLI aware but this is even becoming less important as distros such as ubuntu GUI-ify everything.

So why the fear of the command line? Why is it assumed to be more "complicated" than a graphical user interface (GUI)? I have found that, in some cases, the opposite is true ... there is something reassuringly simple about typing something and getting a response back. It feels like you are in direct control of the computer. Which, indeed, you _always_ are. The computers always do exactly what you tell them, whether you are in a GUI or a CLI. But GUIs attempt to abstract away the details so that you _don't need to know_ exactly what you're telling the computer to do. This nice fluffy feeling comes at the cost of many important factors. 

## The benefits of the command line interface

### Automation
If you had, for instance, monitoring data coming in in a hourly basis and needed to process the data, would you want to be on call 24 hours a day to click a few buttons. Of course not. Write a command that performs the job and schedule it to execute at some regular interval. (I wonder if those guys on LOST ever thought to just set up a cron job to enter the numbers in the hatch?)  





### Repeatability 
Whenever I show someone a CLI-based method for solving their problem, they almost immediately say (or at least imply) that the typing is too much trouble.  Consider this command to convert a .tif image to ERDAS .img (HFA) format:

    
    cd /data/images
    gdal_translate -of HFA aerial.tif aerial.tif.img


You might ask, "Why not just use a GUI, click a button or two, and get your output".  Sure. Now do that for 2,000 tif images. With a CLI you only have to type a few extra lines. 

    
    cd /data/images
    for i in *.tif; do 
      gdal_translate -of HFA $i $i.img;
    done






### Documentability
There is nothing more important to a GIS Analyst than documenting his/her work! We live by metadata and methods write-ups.   Now picture an intense 5 hour work session ... everything needed to get out by 2pm. You're done and now it's time to document your procedure and methods. With the CLI, you copy and paste your commands from the terminal or simply look at your command history which will show _exactly_ what you did and how. You can store this in a text file and come back to it months later and be able to re-run the procedure. 

With the GUI, you have to remember and describe every click, every sub-menu, every option, every action taken to arrive at the answer. Often this requires verbose description, screenshots, etc. None of which is recorded in any history file of course. And of course, when the client inevitably comes back the next day with modifications, none of it is repeatable in any automated fashion with a GUI. 





### Accessibility
It's just plain text with a CLI. You can print it out and study it on the bus. You can email the whole process to co-workers. You can use a concurrent versioning system to keep track of changes to scripted procedures. You can transfer massive amounts of knowledge without having to sit down and go through everything step-by-step, click-by-click in a visual interface. 





### Accuracy
Far too often, GUI designers make over-reaching assumptions about how things should work. The idea is often that the user should not need to know anything more than the absolute minumum.  To use a car analogy, the driver turns the key, presses the pedal and steers but does not need to know what goes on under the hood.  This works most of the time. But the [law of leaky abstractions](http://en.wikipedia.org/wiki/Leaky_abstraction) usually takes hold and something inevitably breaks or performs differently than expected.  Since the CLI does not hold your hand (it executes the exact command you give it) it more accurately mimics the actual physical interaction with the computer and is much more useful in debugging and investigating complex problems. 






So basically, don't make the mistake of thinking that a pretty window will always contain the magic button to get the job done. In many cases, a command line is much more efficient, even essential. If you don't know how to effectively work in a command-line environment, do yourself a huge favor and learn.

Oh and I'd be remiss if I didn't mention [Neal Stephenson's book ](http://www.amazon.com/Beginning-was-Command-Line-Neal-Stephenson/dp/0380815931) on the subject ... a bit technically outdated but a great quick read on why command lines are still very relevant in the face of increasingly sophisticated graphical interfaces.
