#!/usr/bin/env python
# coding: utf-8

# # .  1D_FD_ homogeneous

# In[1]:


import numpy as np
import itertools  as itt
import matplotlib.pyplot as plt 
import pandas as pd 
from numpy import array
import sys
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual


# In[2]:




def Head(start_head, final_head, steps, R2, R3, R4, R5, R6, R7, R8, R9, R10, m, K, X):
    h=np.array([[start_head, start_head-steps, start_head-(2*steps), start_head-(3*steps), start_head-(4*steps), 
             start_head-(5*steps), start_head-(6*steps), start_head-(7*steps), start_head-(8*steps), start_head-(9*steps),
             start_head-(10*steps)],
             [start_head, 0, 0, 0, 0, 0, 0, 0, 0, 0, final_head],
             [start_head, 0, 0, 0, 0, 0, 0, 0, 0, 0, final_head],
             [start_head, 0, 0, 0, 0, 0, 0, 0, 0, 0, final_head],
             [start_head, 0, 0, 0, 0, 0, 0, 0, 0, 0, final_head],
             [start_head, 0, 0, 0, 0, 0, 0, 0, 0, 0, final_head]])
    T=K*m
    R1_new=0
    R2_new=(R2/2*T)*(X**2)
    R3_new=(R3/2*T)*(X**2)
    R4_new=(R4/2*T)*(X**2)
    R5_new=(R5/2*T)*(X**2)
    R6_new=(R6/2*T)*(X**2)
    R7_new=(R7/2*T)*(X**2)
    R8_new=(R8/2*T)*(X**2)
    R9_new=(R9/2*T)*(X**2)
    R10_new=(R10/2*T)*(X**2)
    R11_new=0
    R=np.array([[0, R2_new, R3_new, R4_new, R5_new, R6_new, R7_new, R8_new, R9_new, R10_new, 0],
                [0, R2_new, R3_new, R4_new, R5_new, R6_new, R7_new, R8_new, R9_new, R10_new, 0],
                [0, R2_new, R3_new, R4_new, R5_new, R6_new, R7_new, R8_new, R9_new, R10_new, 0],
                [0, R2_new, R3_new, R4_new, R5_new, R6_new, R7_new, R8_new, R9_new, R10_new, 0],
                [0, R2_new, R3_new, R4_new, R5_new, R6_new, R7_new, R8_new, R9_new, R10_new, 0],
                [0, R2_new, R3_new, R4_new, R5_new, R6_new, R7_new, R8_new, R9_new, R10_new, 0]])
    for r in range(1, 6):
        for c in range (1, 10):
            h[r,c]=0.5*(h[r-1, c-1] + h[r-1, c+1])


    Final_head=h+R
    print( "The final matrix of hydraulic head iteraion is:", "\n", Final_head)
    return 
style = {'description_width': 'initial'} 
inter=widgets.interact_manual(Head,
                              start_head=widgets.FloatText(description="Starting head", style=style),
                              final_head=widgets.FloatText(description="Finished head", style=style),
                              steps=widgets.FloatText(description="head difference", style=style),
                              R2= widgets.FloatText(description= "Recharge on cell 2", style=style),
                              R3= widgets.FloatText(description= "Recharge on cell 3", style=style),
                              R4= widgets.FloatText(description= "Recharge on cell 4", style=style),
                              R5= widgets.FloatText(description= "Recharge on cell 5", style=style),
                              R6= widgets.FloatText(description= "Recharge on cell 6", style=style),
                              R7= widgets.FloatText(description= "Recharge on cell 7", style=style),
                              R8= widgets.FloatText(description= "Recharge on cell 8", style=style),
                              R9= widgets.FloatText(description= "Recharge on cell 9", style=style),
                              R10= widgets.FloatText(description= "Recharge on cell 10", style=style),
                              R11= widgets.FloatText(description= "Recharge on cell 11", style=style),
                              K=widgets.FloatText(description= "Hydraulic conductivity", style=style),
                              m=widgets.FloatText(description= "Aquifer thickness", style=style),
                              X=widgets.FloatText(description="Cell increment", style=style))
                              

