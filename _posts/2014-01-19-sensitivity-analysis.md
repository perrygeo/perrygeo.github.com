---
layout: post
title: "Sensitivity analysis made (relatively) simple"
description: "Use SALib python module to sample and test the sensitivity of models"
category: 
tags:
- statistics
- forestry
---


### Best bang for your analytical buck

As (geo)data scientists, we spend much of our time working with data models that try (with varying degrees of success) to capture some essential truth about the world while still being as simple as possible to provide a useful abstraction. Inevitably, complexity starts to creep into every model and we don't often stop to assess the value added by that complexity. When working with models that require a large number of parameters and a huge domain of potential inputs that are expensive to collect, it becomes difficult to answer the question:

**What parameters of the model are the most sensitive?**

In other words, if I am going to spend my resources obtaining/refining data for this model, where should I focus
my efforts in order to get the best bang for the buck? If I spend weeks working on deriving a single parameter for the model,
I want some assurance that the parameter is critically important to the model's prediction. 
The flip-side, of course, is that if a parameter is *not* that important to the model's predictive power, I could
save some time by perhaps just using some quick-and-dirty approximation. 

### SALib: a python module for testing model sensitivity

I was thrilled to find [SALib](http://jdherman.github.io/SALib/) which implements a number of vetted methods for quantitatively 
assessing parameter sensitivity. There are three basic steps to running SALib:

1. Define the parameters to test, define their domain of possible values and generate *n* sets of randomized input parameters.   
2. Run the model *n* times and capture the results.
3. Analyze the results to identify the most/least sensitive parameters.

I'll leave the details of these steps to the [SALib documentation](http://jdherman.github.io/SALib/).
The beauty of the SALib approach is that you have the flexibility[1] to run any model in any way you want, so long as you can manipulate the inputs and outputs adequately.

### Case Study: Climate effects on forestry

I wanted to compare a forest growth and yield model under different climate change scenarios in order to assess what the most sensitive climate-related variables were. I identified 4 variables:

* Climate model (4 global circulation models)
* Representative Concentration Pathways (RCPs; 3 different emission trajectories)
* Mortality factor for species viability (0 to 1)
* Mortality factor for equivalent elevation change (0 to 1)

In this case, I was using the [Forest Vegetation Simulator](http://www.fs.fed.us/fmsc/fvs/)(FVS) which requires
a configuration file for every model iteration. So, for Step 2, I had to iterate through each set of input variables and use them to generate an appropriate configuration file. This involved translating the real numbers from the samples into categorical variables in some cases. Finally, in order to get the result of the model iteration, I had to parse the outputs of FVS and do some post-processing to obtain the variable of interest (the average volume of standing timber over 100 years). So the flexibility of SALib comes at a slight cost: unless your model works directly with the file formatted for SALib, the input and outputs may require some data manipulation.  

After running the all required iterations of the model[2] I was able to analyze the results and assess the sensitivity of the four parameters. 

Here's the output of SALib's analysis (formatted slightly for readability):

    Parameter    First_Order First_Order_Conf Total_Order Total_Order_Conf
    circulation  0.193685    0.041254         0.477032    0.034803
    rcp          0.517451    0.047054         0.783094    0.049091
    mortviab    -0.007791    0.006993         0.013050    0.007081
    mortelev    -0.005971    0.005510         0.007162    0.006693


The *first order effects* represent the effect of that parameter alone. The *total order effects* are arguably more
relevant to understanding the overall interaction of that parameter with your model. The "Conf" columns represent confidence and can be interpreted as error bars.

In this case, we interpret the output as follows:

    Parameter    Total Order Effect   
    circulation  0.47  +- 0.03  (moderate influence)      
    rcp          0.78  +- 0.05  (dominant parameter)
    mortviab     0.01  +- 0.007 (weak influence)
    mortelev     0.007 +- 0.006 (weak influence)

We can graph each of the input parameters against the results to visualize this:

![sagraph](/assets/img/sagraph.png)

Note that the 'mortelev' component is basically flat (as the factor increases, the result stays the same) whereas the choice of 'rcp' has a heavy influence (as emissions increase to the highest level, the resulting prediction for timber volumes are noticeably decreased).

The conclusion is that the climate variables, particularly the RCPs related to human-caused emissions, were the strongest determinants[1] of tree growth *for this particular forest stand*. This ran counter to our initial intuition that the mortality factors would play a large role in the model. Based on this sensitivity analysis, we may be able to avoid wasting effort on refining parameters that are of minor consequence to the output.


<hr>
Footnotes:

1. Compared to more tightly integrated, model-specific methods of sensitivity analysis
2. 20 thousand iterations took approximately 8 hours; sensitivity analysis generally requires lots of processing
3. Note that the influence of a parameter says nothing about direct *causality*
