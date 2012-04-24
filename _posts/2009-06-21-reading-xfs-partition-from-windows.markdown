---
date: '2009-06-21 08:09:30'
layout: post
slug: reading-xfs-partition-from-windows
status: publish
title: Reading XFS partition from Windows
wpid: '137'
---

When I was setting up my linux system a few years ago, I did some research into filesystems and determined that the [XFS file system](http://en.wikipedia.org/wiki/XFS), being particularly proficient in dealing with large files, would be ideal for my home directory. And it was. But the one factor I didn't consider was portability. Turns out that there is basically no support for XFS in windows. 

So how do you access your files from Windows if they are on an XFS partition? I had just shy of 1 TB of data to transfer so using my other linux box and transferring across the network would have taken forever. The solution I came up with is a bit convoluted but it has some real advantages:

1) Install Sun's VirtualBox.
2) Download an iso for your favorite linux distribution (mine being Ubuntu 9.04)
3) Create a virtual machine from the linux iso
4) Install the VBOxGuestAdditions in the linux virtual machine. 
5) Create a Share folder on the windows host and register it with the virtual machine. This will allow you to transfer files from the guest (linux) to the host(windows) You may have to manually mount the drive in the linux guest:

 
    
    mount -t vboxsf share_name /mnt/share_name



6) Using the windows host cmd line, create a vmdk from the physical drive that your XFS partition resides on. In this case, PhysicalDrive1 corresponds to the second SATA connector. This will allow your guest OS to talk directly with the drive:


    
    cd C:\Program Files\Sun\xVM VirtualBox
    VBoxManage.exe internalcommands createrawvmdk 
      -filename "C:\Documents and Settings\perry\.VirtualBox\HardDisks\Physical1.vmdk" 
      -rawdisk \\.\PhysicalDrive1 -register



Once completed, you should see:
_
    
    
    RAW host disk access VMDK file 
    C:\Documents and Settings\perry\.VirtualBox\HardDisks\Physical1.vmdk created successfully.

_

7) Make sure to add the physical drive to your list of hard drives in the linux guest options. Restart the linux guest virtual machine and your XFS partition should already be mounted. Now you can begin transfering files between your XFS partition and the shared folder on the windows host.

Whew. Lots of hassle for a simple file transfer, right! But the side benefit is that now you have a fully functional linux virtual machine with a shared folder set up to the windows host. Very useful - even when you must run windows, it helps to have a linux VM standing by!
