#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import panel as pn
pn.extension('katex', 'mathjax') 
from ipywidgets import interact, widgets


# In[2]:


data19 = pd.read_csv("T07_TP19_data.csv", sep = ",", usecols =["Time (min)", "Drawdown (m)"])

df_t1= data19.values[:,0]
df_s1= data19.values[:,1]

d = {'time [min]': df_t1, 'drawdown [m]': df_s1}
df = pd.DataFrame(data=d, index=None) 
df.head(5)


# In[3]:


#given
r = 251.32 # m, observation well distance
t_s = df_t1*60 # s, converting time in s
t_r2 = t_s/r**2# s/m^2,  finding t/r^2 

#output
d2= {'time [min]': df_t1, 'drawdown [m]': df_s1, "t/r2 (s/m^2)": t_r2}  
df2 = pd.DataFrame(data=d2, index=None) 

pn.Row(df2) 


# In[4]:


#
# Typ curve
#code to find W(u) (see L07/S-31) using the infinite series W(u) = -0.5772-log(u)+u-u^2/(2*2!)+u^3/(3*3!)-... (100 terms) 
# It is possible to use: from scipy.special import expi def W(u):  return  -expi(-u)

# W(u) = -0.5772-log(u)+u-u^2/(2*2!)+u^3/(3*3!)-... (100 terms) 

def W(u):  
    w = -0.5772 -np.log(u) + u
    a = u
    for n in range(1, 100):
        a = -a * u * n / (n+1)**2 # new term (next term)
        w += a  # w = w+a
        return w
        
u_1 = np.logspace(10,-1,250, base=10.0) # setting the value of u
w_u =W(1/u_1) # finding W(1/u) : as we use 1/u in the typ curce
        
plt.figure(figsize=(9,6)) 
plt.loglog(u_1, w_u) 
plt.title("The typ curve"); plt.ylim((0.1, 10)); plt.xlim(1, 1e5)
plt.grid(True, which="both",ls="-"); plt.ylabel(r"W(u)");plt.xlabel(r"1/u") ;


# In[5]:


# Solution from typ curve (extra code)

# Data to fit
p_r = 50/3600 # m^3/s, pumping rate /3600 for unit /h- /s
r = 251.32 # m, distance of observation well
m = 14.65 # m, aquifer thickness
d_s = df_s1 # m, drawdown data

# Obtained from graphical method
S_C = 2.21e-05 # (-), storage coeff.
T = 0.00138 # m^2/s, transmissivity
K_aq = T/m

#Calculations
u_1d = 4*T*t_s/(S_C*r**2)  
w_ud = 4*np.pi*d_s*T/p_r

# plots
u_1 = np.logspace(10,-1,250, base=10.0)
w_u =W(1/u_1) 
        
plt.figure(figsize=(9,6)) 
plt.loglog(u_1, w_u) 
plt.loglog(u_1d, w_ud, "o", color="red"  )
plt.ylim((0.1, 10))
plt.xlim(1, 1e5)
plt.grid(True, which="both",ls="-") 
plt.ylabel(r"W(u)");
plt.xlabel(r"1/u") ;


# In[ ]:




