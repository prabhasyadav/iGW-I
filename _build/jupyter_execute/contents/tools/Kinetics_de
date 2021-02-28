#!/usr/bin/env python
# coding: utf-8

# ## Simulating Kinetics and Degradation ##

# The tool simulates:
# 
# 1. Enzymatic degradation of ethanol e.g., in the human and organism.
# 2. Decay of radioactive elements e.g., Cobalt, Strontium 
# 3. Michaelis–Menten Kinetics

# ### How to use this tool ###
# 
# 1. Go to the Binder by clicking the rocket button (top-right of the page)
# 
# 2. Execute the code cell with libraries 
# 
# 3. Interact with the sliders.
# 
# The codes are licensed under CC by 4.0 [(use anyways, but acknowledge the original work)](https://creativecommons.org/licenses/by/4.0/deed.en)

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from ipywidgets import interact, fixed
import ipywidgets as widgets


# The enzymatic degradation of ethanol in the human and organism.

# In[2]:


def alcohol(C0,λ,t):
    
    """
    C0 = concentration [M/L^3]
    λ = degradation constant [M/L^3/T]
    t = time [T]
    
    """
    
    plt.figure()
    t = np.linspace(0, t, 1000)
    plt.plot(t, C0 - λ * t)
    plt.ylabel('Blood alcohol concentration [‰]')
    plt.title('enzymatic degradation of ethanol')
    plt.ylim(0,8.1) #the highest measured blood alcohol concentration in germany 
    plt.xlabel('time [h]')
    plt.xlim(0,100)
    plt.show()

    
interact(alcohol, C0 = widgets.FloatSlider(min=0, max= 8.1, step=0.1, value=3), 
         t= fixed(200), λ=widgets.FloatSlider(min=0,max=1, value=0.15, step=0.01, readout_format='.2f'))


# The decay of the elements cobalt and strontium. 

# In[3]:


def Co(C0,λ,t): #define the funtion for the decay of cobalt
   
    plt.figure()
    t = np.linspace(0, t, 1000)
    y= C0 * np.exp(-(λ * t)) #equation for 0th-degradation kinetics
    plt.plot(t, y)
    plt.ylabel('solute concentration [mg/l]')
    plt.title('radioactive decay of cobalt')
    plt.ylim(0,100)
    plt.xlabel('time [a]')
    plt.xlim(0,200)
    plt.show()

    
interact(Co, C0 = widgets.IntSlider(min=0, max= 100, step=1, value=100),
         t = fixed(1000),
         λ = widgets.FloatSlider(value=0.132, min=0, max=1, step=0.001, readout_format='.3f'))

def Sr(C0,λ,t): #define the function for the decay of strontium
    plt.figure()
    t = np.linspace(0, t, 1000)
    y= C0 * np.exp(-(λ * t))
    plt.plot(t, y)
    plt.ylabel('solute concentration [mg/l]')
    plt.title('radioactive decay of strontium')
    plt.ylim(0,100)
    plt.xlabel('time [a]')
    plt.xlim(0,200)
    

interact(Sr, C0 = widgets.IntSlider(min=0, max= 100, step=1, value=100),
         t= fixed(1000),
         λ=widgets.FloatSlider(min=0,max=1, value=0.025, step=0.001, readout_format='.3f'))


# ### Michaelis-Menten-Kinetics
# 
# The Michaelis-Menten degradation kinetics behaves like a $0^{th}$-order kinetics for **"short" times** and like a $1^{st}$-order kinetics for **"long" times.** It describes the dependence of the speed of an enzyme-catalyzed reaction on the substrate concentration.

# In[4]:


def MM1(C_i, P_s, H_l, R_f, n_sim):
    
    """
    C_i = Initial concentration [M/L^3]
    P_s = Coefficient- shape factor [M/L^3]
    t
    """
    
    #intermediate calculation
    MM_rc = (0.5*C_i+P_s*np.log(2))/H_l # [M/L^3/T], Michaelis-Menten rate constant

    ZO_rc = MM_rc*C_i/(P_s+C_i) # [M/L^3/T], Zero order rate constant

    ZO_hl = 0.5*C_i/ZO_rc # [T], half-life
    t_c0 = 2*ZO_hl # [T] time to reach C=0

    FO_rc = MM_rc/P_s
    FO_hl = np.log(2)/FO_rc # [T], half-life
    FO_ci = C_i*np.exp(C_i/2) # [M/L^3]

    # Main Computing

    MM = np.zeros(n_sim)  # creat an array with zros

    for i in range(0, n_sim-1):
        MM[0] = C_i
        MM[i+1] = MM[i]*R_f
#        MM[i]

    time = (C_i-MM)/MM_rc - P_s/MM_rc * np.log(MM/C_i)

    ZO = C_i-ZO_rc*time
    ZO[ZO < 0] = 0 # forcing -ve conc. to be zero

    FO = FO_ci*np.exp(-FO_rc*time)
    FO[FO < 0] = 0 # forcing -ve conc. to be zero

    
#    dict1 = {"time [T]": time, "Michaelis-Menten": MM[i], "Zero-Order":ZO, "First-Order": FO}
#    pd.DataFrame(dict1)

    plt.plot(time, MM, "-r", label="Michaelis Menten")
    plt.plot(time, FO,"-g", label="First Order")
    plt.plot(time, ZO,"-b", label="Zero Order")
    plt.xlabel("time [T]"); plt.ylabel(r"Concentration [M/L$^3$]")
    plt.legend()    
    plt.grid()


interact(MM1, 
         C_i = widgets.FloatSlider(min=0.001, max= 10., step=0.01, value=1.0, readout_format='.2f'),
         P_s = widgets.IntSlider(min=1, max= 10, step=1, value=2),
         H_l = widgets.FloatSlider(min=1., max= 1000., step=1., value=300., readout_format='.1f'),
         R_f = widgets.FloatSlider(min=0.01, max= 1., step=0.1, value=0.97, readout_format='.2f'),
         n_sim = widgets.IntSlider(min=1, max= 1000, step=1, value=150))


# In[ ]:




