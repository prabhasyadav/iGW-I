#!/usr/bin/env python
# coding: utf-8

# # Uniform Flow and Well*
# 
# The worksheet addresses the superposition of uniform and radial steady-state groundwater flow <br>
# in a homogeneous, confined aquifer of uniform thickness without recharge. <br>
# The radial flow component may represent an extraction or injection well. <br>
# 
# The worksheet calculates hydraulic head isolines (red), streamlines (blue / black), and isochrones (green) <br>
# by using an analytical solution. The set of streamlines includes the dividing streamline (black). <br>
# In addition, the capture width of the well (dashed lines) and the position of the stagnation point are determined. <br>
# Three travel time values representing isochrones can be selected by the user. <br>
# 
# input parameters		    |   units	|   remarks
# :---------------------------|:----------|:--------------------------------------
# hydraulic conductivity		|   m/s	    |   enter positive number
# effective porosity		    |   -	    |   enter number between 0 and 1
# thickness		            |   mm/a	|   enter positive number
# uniform velocity		    |   m/d	    |   enter number different from zero$*$
# pumping rate		        |   m³/d	|   enter number different from zero$**$
# travel time		            |   d	    |   enter positive number
# 
# 
# $*$ Positive or negative numbers correspond to uniform flow in parallel with or antiparallel to the x-axis, resp. <br>
# $**$ Positive or negative numbers correspond to water extraction or injection, resp.
# 
# 
# **_Contributed by Ms. Anne Pförtner and Sophie Pförtner. The original concept from Prof. R. Liedl spreasheet code._**

# In[1]:


import numpy as np
from ipywidgets import *
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

#definition of the function 
def uniform_flow(K, ne, m, v, Q, t1, t2, t3):

    #intermediate results 
    K_1 = K*86400                       #hydraulic conductivity [m/d]
    capture_width = Q/m/v               #capture width [m]
    L_ref = Q/(2*np.pi*np.exp(1)*m*v)   #[m]
    h_ref = v/K_1*L_ref                 #[m]
    t_ref = 0.5*ne*Q/np.pi/m/v**2       #[d]
    stagnation_x = np.exp(1)*L_ref      #stagnation point (x) [m]
    stagnation_y = 0                    #stagnation point (y) [m]

    #isolines; Syntax: isolines_[X or Y]_plot_[h_ref]_[optional: 1 or 2]
    isolines_x_plot_n5_1=[] 
    isolines_y_plot_n5_1=[]
    isolines_x_plot_n5_2 = []
    isolines_y_plot_n5_2 = []
    isolines_x_plot_n2_5_1 = []
    isolines_y_plot_n2_5_1 = []
    isolines_x_plot_n2_5_2 = []
    isolines_y_plot_n2_5_2 = []
    isolines_x_plot_0_1 = []
    isolines_y_plot_0_1 = []
    isolines_x_plot_0_2 = []
    isolines_y_plot_0_2 = []
    isolines_x_plot_2_5 = []
    isolines_y_plot_2_5 = []
    isolines_x_plot_5 = []
    isolines_y_plot_5 = []
    isolines_x_plot_7_5 = []
    isolines_y_plot_7_5 = []
    isolines_x_plot_10 = []
    isolines_y_plot_10 = []
    isolines_x_plot_12_5 = []
    isolines_y_plot_12_5 = []
    isolines_x_plot_15 = []
    isolines_y_plot_15 = []
    
    
    for x in range(0, 100):
        isolines_x_n5_1=L_ref*((x*0.169103048517306+(100-x)*-0.150360933444141)/100)
        isolines_x_n5_2=L_ref*((x*12.35+(100-x)*11.6815653622516)/100)
        isolines_x_n2_5_1=L_ref*((x*0.474722923528955+(100-x)*-0.350418198256065)/100)
        isolines_x_n2_5_2=L_ref*((x*9.45+(100-x)*8.22933315122817)/100)
        isolines_x_0_1=L_ref*((x*np.exp(1)+(100-x)*-0.75695357132717)/100)
        isolines_x_0_2=L_ref*((x*6.65+(100-x)*np.exp(1))/100)
        isolines_x_2_5=L_ref*((x*4+(100-x)*-1.46395392968976)/100)
        isolines_x_5=L_ref*((x*1.5+(100-x)*-2.50444142220744)/100)
        isolines_x_7_5=L_ref*((x*-0.875+(100-x)*-3.84154019983304)/100)
        isolines_x_10=L_ref*((x*-3.15+(100-x)*-5.4105773228373)/100)
        isolines_x_12_5=L_ref*((x*-5.4+(100-x)*-7.15205676143326)/100)
        isolines_x_15=L_ref*((x*-7.65+(100-x)*-9.02099613666581)/100)
        
        if x == 0:
            isolines_y_n5_1 = 0
            isolines_y_n5_2 = 0
            isolines_y_n2_5_1 = 0
            isolines_y_n2_5_2 = 0
            isolines_y_0_1 = 0
            isolines_y_0_2 = 0
            isolines_y_2_5 = 0
            isolines_y_5 = 0
            isolines_y_7_5 = 0
            isolines_y_10 = 0
            isolines_y_12_5 = 0
            isolines_y_15 = 0
            
        else:
            isolines_y_n5_1 = np.sqrt((L_ref*np.exp(-5/np.exp(1)+isolines_x_n5_1/L_ref/np.exp(1)))**2-isolines_x_n5_1**2)
            isolines_y_n5_2 = np.sqrt((L_ref*np.exp(-5/np.exp(1)+isolines_x_n5_2/L_ref/np.exp(1)))**2-isolines_x_n5_2**2)
            isolines_y_n2_5_1 = np.sqrt((L_ref*np.exp(-2.5/np.exp(1)+isolines_x_n2_5_1/L_ref/np.exp(1)))**2-isolines_x_n2_5_1**2)
            isolines_y_n2_5_2 = np.sqrt((L_ref*np.exp(-2.5/np.exp(1)+isolines_x_n2_5_2/L_ref/np.exp(1)))**2-isolines_x_n2_5_2**2)
            isolines_y_0_1 = np.sqrt((L_ref*np.exp(0/np.exp(1)+isolines_x_0_1/L_ref/np.exp(1)))**2-isolines_x_0_1**2)
            isolines_y_0_2 = np.sqrt((L_ref*np.exp(0/np.exp(1)+isolines_x_0_2/L_ref/np.exp(1)))**2-isolines_x_0_2**2)
            isolines_y_2_5 = np.sqrt((L_ref*np.exp(2.5/np.exp(1)+isolines_x_2_5/L_ref/np.exp(1)))**2-isolines_x_2_5**2)
            isolines_y_5 = np.sqrt((L_ref*np.exp(5/np.exp(1)+isolines_x_5/L_ref/np.exp(1)))**2-isolines_x_5**2)
            isolines_y_7_5 = np.sqrt((L_ref*np.exp(7.5/np.exp(1)+isolines_x_7_5/L_ref/np.exp(1)))**2-isolines_x_7_5**2)
            isolines_y_10 = np.sqrt((L_ref*np.exp(10/np.exp(1)+isolines_x_10/L_ref/np.exp(1)))**2-isolines_x_10**2)
            isolines_y_12_5 = np.sqrt((L_ref*np.exp(12.5/np.exp(1)+isolines_x_12_5/L_ref/np.exp(1)))**2-isolines_x_12_5**2)
            isolines_y_15 = np.sqrt((L_ref*np.exp(15/np.exp(1)+isolines_x_15/L_ref/np.exp(1)))**2-isolines_x_15**2)
        
        isolines_x_plot_n5_1.append(isolines_x_n5_1)
        isolines_y_plot_n5_1.append(isolines_y_n5_1)
        isolines_x_plot_n5_2.append(isolines_x_n5_2)
        isolines_y_plot_n5_2.append(isolines_y_n5_2)
        isolines_x_plot_n2_5_1.append(isolines_x_n2_5_1)
        isolines_y_plot_n2_5_1.append(isolines_y_n2_5_1)
        isolines_x_plot_n2_5_2.append(isolines_x_n2_5_2)
        isolines_y_plot_n2_5_2.append(isolines_y_n2_5_2)
        isolines_x_plot_0_1.append(isolines_x_0_1)
        isolines_y_plot_0_1.append(isolines_y_0_1)
        isolines_x_plot_0_2.append(isolines_x_0_2)
        isolines_y_plot_0_2.append(isolines_y_0_2)
        isolines_x_plot_2_5.append(isolines_x_2_5)
        isolines_y_plot_2_5.append(isolines_y_2_5)
        isolines_x_plot_5.append(isolines_x_5)
        isolines_y_plot_5.append(isolines_y_5)
        isolines_x_plot_7_5.append(isolines_x_7_5)
        isolines_y_plot_7_5.append(isolines_y_7_5)
        isolines_x_plot_10.append(isolines_x_10)
        isolines_y_plot_10.append(isolines_y_10)
        isolines_x_plot_12_5.append(isolines_x_12_5)
        isolines_y_plot_12_5.append(isolines_y_12_5)
        isolines_x_plot_15.append(isolines_x_15)
        isolines_y_plot_15.append(isolines_y_15)
    
    #streamlines; synthax: streamlines_[X or Y]_plot_[psi]
    streamlines_x_plot_0 = [0, (L_ref*-10)]
    streamlines_y_plot_0 = [0, 0]
    streamlines_x_plot_0_2 = []
    streamlines_y_plot_0_2 = []
    streamlines_x_plot_0_4 = []
    streamlines_y_plot_0_4 = []
    streamlines_x_plot_0_6 = []
    streamlines_y_plot_0_6 = []
    streamlines_x_plot_0_8 = []
    streamlines_y_plot_0_8 = []
    streamlines_x_plot_1 = []
    streamlines_y_plot_1 = []
    streamlines_x_plot_1_2 = []
    streamlines_y_plot_1_2 = []
    streamlines_x_plot_1_4 = []
    streamlines_y_plot_1_4 = []
    streamlines_x_plot_1_6 = []
    streamlines_y_plot_1_6 = []
    
    for x in range(0,100):
        streamlines_y_0_2 = L_ref*((x*0+(100-x)*1.34462005667342)/100)
        streamlines_y_0_4 = L_ref*((x*0+(100-x)*2.6992421745751)/100)
        streamlines_y_0_6 = L_ref*((x*0+(100-x)*4.07255559164565)/100)
        streamlines_y_0_8 = L_ref*((x*0+(100-x)*5.47097889806004)/100)
        streamlines_y_1 = L_ref*((x*0+(100-x)*6.89826117541355)/100)
        streamlines_y_1_2 = L_ref*((x*2.13413758353342+(100-x)*8.35561532789609)/100)
        streamlines_y_1_4 = L_ref*((x*4.24381382643103+(100-x)*9.8422946888304)/100)
        streamlines_y_1_6 = L_ref*((x*6.31283612436048+(100-x)*11.3562442221618)/100)

        streamlines_x_0_2 = streamlines_y_0_2/np.tan(streamlines_y_0_2/L_ref/np.exp(1)-np.pi*0.2)
        streamlines_x_0_4 = streamlines_y_0_4/np.tan(streamlines_y_0_4/L_ref/np.exp(1)-np.pi*0.4)
        streamlines_x_0_6 = streamlines_y_0_6/np.tan(streamlines_y_0_6/L_ref/np.exp(1)-np.pi*0.6)
        streamlines_x_0_8 = streamlines_y_0_8/np.tan(streamlines_y_0_8/L_ref/np.exp(1)-np.pi*0.8)
        streamlines_x_1 = streamlines_y_1/np.tan(streamlines_y_1/L_ref/np.exp(1)-np.pi*1)
        streamlines_x_1_2 = streamlines_y_1_2/np.tan(streamlines_y_1_2/L_ref/np.exp(1)-np.pi*1.2)
        streamlines_x_1_4 = streamlines_y_1_4/np.tan(streamlines_y_1_4/L_ref/np.exp(1)-np.pi*1.4)
        streamlines_x_1_6 = streamlines_y_1_6/np.tan(streamlines_y_1_6/L_ref/np.exp(1)-np.pi*1.6)
        
        streamlines_x_plot_0_2.append(streamlines_x_0_2)
        streamlines_y_plot_0_2.append(streamlines_y_0_2)
        streamlines_x_plot_0_4.append(streamlines_x_0_4)
        streamlines_y_plot_0_4.append(streamlines_y_0_4)
        streamlines_x_plot_0_6.append(streamlines_x_0_6)
        streamlines_y_plot_0_6.append(streamlines_y_0_6)
        streamlines_x_plot_0_8.append(streamlines_x_0_8)
        streamlines_y_plot_0_8.append(streamlines_y_0_8)
        streamlines_x_plot_1.append(streamlines_x_1)
        streamlines_y_plot_1.append(streamlines_y_1)
        streamlines_x_plot_1_2.append(streamlines_x_1_2)
        streamlines_y_plot_1_2.append(streamlines_y_1_2)
        streamlines_x_plot_1_4.append(streamlines_x_1_4)
        streamlines_y_plot_1_4.append(streamlines_y_1_4)
        streamlines_x_plot_1_6.append(streamlines_x_1_6)
        streamlines_y_plot_1_6.append(streamlines_y_1_6)

    #isochrones
    isochrones_x_plot_t1 = []
    isochrones_y_plot_t1 = []
    isochrones_x_plot_t2 = []
    isochrones_y_plot_t2 = []
    isochrones_x_plot_t3 = []
    isochrones_y_plot_t3 = []
    
    #iterate 5 times with start value t_xmin1/ t_xmax1
    
    t1_xmin1=-np.exp(1)*np.sqrt(np.exp(2*(t1/t_ref))-1)
    t1_xmin6= t1_xmin1+(np.exp(1)-t1_xmin1)*(1+np.exp(1)/t1_xmin1*(np.log(1-t1_xmin1/np.exp(1))+(t1/t_ref)))
    t1_xmax1= np.exp(1)*np.sqrt(1-np.exp(-2*(t1/t_ref)))
    t1_xmax6= t1_xmax1+(np.exp(1)-t1_xmax1)*(1+np.exp(1)/t1_xmax1*(np.log(1-t1_xmax1/np.exp(1))+(t1/t_ref)))
    t2_xmin1=-np.exp(1)*np.sqrt(np.exp(2*(t2/t_ref))-1)
    t2_xmin6= t2_xmin1+(np.exp(1)-t2_xmin1)*(1+np.exp(1)/t2_xmin1*(np.log(1-t2_xmin1/np.exp(1))+(t2/t_ref)))
    t2_xmax1=np.exp(1)*np.sqrt(1-np.exp(-2*(t2/t_ref)))
    t2_xmax6= t2_xmax1+(np.exp(1)-t2_xmax1)*(1+np.exp(1)/t2_xmax1*(np.log(1-t2_xmax1/np.exp(1))+(t2/t_ref)))
    t3_xmin1=-np.exp(1)*np.sqrt(np.exp(2*(t3/t_ref))-1)
    t3_xmin6= t3_xmin1+(np.exp(1)-t3_xmin1)*(1+np.exp(1)/t3_xmin1*(np.log(1-t3_xmin1/np.exp(1))+(t3/t_ref)))
    t3_xmax1=np.exp(1)*np.sqrt(1-np.exp(-2*(t3/t_ref)))
    t3_xmax6= t3_xmax1+(np.exp(1)-t3_xmax1)*(1+np.exp(1)/t3_xmax1*(np.log(1-t3_xmax1/np.exp(1))+(t3/t_ref)))
    for i in range(4):     
        t1_xmin6= t1_xmin6+(np.exp(1)-t1_xmin6)*(1+np.exp(1)/t1_xmin6*(np.log(1-t1_xmin6/np.exp(1))+(t1/t_ref)))
        t1_xmax6= t1_xmax6+(np.exp(1)-t1_xmax6)*(1+np.exp(1)/t1_xmax6*(np.log(1-t1_xmax6/np.exp(1))+(t1/t_ref)))
        t2_xmin6= t2_xmin6+(np.exp(1)-t2_xmin6)*(1+np.exp(1)/t2_xmin6*(np.log(1-t2_xmin6/np.exp(1))+(t2/t_ref)))
        t2_xmax6= t2_xmax6+(np.exp(1)-t2_xmax6)*(1+np.exp(1)/t2_xmax6*(np.log(1-t2_xmax6/np.exp(1))+(t2/t_ref)))
        t3_xmin6= t3_xmin6+(np.exp(1)-t3_xmin6)*(1+np.exp(1)/t3_xmin6*(np.log(1-t3_xmin6/np.exp(1))+(t3/t_ref)))
        t3_xmax6= t3_xmax6+(np.exp(1)-t3_xmax6)*(1+np.exp(1)/t3_xmax6*(np.log(1-t3_xmax6/np.exp(1))+(t3/t_ref)))

    for x in range (0,100):
    
        isochrones_x_t1 = 0.5*L_ref*(t1_xmin6+t1_xmax6+(t1_xmax6-t1_xmin6)*np.cos(np.pi*(100-x)/100))
        isochrones_x_t2 = 0.5*L_ref*(t2_xmin6+t2_xmax6+(t2_xmax6-t2_xmin6)*np.cos(np.pi*(100-x)/100))
        isochrones_x_t3 = 0.5*L_ref*(t3_xmin6+t3_xmax6+(t3_xmax6-t3_xmin6)*np.cos(np.pi*(100-x)/100))

        if x == 0:
            isochrones_y_t1 = 0
            isochrones_y_t2 = 0
            isochrones_y_t3 = 0
        else:
        
            isochrones_y1_t1 = L_ref*np.exp(1)*np.arccos((0.5*isochrones_x_t1/np.exp(1)/L_ref+np.exp(-(t1/t_ref)-isochrones_x_t1/np.exp(1)/L_ref))/(1-0.5*isochrones_x_t1/np.exp(1)/L_ref))
            isochrones_y_t1 = L_ref*np.exp(1)*np.arccos((isochrones_x_t1/L_ref*(np.sin(isochrones_y1_t1/np.exp(1)/L_ref)/(isochrones_y1_t1/L_ref)-0.5*np.cos(isochrones_y1_t1/np.exp(1)/L_ref)/np.exp(1))+np.exp(-(t1/t_ref)-isochrones_x_t1/np.exp(1)/L_ref))/(1-0.5*isochrones_x_t1/np.exp(1)/L_ref))

            isochrones_y1_t2 = L_ref*np.exp(1)*np.arccos((0.5*isochrones_x_t2/np.exp(1)/L_ref+np.exp(-(t2/t_ref)-isochrones_x_t2/np.exp(1)/L_ref))/(1-0.5*isochrones_x_t2/np.exp(1)/L_ref))
            isochrones_y_t2 = L_ref*np.exp(1)*np.arccos((isochrones_x_t2/L_ref*(np.sin(isochrones_y1_t2/np.exp(1)/L_ref)/(isochrones_y1_t2/L_ref)-0.5*np.cos(isochrones_y1_t2/np.exp(1)/L_ref)/np.exp(1))+np.exp(-(t2/t_ref)-isochrones_x_t2/np.exp(1)/L_ref))/(1-0.5*isochrones_x_t2/np.exp(1)/L_ref))

            isochrones_y1_t3 = L_ref*np.exp(1)*np.arccos((0.5*isochrones_x_t3/np.exp(1)/L_ref+np.exp(-(t3/t_ref)-isochrones_x_t3/np.exp(1)/L_ref))/(1-0.5*isochrones_x_t3/np.exp(1)/L_ref))
            isochrones_y_t3 = L_ref*np.exp(1)*np.arccos((isochrones_x_t3/L_ref*(np.sin(isochrones_y1_t3/np.exp(1)/L_ref)/(isochrones_y_t3/L_ref)-0.5*np.cos(isochrones_y1_t3/np.exp(1)/L_ref)/np.exp(1))+np.exp(-(t3/t_ref)-isochrones_x_t3/np.exp(1)/L_ref))/(1-0.5*isochrones_x_t3/np.exp(1)/L_ref))

            for i in range(4):
                isochrones_y_t1 = L_ref*np.exp(1)*np.arccos((isochrones_x_t1/L_ref*(np.sin(isochrones_y_t1/np.exp(1)/L_ref)/(isochrones_y_t1/L_ref)-0.5*np.cos(isochrones_y_t1/np.exp(1)/L_ref)/np.exp(1))+np.exp(-(t1/t_ref)-isochrones_x_t1/np.exp(1)/L_ref))/(1-0.5*isochrones_x_t1/np.exp(1)/L_ref))
            
                isochrones_y_t2 = L_ref*np.exp(1)*np.arccos((isochrones_x_t2/L_ref*(np.sin(isochrones_y_t2/np.exp(1)/L_ref)/(isochrones_y_t2/L_ref)-0.5*np.cos(isochrones_y_t2/np.exp(1)/L_ref)/np.exp(1))+np.exp(-(t2/t_ref)-isochrones_x_t2/np.exp(1)/L_ref))/(1-0.5*isochrones_x_t2/np.exp(1)/L_ref))

                isochrones_y_t3 = L_ref*np.exp(1)*np.arccos((isochrones_x_t3/L_ref*(np.sin(isochrones_y_t3/np.exp(1)/L_ref)/(isochrones_y_t3/L_ref)-0.5*np.cos(isochrones_y_t3/np.exp(1)/L_ref)/np.exp(1))+np.exp(-(t3/t_ref)-isochrones_x_t3/np.exp(1)/L_ref))/(1-0.5*isochrones_x_t3/np.exp(1)/L_ref))

    
        isochrones_x_plot_t1.append(isochrones_x_t1)
        isochrones_y_plot_t1.append(isochrones_y_t1)
        isochrones_x_plot_t2.append(isochrones_x_t2)
        isochrones_y_plot_t2.append(isochrones_y_t2)
        isochrones_x_plot_t3.append(isochrones_x_t3)
        isochrones_y_plot_t3.append(isochrones_y_t3)

    #still necessary: mirror on x-axis 
    isolines_y_plot_n5_1_mirror = -1*(np.asarray(isolines_y_plot_n5_1))
    isolines_y_plot_n5_2_mirror = -1*(np.asarray(isolines_y_plot_n5_2))
    isolines_y_plot_n2_5_1_mirror = -1*(np.asarray(isolines_y_plot_n2_5_1))
    isolines_y_plot_n2_5_2_mirror = -1*(np.asarray(isolines_y_plot_n2_5_2))
    isolines_y_plot_0_1_mirror = -1*(np.asarray(isolines_y_plot_0_1))
    isolines_y_plot_0_2_mirror = -1*(np.asarray(isolines_y_plot_0_2))
    isolines_y_plot_2_5_mirror = -1*(np.asarray(isolines_y_plot_2_5))
    isolines_y_plot_5_mirror = -1*(np.asarray(isolines_y_plot_5))
    isolines_y_plot_7_5_mirror = -1*(np.asarray(isolines_y_plot_7_5))
    isolines_y_plot_10_mirror = -1*(np.asarray(isolines_y_plot_10))
    isolines_y_plot_12_5_mirror = -1*(np.asarray(isolines_y_plot_12_5))
    isolines_y_plot_15_mirror = -1*(np.asarray(isolines_y_plot_15))
    
    streamlines_y_plot_0_2_mirror = -1*(np.asarray(streamlines_y_plot_0_2))
    streamlines_y_plot_0_4_mirror = -1*(np.asarray(streamlines_y_plot_0_4))
    streamlines_y_plot_0_6_mirror = -1*(np.asarray(streamlines_y_plot_0_6))
    streamlines_y_plot_0_8_mirror = -1*(np.asarray(streamlines_y_plot_0_8))
    streamlines_y_plot_1_mirror = -1*(np.asarray(streamlines_y_plot_1))
    streamlines_y_plot_1_2_mirror = -1*(np.asarray(streamlines_y_plot_1_2))
    streamlines_y_plot_1_4_mirror = -1*(np.asarray(streamlines_y_plot_1_4))
    streamlines_y_plot_1_6_mirror = -1*(np.asarray(streamlines_y_plot_1_6))

    
    isochrones_y_plot_t1_mirror = -1*(np.asarray(isochrones_y_plot_t1))
    isochrones_y_plot_t2_mirror = -1*(np.asarray(isochrones_y_plot_t2))
    isochrones_y_plot_t3_mirror = -1*(np.asarray(isochrones_y_plot_t3))
    

    fig, (ax1, ax2) = plt.subplots(2, figsize=(10, 10))

    #plotten incl. mirror on x-axis

    ax1.plot(isolines_x_plot_n5_1, isolines_y_plot_n5_1, 'r')
    ax1.plot(isolines_x_plot_n5_2, isolines_y_plot_n5_2, 'r')
    ax1.plot(isolines_x_plot_n2_5_1, isolines_y_plot_n2_5_1, 'r')
    ax1.plot(isolines_x_plot_n2_5_2, isolines_y_plot_n2_5_2, 'r')
    ax1.plot(isolines_x_plot_0_1, isolines_y_plot_0_1, 'r')
    ax1.plot(isolines_x_plot_0_2, isolines_y_plot_0_2, 'r')
    ax1.plot(isolines_x_plot_2_5, isolines_y_plot_2_5, 'r')
    ax1.plot(isolines_x_plot_5, isolines_y_plot_5, 'r')
    ax1.plot(isolines_x_plot_7_5, isolines_y_plot_7_5, 'r')
    ax1.plot(isolines_x_plot_10, isolines_y_plot_10, 'r')
    ax1.plot(isolines_x_plot_12_5, isolines_y_plot_12_5, 'r')
    ax1.plot(isolines_x_plot_15, isolines_y_plot_15, 'r')

    ax1.plot(isolines_x_plot_n5_1, isolines_y_plot_n5_1_mirror, 'r')
    ax1.plot(isolines_x_plot_n5_2, isolines_y_plot_n5_2_mirror, 'r')
    ax1.plot(isolines_x_plot_n2_5_1, isolines_y_plot_n2_5_1_mirror, 'r')
    ax1.plot(isolines_x_plot_n2_5_2, isolines_y_plot_n2_5_2_mirror, 'r')
    ax1.plot(isolines_x_plot_0_1, isolines_y_plot_0_1_mirror, 'r')
    ax1.plot(isolines_x_plot_0_2, isolines_y_plot_0_2_mirror, 'r')
    ax1.plot(isolines_x_plot_2_5, isolines_y_plot_2_5_mirror, 'r')
    ax1.plot(isolines_x_plot_5, isolines_y_plot_5_mirror, 'r')
    ax1.plot(isolines_x_plot_7_5, isolines_y_plot_7_5_mirror, 'r')
    ax1.plot(isolines_x_plot_10, isolines_y_plot_10_mirror, 'r')
    ax1.plot(isolines_x_plot_12_5, isolines_y_plot_12_5_mirror, 'r')
    ax1.plot(isolines_x_plot_15, isolines_y_plot_15_mirror, 'r')

    ax1.plot(streamlines_x_plot_0,streamlines_y_plot_0, 'b')
    ax1.plot(streamlines_x_plot_0_2,streamlines_y_plot_0_2, 'b')
    ax1.plot(streamlines_x_plot_0_4,streamlines_y_plot_0_4, 'b')
    ax1.plot(streamlines_x_plot_0_6,streamlines_y_plot_0_6, 'b')
    ax1.plot(streamlines_x_plot_0_8,streamlines_y_plot_0_8, 'b')
    ax1.plot(streamlines_x_plot_1,streamlines_y_plot_1, color = 'black')
    ax1.plot(streamlines_x_plot_1_2,streamlines_y_plot_1_2, 'b')
    ax1.plot(streamlines_x_plot_1_4,streamlines_y_plot_1_4, 'b')
    ax1.plot(streamlines_x_plot_1_6,streamlines_y_plot_1_6, 'b')

    
    ax1.plot(streamlines_x_plot_0_2,streamlines_y_plot_0_2_mirror, 'b')
    ax1.plot(streamlines_x_plot_0_4,streamlines_y_plot_0_4_mirror, 'b')
    ax1.plot(streamlines_x_plot_0_6,streamlines_y_plot_0_6_mirror, 'b')
    ax1.plot(streamlines_x_plot_0_8,streamlines_y_plot_0_8_mirror, 'b')
    ax1.plot(streamlines_x_plot_1,streamlines_y_plot_1_mirror, color = 'black')
    ax1.plot(streamlines_x_plot_1_2,streamlines_y_plot_1_2_mirror, 'b')
    ax1.plot(streamlines_x_plot_1_4,streamlines_y_plot_1_4_mirror, 'b')
    ax1.plot(streamlines_x_plot_1_6,streamlines_y_plot_1_6_mirror, 'b')


    ax1.set(xlabel='x [m]', ylabel ='y [m]', xlim = [-175, 225], ylim = [-175,175])
    fig.savefig("isolines.png", dpi=300)

    ax2.plot(isochrones_x_plot_t1, isochrones_y_plot_t1, 'g')
    ax2.plot(isochrones_x_plot_t2, isochrones_y_plot_t2, 'g')
    ax2.plot(isochrones_x_plot_t3, isochrones_y_plot_t3, 'g')

    ax2.plot(isochrones_x_plot_t1, isochrones_y_plot_t1_mirror, 'g')
    ax2.plot(isochrones_x_plot_t2, isochrones_y_plot_t2_mirror, 'g')
    ax2.plot(isochrones_x_plot_t3, isochrones_y_plot_t3_mirror, 'g')
    
    ax2.plot(streamlines_x_plot_0,streamlines_y_plot_0, 'b')
    ax2.plot(streamlines_x_plot_0_2,streamlines_y_plot_0_2, 'b')
    ax2.plot(streamlines_x_plot_0_4,streamlines_y_plot_0_4, 'b')
    ax2.plot(streamlines_x_plot_0_6,streamlines_y_plot_0_6, 'b')
    ax2.plot(streamlines_x_plot_0_8,streamlines_y_plot_0_8, 'b')
    ax2.plot(streamlines_x_plot_1,streamlines_y_plot_1, color = 'black')
    ax2.plot(streamlines_x_plot_1_2,streamlines_y_plot_1_2, 'b')
    ax2.plot(streamlines_x_plot_1_4,streamlines_y_plot_1_4, 'b')
    ax2.plot(streamlines_x_plot_1_6,streamlines_y_plot_1_6, 'b')
    
    
    ax2.plot(streamlines_x_plot_0_2,streamlines_y_plot_0_2_mirror, 'b')
    ax2.plot(streamlines_x_plot_0_4,streamlines_y_plot_0_4_mirror, 'b')
    ax2.plot(streamlines_x_plot_0_6,streamlines_y_plot_0_6_mirror, 'b')
    ax2.plot(streamlines_x_plot_0_8,streamlines_y_plot_0_8_mirror, 'b')
    ax2.plot(streamlines_x_plot_1,streamlines_y_plot_1_mirror, color = 'black')
    ax2.plot(streamlines_x_plot_1_2,streamlines_y_plot_1_2_mirror, 'b')
    ax2.plot(streamlines_x_plot_1_4,streamlines_y_plot_1_4_mirror, 'b')
    ax2.plot(streamlines_x_plot_1_6,streamlines_y_plot_1_6_mirror, 'b')
    
    

    ax2.set(xlabel='x [m]', ylabel ='y [m]', xlim = [-175, 225], ylim = [-175,175])
    fig.savefig("isochrones.png", dpi=300)

interact(uniform_flow,
         K=widgets.FloatLogSlider(value=3e-4, base=10, min=-10, max=0, step=0.1, description='hydraulic conductivity [m/s]:', disabled=False),
         ne=widgets.FloatSlider(value=0.2, min=0.001, max=1, step=0.05, description='effective porosity [-]:', disabled=False),
         m= widgets.FloatSlider(value=7,min=0, max=30,step=1, description='thickness [m]:' , disabled=False),
         v=widgets.FloatSlider(value=0.4, min=0.00001, max=5, step=0.1, description='uniform velocity [m/d]:', disabled=False),
         Q=widgets.FloatSlider(value=800, min=100, max=1000, step=0.1, description='pumping rate [m^3/d]:', disabled=False),
         t1=widgets.BoundedFloatText(value=10, min=1, max=100, step=0.1, description='t1 [d]:', disabled=False),
         t2=widgets.BoundedFloatText(value=30, min=1, max=100, step=0.1, description='t2 [d]:', disabled=False),
         t3=widgets.BoundedFloatText(value=50, min=1, max=100, step=0.1, description='t3 [d]:', disabled=False),
         )
         



# In[ ]:




