---
date: '2006-06-25 15:29:13'
layout: post
slug: mapserver-include
status: publish
title: Mapserver Include
wpid: '54'
---

If you mange even a small number of Mapserver sites, eventually you notice that you use a number of identical layers in multiple mapfiles. The way this is typically done is to copy and paste the LAYER definition into each mapfile. But inevitably you'll need to change the styling or the data source and you have to manually go through each mapfile to sync the changes. Wouldn't it be nice to define the layer in a single file and use it in many mapfiles?

While Mapserver has no concept of an "include", the C preprocessor (cpp) does. This is mentioned on the Mapserver list every time the subject of includes comes up. Still I have yet to find an actual example so I thought I'd share my notes on how I accomplish a mapserver include:





  1. Create your mapfile as usual but leave out any LAYER definitions that you wish to share amongst mapfiles. Instead use something like :



> #include "landsat.layer"






  2. The C Preprocessor doesn't deal well with "#" which is the mapfile's chosen comment charachter. Instead replace with "##" to indicate a comment 



  3. Save this pseudo-mapfile as _mymap.template_



  4. Create a file in the same directory called _landsat.layer_ with the LAYER block. 



  5. Run the template through the preprocessor to generate the real mapfile :



> cpp -P -C -o mymap.map mymap.template 







The next step would be to script the preprocessing of _all_ your mapfiles so that changing a layer definition in multiple mapfiles was as simple as changing the \*.layer file and running the script. 
