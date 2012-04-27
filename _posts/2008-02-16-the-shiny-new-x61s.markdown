---
date: '2008-02-16 09:00:14'
layout: post
slug: the-shiny-new-x61s
status: publish
title: The shiny new X61s
wpid: '106'
---

My HP laptop was nearing 5 years old. It had held up extremely well but most modern software taxed it to the absolute limits (just having firefox open with a flash ad in one tab was enough to send the system load through the roof). So I decided to try something new.

I was looking for something in the ultra-portable range. I tried out the OLPC and looked seriously at the Asus eeepc for a while. But they were far too difficult for me to type on. Ergonomics were extremely important and the only ultraportable that consistently rated high in that department was the IBM/Lenovo thinkpads. The X61s was appealing with its low voltage core2 duo and 2GB of RAM. All that in a small package about 3 lbs and about an inch thick.

![](/assets/img/x61s.jpg)

So the X61s arrived and I figured I'd give it a try with the "stock" software. It was my first experience with Vista and I gave it my best shot. After about 1/2 hour of excessive clicking, boggy performance and pop-up windows, I shrunk the ntfs partition and installed Ubuntu Hardy Heron Alpha 4.  

Sound, wireless with WPA, Compiz with 3D; the major things that normally plague a linux laptop install worked right out of the box. On the other hand, I'm running into a few bugs in nautilus (this is is alpha software after all), I can't get bluetooth working, suspending to ram works but is a little buggy (have to restart some services manually) and I had to edit a few config files and compile a kernel module to utilize all the bells and whistles provided by the hardware. But it is still more fun than using Vista.

One thing that really shines on this machine is the battery. I got the 8-cell extended life battery and used some powertop tweaks cut my power consumption and was able to get the wattage down in the 10 to 15 watt range depending on usage patterns. No wonder it is energy star compliant! With that kind of wattage and battery capacity, I'm easily getting about 6 to 7 full hours of battery life.

Some tips if you're setting up Linux on your X61s:


* First and foremost, read [thinkwiki](http://thinkwiki.org). There you'll find 95% of your answers. But to summarize my experience: 



* Upgrade your BIOS first (this is a good reason to keep your Vista partion around since Lenovo ships some handy update utils for windows). 



* Install the [tp_smapi kernel module](http://www.thinkwiki.org/wiki/Tp_smapi) with HDAPS support. This will enable Linux to access the hard drive sensors for disk protection, motion sensing and the joystick interface



* The big blue "Thinkvantage" button doesn't work out of the box. I'm not sure what it _should_ do but its a nicely placed button so [don't let it go to waste](http://www.thinkwiki.org/wiki/How_to_get_special_keys_to_work#acpi_fakekey).



* Tweak the power consumption. For the impatient, just install powertop and follow the instructions .. it will tell you what processes are waking your CPU and how to stop them. Also check out [Less Watts](http://lesswatts.org) - a full resource for tweaking linux power consumption.



* Configure your [trackpoint](http://www.thinkwiki.org/wiki/How_to_configure_the_TrackPoint) pointer and buttons. This involves setting up you xorg.conf file to emulate a middle scroll wheel as well as tweaking the speed and sensitivity of the pointer. BTW - if you've never tried a pointer, give it a shot ... I've found it much more comfortable than a touchpad.



* [Laptop-mode](http://samwel.tk/laptop_mode/) , a set of kernel and userspace tools to manage hard-drive power consumption, can be handy. It can also be [deadly to your disk if configured incorrectly](https://bugs.launchpad.net/mandriva/+source/laptop-mode-tools/+bug/59695). Basically it aggressively spins down the disk after short periods of inactivity to save power. Inevitably an application will try to hit the disk again and it will spin right back up. This leads to an unreasonably high amount of load cycles (100 per hour) and the drive can only handle a finite amount before failure (~600,000).  You can configure it for more sane behavior but do your research before you enable laptop-mode! And check out smartctl to monitor the disks health. 


* If, after you unsuspend the machine, your screen is way too dark, try Ctl-Alt-F1 followed by Ctl-Alt-F7. There are some other hacks involving acpi configuration or grub kernel options but none of them have worked for me yet.
