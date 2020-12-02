#!/usr/bin/env python
# coding: utf-8

# ## Simulating the Anisotropy and flow direction
# 
# ### How to use the tool?
# 
# 1. Go to the Binder by clicking the rocket button (top-right of the page)
# 2. Execute the code cell
# 3. Change the values of different quantities in the box.
# 4. For re-simulations - changes the input values in the boxes. 
# 
# This tool can also be downloaded and run locally. For that download the _aniso2D.ipynb_ file and execute the process in any editor (e.g., JUPYTER notebook, JUPYTER lab) that is able to read and execute this file-type.
# 
# The code may also be executed in the book page. 
# 
# The codes are licensed under CC by 4.0 [(use anyways, but acknowledge the original work)](https://creativecommons.org/licenses/by/4.0/deed.en)
# 
# 
# 

# In[1]:


# The library used 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ipywidgets import widgets, interactive

# the main programme
def aniso(a_d, ani_r):

# interim calculation
    a_r = a_d*np.pi/180

    i_xr = np.cos(a_r) # (-), rel. hyd grad. along x
    i_zr = np.sin(a_r) # (-), rel. hyd grad. along z
    K_h = 1 # (-), m/s K_h
    K_v = 1/ani_r # m/s, rel K_v
    f_x = -i_xr*K_h # m/s
    f_z = -i_zr*K_v # m/s
    f_m = np.sqrt(f_x*f_x+f_z*f_z) # m/s

    args = (K_h*i_xr*i_xr + K_v*i_zr*i_zr)/f_m
    an_i_f = ((np.pi-np.arccos(args))*180/np.pi)# deg,

# plots axes

    fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(10,6), gridspec_kw={'width_ratios': [3, 1]})

# points for gradient and flux

    grad_px = [0, i_xr]#i_xr
    grad_pz = [0, i_zr]#i_zr

    flux_px = [0, f_x]
    flux_pz = [0, f_z]

# creating points for intersect lines (5 of them)

    p1=-0.5*i_zr; p2 = 0.5*i_zr; p3 =-0.5*i_zr+0.35*i_xr; p4 = 0.5*i_zr+0.35*i_xr; p5 = -0.5*i_zr+0.7*i_xr
    p6 = 0.5*i_zr+0.7*i_xr;p7 = -0.5*i_zr-0.35*i_xr; p8 = 0.5*i_zr-0.35*i_xr; p9 = -0.5*i_zr-0.7*i_xr;p10 =0.5*i_zr-0.7*i_xr

    q1=0.5*i_xr; q2 =- 0.5*i_xr; q3 =0.5*i_xr+0.35*i_zr; q4 = -0.5*i_xr+0.35*i_zr; q5 = 0.5*i_xr+0.7*i_zr
    q6 = -0.5*i_xr+0.7*i_zr;q7 = 0.5*i_xr-0.35*i_zr;q8 = -0.5*i_xr-0.35*i_zr; q9 = 0.5*i_xr-0.7*i_zr;q10 = -0.5*i_xr-0.7*i_zr

# plotted points
    l_1x =[p1, p2]; l_1y = [q1, q2]
    l_2x =[p3, p4]; l_2y = [q3, q4]
    l_3x =[p5, p6]; l_3y = [q5, q6]
    l_4x =[p7, p8]; l_4y = [q7, q8]
    l_5x =[p9, p10]; l_5y = [q9, q10]


# creating points for anisotropy
    r1 =1.05 if ani_r >= 1 else 1.5-0.45*ani_r
    r2 = 1.95 if ani_r >= 1 else 1.5+0.45*ani_r
    r3 = 0.5*(r1+r2); r4 = r3

    s1 = -0.5; s2 = s1
    s3 = -0.05 if ani_r<=1 else -0.5+0.45/ani_r
    s4 = -0.95 if ani_r<=1 else -0.5-0.45/ani_r

# plotted points
    Iso_1x = [r1, r2]; Iso_1y = [s1, s2]
    Iso_2x = [r3, r4]; Iso_2y = [s3, s4]
    Iso_x =[r1, r2, r3, r4]; Iso_y = [s1,s2,s3,s4]

# plotting all points

# plotting gradient/flux lines

    ax1.plot(grad_px, grad_pz, "g", label=" gradient") # plotting gradient
    ax1.plot(flux_px, flux_pz, "r", label=" flux") # plotting flux

# plotting intersect lines 
    ax1.plot(l_1x, l_1y, "b", label = "head isoline")
    ax1.plot(l_2x, l_2y, "b")
    ax1.plot(l_3x, l_3y, "b")
    ax1.plot(l_4x, l_4y, "b")
    ax1.plot(l_5x, l_5y, "b")
    ax1.legend()


    ax1.spines['left'].set_position('center') # bring the axis lines in center
    ax1.spines['bottom'].set_position('center')
    ax1.spines['right'].set_color('none') # remove the top box
    ax1.spines['top'].set_color('none') 
    ax1.set_xticks([]);ax1.set_yticks([]); # remove the ticks
    ax1.set_title("Anisotropy flux and gradient", y=0, pad=-25, verticalalignment="top")


# plotting Anisotropy
    ax2.plot(Iso_1x, Iso_1y, "k", label = r"$K_h: K_v$")
    ax2.plot(Iso_2x, Iso_2y, "k")
    ax2.legend(bbox_to_anchor=(-0.4, -0.05), loc='lower left')
    ax2.set_xlim(1, 2)
    ax2.set_ylim(-1, 1)
    ax2.axis('off')
    ax2.set_title("Anisotropy ratio", y=0, pad=-25, verticalalignment="top");

interactive(aniso,
         a_d=widgets.BoundedFloatText(value=45, min=0, max=360, step=0.5, description=r'angle (°)', disabled=False),
         ani_r=widgets.BoundedIntText(value=1, min=1, max=100, step=1, description='K<sub>h</sub>/K<sub>v</sub>', disabled=False),)
    


# In[ ]:




