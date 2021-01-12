#!/usr/bin/env python
# coding: utf-8

# ## Simulating Degradation ##

# ## Some Basics 
# 
# Degradation includes **all reactive processes** wich eventually lead to the removal of a chemical from the subsurface.
# This is in contrast to sorption/desorption processes which only lead to a transfer of the chemical between the dissolved and the sorbed phase.
# 
# Degradation can appear as
# - radioactive decay 
# - mikrobial degradation (biodegradation)
# - chemical degradation 
# 
# It is important to note that degradation **results in daughter products (metabolites).** This can reduce or increase the toxicity in the subsurface.
# 
# Several laws were suggested to quantify degradation processes. All of them assume degradation to be **time-dependent ("kinetics").**

# ## $n^{th}$- Order Degradation Kinetics
# 
# The Equation for the degradation kinetics is
# 
# $$ \frac{dC}{dt}= - \lambda \cdot C^n $$
# 
# with $t$ = time $[T]$, $C$ = solute concentration $[M/L^3]$, $n$ = order of the degradation kinetics $[-]$ and $\lambda$ = degradation rate constant $[(M/L^3)^{1-n}/T]$
# 
# When you solve this Equation for an initial concentration $C_0$ you get following equitions: 
# 
# $$C(t)=C_0 \cdot e^{-\lambda \cdot t} \quad  \text{if} \quad  n = 1 $$
# 
# $$C(t)=[ C_0^{ 1-n} -(1-n) \cdot \lambda \cdot t ]^{\frac {1}{1-n}} \quad  \text{if} \quad  n \ne 1 $$
# 
# The **half life** $T_{1/2}$ is the time span elapsing until the initial concentration is reduced by half. $T_{1/2}$ **depends on the initial concentration** in nearly all cases. An **exception is the $1^{st}$-order degradation** kinetics. 
# 
# For degradation kinetics of order $n<1$ the solute concentration reaches zero. While the degradation kinetics of orders $n \geq 1$ the solute concentration only asymptotically approach zero.

# ## Special Cases 

# ### $0^{st}$ - order kinetics (n = 0)
# 
# An other special case is the dagradation of $0^{st}$ **- order.** 
# 
# For $n = 0$ the general equation becomes:
# 
# $$C(t) = C_0  - \lambda \cdot t$$
# 
# with $$T_{1/2}= \frac{C_0}{2 \cdot \lambda} $$
# 
# The **speed of the reaction is independent of the initital concentration** of the reaction partners. During a period of time, therefore, the same amount of substance is always converted, regardless of the respective concentration.
# 
# $0^{st}$ **- order kinetics** can be
# - enzyme reactions,
# - photochemical reactions or
# - reactions on solid surfaces

# The following example shows the enzymatic degradation of ethanol in the human and organism.
# 

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from ipywidgets import interact, fixed
import ipywidgets as widgets


# In[2]:


def alcohol(C0,λ,t):
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


# ### $1^{st}$ - order kinetics (n = 1)
# 
# The  $1^{st}$ - order kinetics represent one of the most important special cases of the general $n^{th}$ - order kinetics.
# 
# For $n=1$ the general equation results in 
# 
# $$ C(t) = C_0 \cdot e^{- \lambda \cdot t}$$
# 
# with  $$T_{1/2} = \frac{ln2}{\lambda}$$
# 
# The speed of this kinetics is proportional to the solute concentration. For example, this is the case with **radioactive decay.**
# 

# The following diagram shows the degradation of the elements cobalt and strontium. 

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

# The Equation for the Michaelis-Menten degradation kinetics is:
# 
# $$ \frac{dC}{dt} = - \frac{k \cdot C}{k_m + C}$$
# 
# with $t$ = time $[T]$, $C$ = solute concentration $[M/L^3]$, $k$ = rate constant $[M/L^3/T]$ and $k_m$ = degradation parameter $[M/L^3]$.
# 
# $k_m$ characterizes the affinity of the enzyme to its substrate. It corresponds to the substrate concentration at wich half the maximum reaction rate is reached.
# 
# When the equation is solved (implicit) for an initial concentration $C_0$, it becomes to:
# 
# $$ t = \frac{C_0-C(t)}{k}+\frac{k_m}{k}\cdot ln \frac{C_0}{C(t)}$$
# 
# The half life $T_{1/2}$ depends on the initial concentration $C_0$ as well as the $0^{th}$-order degradation kinetics. 
# 
# $$ T_{1/2} = \frac{C_0}{2 \cdot k} + \frac{k_m}{k} \cdot ln2 $$
# 
# 

# In[4]:


### Simulating Michaelis-Menten-Kinetics


# In[5]:


def MM1(C_i, P_s, H_l, R_f, n_sim):
    
    """
    C_i = Initial concentration [M/L^3]
    P_s = Coefficient- shape factor 
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




