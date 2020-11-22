#!/usr/bin/env python
# coding: utf-8

# # Layered Systems

# In[1]:


import numpy as np


# ## Case I - Flow Parallel to Layering

# In[2]:


print("\033[1m\033[4mA quick example:\033[0m You can change the provided values.\n")
print("Calculate the effective hydraulic conductivity of the layer system consisting of 5 layers if the flow is parallel to the stratification.\n\n\033[1mProvided are:\033[0m")

#Thickness of i-th layer [m]
m1 = 3 
m2 = 2.5
m3 = 1.75

#conductivity of i-th layer [m/s]
K1 = 3.5e-3
K2 = 2e-2
K3 = 5e-4


#intermediate calculation
m = m1+m2+m3

#solution
K = (m1*K1+m2*K2+m3*K3)/m
print("thickness of layer 1 = {}".format(m1), "m\nthickness of layer 2 = {}".format(m2),"m\nthickness of layer 3 = {}".format(m3), "m\nconductivity of layer 1 = {:02.1e}".format(K1),
      "m/s\nconductivity of layer 2 = {:02.1e}".format(K2), "m/s\nconductivity of layer 3 {:02.1e}".format(K3), "m/s")
print("\n\033[1mSolution:\033[0m\nThe resulting hydraulic conductivity of the layer system is \033[1m{:02.1e} m/s\033[0m.".format(K))


# ## Case II - Flow Perpendicular to Layering

# In[3]:


print("\033[1m\033[4mA quick example:\033[0m You can change the provided values.\n")
print("Calculate the effective hydraulic conductivity of the layer system consisting of 5 layers if the flow is perpendicular to the layering.\n\n\033[1mProvided are:\033[0m")

#Thickness of i-th layer [m]
m1 = 3 
m2 = 2.5
m3 = 1.75

#conductivity of i-th layer [m/s]
K1 = 3.5e-3
K2 = 2e-2
K3 = 5e-4

#intermediate calculation
m = m1+m2+m3

#solution
K = m/(m1/K1+m2/K2+m3/K3)

print("thickness of layer 1 = {}".format(m1), "m\nthickness of layer 2 = {}".format(m2),"m\nthickness of layer 3 = {}".format(m3), "m\nconductivity of layer 1 = {:02.1e}".format(K1),
      "m/s\nconductivity of layer 2 = {:02.1e}".format(K2), "m/s\nconductivity of layer 3 {:02.1e}".format(K3), "m/s")
print("\n\033[1mSolution:\033[0m\nThe resulting hydraulic conductivity of the layer system is \033[1m{:02.1e} m/s\033[0m.".format(K))


# In[ ]:




