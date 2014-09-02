---
layout: post
title: "Blogging with ipython notebook"
description: ""
category: 
tags:
- python
---
{% include JB/setup %}

# Introduction

## Overview

This project will explore techniques available in python for determining the
"nearest" climate based on a vector of climatic variables. This will allow us to
evaluate the projected *future* conditions and identify locations which
*currently* have a similar climate. The application of this technique could
inform proactive climate planning, particularly in forestry where e.g. it could
inform which seeds to planted today in order to hedge against climate risks.

## Data

Climate data for 1990 (the "current" condition) and projected climate surfaces
for 2030, 2060 and 2090 were obtained for the US West at a 1km cell resolution.
Data are from the [US Forest Service Climate-
FVS](http://www.fs.fed.us/fmsc/fvs/whatis/climate-fvs.shtml) program. The
variables of interest calculated for each years are

- d100 — Julian date the sum of degree-days &gt;5 degrees C reaches 100
- dd0 — Degree-days &lt;0 degrees C (based on mean monthly temperature)
- dd5 — Degree-days &gt;5 degrees C (based on mean monthly temperature)
- fday — Julian date of the first freezing date of autumn
- ffp — Length of the frost-free period (days)
- gsdd5 — Degree-days &gt;5 degrees C accumulating within the frost-free period
- gsp — Growing season precipitation, April to September
- map — Mean annual precipitation
- mat_tenths — Mean annual temperature
- mmax_tenths — Mean maximum temperature in the warmest month
- mmindd0 — Degree-days &lt;0 degrees C (based on mean minimum monthly temperature)
- mmin_tenths — Mean minimum temperature in the coldest month
- mtcm_tenths — Mean temperature in the coldest month
- mtwm_tenths — Mean temperature in the warmest month
- sday — Julian date of the last freezing date of spring
- smrpb — Summer precipitation balance: (jul+aug+sep)/(apr+may+jun)
- smrsprpb — Summer/Spring precipitation balance: (jul+aug)/(apr+may)
- sprp — Spring precipitation: (apr+may)
- smrp — Summer precipitation: (jul+aug)
- winp — Winter precipitation: (nov+dec+jan+feb)

## Software

We'll be using the `sklearn`, `pandas`, `numpy` and `matplotlib` python
libraries


# Dimensionality Reduction

## Overview
In order to avoid the "curse of dimensionality" and to avoid multicollinearity
(correlated independent variables), we can perform a Principal Component
Analysis or PCA.

$$c = \sqrt{a^2 + b^2}$$

## Code

### Load the dataset


    %pylab inline
        
    import numpy as np
    import pandas as pd
    from sklearn.decomposition import RandomizedPCA
    
    data = pd.read_csv('./data/Ensemble_rcp60_2060.csv')
    data.columns

    Populating the interactive namespace from numpy and matplotlib





    Index([u'StandID', u'Scenario', u'Year', u'mat', u'map', u'gsp', u'mtcm', u'mmin', u'mtwm', u'mmax', u'sday', u'ffp', u'dd5', u'gsdd5', u'd100', u'dd0', u'smrpb', u'smrsprpb', u'sprp', u'smrp', u'winp', u'ABAM', u'ABCO', u'ABGR', u'ABLA', u'ABLAA', u'ABMA', u'ABPR', u'ABSH', u'ACGL', u'ACGR3', u'ACMA3', u'AECA', u'ALRH2', u'ALRU2', u'ARME', u'BEPA', u'BEPAC', u'CADE27', u'CELE3', u'CHCH7', u'CHLA', u'CHNO', u'CONU4', u'FRLA', u'JUCO11', u'JUDE2', u'JUMO', u'JUOC', u'JUOS', u'JUSC2', u'LALY', u'LAOC', u'LIDE3', u'OLTE', u'PIAL', u'PIAR', u'PIAT', u'PIBR', u'PICO', u'PICO3', u'PIED', u'PIEN', u'PIFL2', u'PIJE', u'PILA', u'PILO', u'PIMO', u'PIMO3', u'PIPO', u'PIPU', u'PISI', u'PIST3', u'PODEM', u'POTR5', u'PROSO', u'PRUNU', u'PSME', u'QUAG', u'QUCH2', u'QUDO', u'QUEM', u'QUGA', u'QUGA4', u'QUHY', u'QUKE', u'QULO', u'QUOB', u'QUWI2', u'RONE', u'SALIX', u'SEGI2', u'TABR2', u'THPL', u'TSHE', u'TSME', u'UMCA', u'pSite', u'DEmtwm', u'DEmtcm', u'DEdd5', u'DEsdi', u'DEdd0', u'DEpdd5'], dtype=object)



### Scale the values from 0 to 100


    def scale_linear_bycolumn(rawpoints, high=100.0, low=0.0):
        mins = np.min(rawpoints, axis=0)
        maxs = np.max(rawpoints, axis=0)
        rng = maxs - mins
        return high - (((high - low) * (maxs - rawpoints)) / rng)
    


### Take 2D subset

Start small so we can visualize what PCA is doing.


    subdf = data[['mat','mtcm']]
    sub = scale_linear_bycolumn(np.array(subdf))
    scatter(sub[:,0], sub[:,1])





    <matplotlib.collections.PathCollection at 0x43de510>




![png](Nearest%20Climate%20Analysis_files/Nearest%20Climate%20Analysis_7_1.png)


### Run PCA

Here we see that the first derived axis explains 96% of the variance; it's
likely we could just use that 1D axis alone rather than searching in 2D space
(hence the dimensionality *reduction*).


    pca = RandomizedPCA(n_components=2)
    pca.fit(sub)
    
    print pca.explained_variance_ratio_
    print sum(pca.explained_variance_ratio_)

    [ 0.96147393  0.03852607]
    1.0



    trans_sub = pca.transform(sub)
    scatter(trans_sub[:,0], trans_sub[:,1])





    <matplotlib.collections.PathCollection at 0x65f43d0>




![png](Nearest%20Climate%20Analysis_files/Nearest%20Climate%20Analysis_10_1.png)


### Run PCA with 18 dimensional data

The benefits of PCA really become apparent when we start looking at a lot of
data.


    pca2 = RandomizedPCA(n_components=6)
    pca2.fit(sub)
    
    print list(pca2.explained_variance_)
    print list(pca2.explained_variance_ratio_)
    print sum(pca2.explained_variance_)

    [4054.9402495692266, 1597.5480043302775, 573.13375569120421, 144.91093617219519, 108.15157205121828, 52.661813374481412]
    [0.62084293864589646, 0.24459704375216448, 0.087751242489525566, 0.022186993128846019, 0.016558848140508328, 0.0080629338430592435]
    6531.34633119



    subdf = data[[u'mat', u'map', u'gsp', u'mtcm', u'mmin', 
                u'mtwm', u'mmax', u'sday', u'ffp', u'dd5', 
                u'gsdd5', u'd100', u'dd0', u'smrpb', u'smrsprpb',
                u'sprp', u'smrp', u'winp',]]
    sub = scale_linear_bycolumn(np.array(subdf))
    
    sub.shape  # many records, 18 dimensions
    





    (18278, 18)



    



    trans_sub = pca2.transform(sub)
    scatter(trans_sub[:,0], trans_sub[:,1])





    <matplotlib.collections.PathCollection at 0x65fd3d0>




![png](Nearest%20Climate%20Analysis_files/Nearest%20Climate%20Analysis_14_1.png)



    print "PCA Range    Scaled Range    Proportion of variance"
    for i in range(6):
        rang = max(trans_sub[:,i]) - min(trans_sub[:,i])
        print i, rang, rang * pca2.explained_variance_ratio_[i],  pca2.explained_variance_ratio_[i]

    PCA Range    Scaled Range    Proportion of variance
    0 248.730080573 154.422314153 0.620842938646
    1 308.070397423 75.3531084773 0.244597043752
    2 136.494352693 11.9775490417 0.0877512424895
    3 96.1595663605 2.13349163811 0.0221869931288
    4 97.8484757729 1.6202580511 0.0165588481405
    5 59.2336624824 0.477597101878 0.00806293384306



    # scale by eigenvalues
    trans_scaled_sub = trans_sub * pca2.explained_variance_ratio_
    
    #scatter(trans_sub[:,0] * pca.explained_variance_ratio_[0], trans_sub[:,1]  * pca.explained_variance_ratio_[1])
    scatter(trans_scaled_sub[:,0], trans_scaled_sub[:,1])
    
    print "AFTER SCALING BY PROPORTION OF EXPLAINED VARIANCE..."
    print "PCA Range    Proportion of variance"
    for i in range(6):
        rang = max(trans_scaled_sub[:,i]) - min(trans_scaled_sub[:,i])
        print i, rang, pca2.explained_variance_ratio_[i]

     AFTER SCALING BY PROPORTION OF EXPLAINED VARIANCE...
    PCA Range    Proportion of variance
    0 154.422314153 0.620842938646
    1 75.3531084773 0.244597043752
    2 11.9775490417 0.0877512424895
    3 2.13349163811 0.0221869931288
    4 1.6202580511 0.0165588481405
    5 0.477597101878 0.00806293384306



![png](Nearest%20Climate%20Analysis_files/Nearest%20Climate%20Analysis_16_1.png)



    # Check the coefficients of the first two component axes
    
    def print_sig_axis(comp, threshold=0.22):
        axis1_pos = [(subdf.columns[i], coef) for i, coef in enumerate(comp) if coef > threshold]
        axis1_neg = [(subdf.columns[i], coef) for i, coef in enumerate(comp) if coef < -1*threshold]
        print "\tPositive:"
        for v in sorted(axis1_pos, key=lambda x: x[1], reverse=True):
            print "\t\t", v
        print "\tNegative:"
        for v in sorted(axis1_neg, key=lambda x: x[1]):
            print "\t\t", v
        
    print "Axis0"
    print_sig_axis(pca2.components_[0])
    print "Axis1"
    print_sig_axis(pca2.components_[1])
    print "Axis2"
    print_sig_axis(pca2.components_[2])
    print "Axis3"
    print_sig_axis(pca2.components_[3])
    


    Axis0
    	Positive:
    		('mmin', 0.38366872039111527)
    		('mtcm', 0.31302089088831225)
    		('winp', 0.30695507721775839)
    		('ffp', 0.29172202573852951)
    		('map', 0.28219034705443152)
    		('sprp', 0.25063265194624024)
    		('gsdd5', 0.22620821118625326)
    	Negative:
    		('d100', -0.30606496645781284)
    		('dd0', -0.25924046411612822)
    		('sday', -0.25746251838022288)
    Axis1
    	Positive:
    		('gsp', 0.36117700288899607)
    		('sprp', 0.35210994444284671)
    		('map', 0.33017870425927082)
    		('smrp', 0.33008995294173454)
    		('winp', 0.31984175089389938)
    	Negative:
    		('mmax', -0.26036639882330709)
    		('dd5', -0.23408560103531431)
    		('mat', -0.22863400086558389)
    		('mtwm', -0.22462825647237586)
    Axis2
    	Positive:
    		('smrpb', 0.62555685305587827)
    		('smrsprpb', 0.61314322785715492)
    		('smrp', 0.26827417799554748)
    	Negative:
    Axis3
    	Positive:
    		('dd0', 0.58853081737921031)
    		('ffp', 0.39774980739485749)
    		('gsdd5', 0.30200572061030923)
    	Negative:
    		('sday', -0.39198833494532204)
    		('smrsprpb', -0.24797982682236203)
    		('mmax', -0.23262826172642612)
    		('mtcm', -0.22416379030625333)


# Find the nearest neighbor

## Overview
Now that we've reduced the dimensionality of the data and scaled our new axes
appropriately, we can search in this multi-dimensional space using a Nearest
Neighbor algorithm

## Code


    # and find the nearest neighbor
    
    # first create NN object
    from sklearn.neighbors import NearestNeighbors
    nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(trans_scaled_sub)



    
    # lets take row #3 
    test = sub[3,:]
    # then transform test data to pca axes
    trans_test = pca2.transform(test)
    # scale to eigenvalues
    trans_scaled_test = trans_test * pca2.explained_variance_ratio_
    distances, indices = nbrs.kneighbors(trans_scaled_test)
    
    # find the matching observation (should be itself!)
    print test
    print 
    print indices[0][0]  # should be row 3


    [ 59.31034483  55.97446032  50.53908356  64.36781609  67.07317073
      41.13924051  43.72294372  57.95454545  47.4916388   44.59161148
      45.76862124  30.           3.71428571  12.06896552  10.60606061
      63.53276353  29.8136646   58.4340515 ]
    
    3



    sub[:-1].shape




    (18277, 18)



# TODO

- lets find a location by lat long,
- query the rasters to construct the 18-variable search observation,
- transform to pca axes
- find the nearest neighbors
- and report back their lat/longs

