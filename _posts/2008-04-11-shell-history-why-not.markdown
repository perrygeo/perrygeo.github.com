---
date: '2008-04-11 12:29:08'
layout: post
slug: shell-history-why-not
status: publish
title: Shell history - Why not?
wpid: '112'
tags:
- unix
---

What an odd meme .. I don't know why but I expected some more interesting results. I guess the majority of the commands I use are pretty pedestrian.

    
    
    history|awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}'|sort -rn|head
    163 vi
    48 screen
    29 python
    28 ls
    17 cp
    17 cd
    9 sqlite3
    6 rm
    5 sudo
    4 htop
    



