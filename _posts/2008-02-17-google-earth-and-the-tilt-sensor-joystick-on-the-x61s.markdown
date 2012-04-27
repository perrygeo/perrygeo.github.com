---
date: '2008-02-17 11:13:34'
layout: post
slug: google-earth-and-the-tilt-sensor-joystick-on-the-x61s
status: publish
title: Google Earth and the tilt sensor joystick on the X61s
wpid: '107'
---

The X61s is one bad-ass machine. Besides the great performance, battery life and solid engineering, there are other hidden gems. Like the tilt sensors that were designed to protect the hard drive in case of a drop can also be used to detect the laptops motion under more normal circumstances. 

There are [some](http://www-128.ibm.com/developerworks/linux/library/l-knockage.html) [interesting](http://www.pberndt.com/Programme/Linux/pyhdaps/index.html#) [applications](http://blog.micampe.it/articles/2006/06/04/here-comes-the-smackpad) that use some simple statistics to determine when the machine is "tapped" or julted to left or right. You can then assign actions to unique combinations of taps.

These applications all use the sysfs interface to the sensors (_ cat /sys/bus/platform/devices/hdaps/position _ will show your position in the x and y axis). But the sensors also provide a joystick interface that allow you to tilt the laptop along the two horizontal axes to control any number of applications. Including Google Earth.







  1. Install [tp_smapi](http://www.thinkwiki.org/wiki/Tp_smapi)


  2. Test the sensors by running hdaps-gl , a simple OpenGL app showing the real-time tilt of your thinkpad.


  3. Run jscal to calibrate the joystick. You'll need to install the "joystick" package for this. The command is:
`jscal -c /dev/input/js0`
After which you should keep your laptop level for a few seconds. Then, when prompted, tilt left, center, right, back (towards you), center, then forward.
 


  4. Now fire up Google Earth. Open the Options menu, go to Navigation and select Enable Contoller. 

![](/assets/img/GE_joystick.jpg)

  5. You should now be able to zoom around by tilting the laptop.  The keyboard shortcuts really help when you're in this mode (Ctl-Up/Down to zoom, Shift-Up/Down to tilt, Shift-Left/Right to pivot). 



There's also a neat [Perl-script technique to control a web-based google map](http://www.metafilter.com/52312/More-accellerometer-goodness) which has some cool potential for an openlayers based system. 

Since most Apple laptops have a similar sensor, you should be able to get the same thing going on your Macbook.  Try it out..its alot more fun that using the mouse!
