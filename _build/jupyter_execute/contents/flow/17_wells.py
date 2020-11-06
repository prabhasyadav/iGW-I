#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import pandas as pd


# #  Lecture 7 -  Wells and aquifer
# 
# ## Prof. Liedl/Prof. Werth/Prof. Chahar/Prabhas is to add the text contents.
# ## Anne/Sophie is to add the numerical contents
# 
# Include ipynb file for:
# 
# Theis method.
# 
# 

# ## Transmissivity ##

# When discussing storage properties in Chapter / Lecture …, we saw that aquifers or single layers may frequently be treated as two-dimensional systems. This is justified because the lateral extension of aquifers is usually much larger than the vertical extension. Thus, vertical variations of storage properties can be replaced by some average value without adversely affecting the quantification of groundwater storage.
# 
# Similar things can be done with regard to conductivity properties and this brings us to the geohydraulic parameter of **Transmissivity**. The idea is to neglect vertical variations of _hydraulic conductivity_ ($K$)  and to use vertically averaged values instead. This procedure does not eliminate horizontal variability, so _transmissivity_ may still depend on horizontal coordinates $(x, y)$.
# 
# The vertically averaged $K$ value is then multiplied by the water-saturated thickness to obtain transmissivity. The concept of water-saturated thickness (or water-saturated depth) requires to distinguish whether _confined_ or _unconfined_ flow conditions prevail.
# 
# In general, water-saturated thickness is the distance from the aquifer bottom to a level up to which all pores are filled with water. For _confined aquifers_, this level is equal to aquifer top and water-saturated thickness is tantamount to aquifer thickness. For _unconfined aquifers_, however, water-saturated thickness corresponds to the distance between aquifer bottom and groundwater level. We will see some illustrations below when we try to quantify _transmissivity_.
# 
# The symbol $T$ is mostly used to denote transmissivity which has a dimension of $L^2T^{-1}$.
# 
# 

# Let us have a closer look at the confined case first. The black cuboid in Fig.[LINK] illustrates that water-saturated thickness extends from aquifer bottom to aquifer top. So, it is equal to _aquifer thickness_ $m$. Transmissivity is calculated by
# 
# $$
# T_x = K_x \cdot m  \;\; \text{ and }  \;\; Ty = K_y \cdot m
# $$
# 
# Here we allow for horizontal aquifer anisotropy with different hydraulic conductivities in $x-$ and $y-$ direction $(K_x \neq K_y)$. 
# 
# For horizontally isotropic aquifers $(K_x = K_y = K)$, transmissivity is given by $T = K  \cdot m $.
# 
# <a href="fig1"></a><img src="images/L7_f1.png" alt ="Transmissivity-Confined aquifer" width = "400">
# 

# In[2]:


print("We already have large text content, equations and so we can add a simple numerical example here")


# Things are a bit more complicated for _unconfined aquifers_. Fig. [LINK] illustrates that water-saturated thickness extends from the aquifer bottom to the groundwater table. It is important to note that _transmissivity_ of unconfined aquifers depends on the vertical position of the groundwater table. 
# 
# For instance, if the groundwater table is lowered during to a draught period, _transmissivity_ is decreasing. This is fundamentally different from the confined case where the water-saturated thickness is given by aquifer geometry only and is not affected by hydraulic head changes.
# 
# <a href="fig2"></a><img src="images/L7_f2.png" alt ="Transmissivity-unconfined aquifer" width = "400">

# Computing transmissivity of unconfined aquifers requires to determine the difference of hydraulic head h and the elevation of aquifer bottom $z_{bot}$. Based on this, transmissivity is given by:
# 
# $$T_x = K_x \cdot (h – z_{bot})$$ 
# and 
# $$T_y = K_y \cdot (h – z_{bot})$$
# 
# As above, we are allowing for horizontal aquifer anisotropy. For an isotropic unconfined aquifer we get 
# $$T = K\cdot(h – z_{bot})$$

# In[3]:


print("We already have large text content, equations and so we can add a simple numerical example here")


# Two more remarks appear to be appropriate: 
# 
# - First, _transmissivity_ may be computed by the given equations even if the aquifer bottom is not horizontal. This case is not covered by the figure above. 
# - Second, textbooks frequently present the equation $$ T = K\cdot h $$ for transmissivity of unconfined aquifers. It is to be noted that this equation only holds if two conditions are fulfilled: 
# 
# - The aquifer bottom must be horizontal and 
# - hydraulic head values are expressed with respect to the elevation of aquifer bottom (= reference datum).
# 
# 
# Finally, we can try to compute transmissivity for isotropic aquifers and check how the result depends on several quantities like aquifer bottom, aquifer top, and hydraulic head.
# 

# In[4]:


# A bit more complicated numerical example here. An example from Prof. Liedl - we improve further.

print("Q1. Determine if the aquifer is confined or unconfind and compute it's Transmissivity")

# input

K = 8.5e-5 # m/s, hydraulic conductivity
Ab = 120 # m asl, aquifer bottom elevation 
At = 150 # m asl, aquifer top elevation 
H  = 139 # m, hydraulic head

#intermediate calculation
A_T = At - Ab # m, Aquifer thickness
S_T = np.minimum(A_T, (H - Ab))

# Results

if H < At:
   print("\n It is a unconfined aquifer")
else:
   print("\n It is a Confined aquifer")
   
T = K*A_T # m²/s, Transmissivity

print("\nThe transmissivity is {0:0.2e} m\u00b2/s".format(T))



# In[ ]:




