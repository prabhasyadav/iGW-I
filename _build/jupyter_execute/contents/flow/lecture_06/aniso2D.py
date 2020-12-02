#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#input 


# In[2]:



a_d = 90*2# degree
ani_r = 1 # aniso


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

print(i_xr, i_zr,K_h, K_v, f_x, f_z, f_m, an_i_f)

grad_px = [0, i_xr]#i_xr
grad_pz = [0, i_zr]#i_zr
plt.plot(grad_pz, grad_px, "r")

flux_px = [0, f_x]
flux_pz = [0, f_z]
plt.plot(flux_pz, flux_px, "g")

data={"grad_px":grad_px, "grad_pz":grad_pz, "flux_px":flux_px, "flux_pz":flux_pz}
df1=pd.DataFrame(data)
df1


# ## i_xr

# In[ ]:




