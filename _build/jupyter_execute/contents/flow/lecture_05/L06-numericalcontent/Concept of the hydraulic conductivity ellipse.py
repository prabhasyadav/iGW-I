#!/usr/bin/env python
# coding: utf-8

# ## Concept of the hydraulic conductivity ellipse

# In[1]:


import numpy as np


# In[2]:


print("\033[1m\033[4mA quick example:\033[0m You can change the provided values.\n")
print("Calculate the hydraulic conductivity.\n\n\033[1mProvided are:\033[0m\n")

Kh =  1e-3 #horizontal hydraulic conductivity [m/s]
Kv =  1e-4 #vertical hydraulic conductivity [m/s]
theta = 50 #angle between flow direction ans horizontal plane [°]

#solution
K = 1 /((np.cos(theta)**2/Kh)+(np.sin(theta)**2/Kv))

print("horizontal hydraulic conductivity = {:02.1e}".format(Kh), "m/s\n" "vertical hydraulic conductivity = {:02.1e}".format(Kv), "m/s\n"
      "angle = {}°\n".format(theta))
print("\033[1mSolution:\033[0m\nThe resulting hydraulic conductivity is \033[1m{:02.1e} m/s\033[0m.".format(K))

