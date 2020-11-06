#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ipywidgets as widgets
get_ipython().run_line_magic('matplotlib', 'widget')
import warnings; warnings.simplefilter('ignore')


# ## Simulating Seive Analysis ##

# In[2]:


print("Please provide the seive data in the boxes:  ")

def SA(mu, m1, m2, m3, m4, ml):
    dia = [6,2,0.6,0.2, 0.06, 0.01] # mm, diameter <0.06 (cup)= 0.01, >2 = 6
    mass = [mu, m1, m2, m3, m4, ml] # g, the residue in seive 
    Total_mass = np.sum(mass)  # add the mass column to get total mass
    retain_per = np.round(mass/Total_mass*100,3)   # retain percentage
    retain_per_cumsum = np.round(np.cumsum(retain_per),3) # get the cummulative sum of the reatined
    passing_per = np.round(100 - retain_per_cumsum, 3) # substract 100-cummsum to get passing %
    data = {"mesh diameter [mm]": dia, "residue in the sieve [g]": mass, "Σtotal": retain_per, "Σ/Σtotal": passing_per }

    df1= pd.DataFrame(data)
    df1 = df1.set_index("mesh diameter [mm]")
    print(df1)

    plt.rcParams['axes.linewidth']=2
    #plt.rcParams["axes.edgecolor"]='white'
    plt.rcParams['grid.linestyle']='--'
    plt.rcParams['grid.linewidth']=1
    x = np.append([20],dia) # adding data to extend over 6 mm dia
    y = np.append([100],passing_per) # adding 100% to plot

    fig, ax = plt.subplots(figsize=(6,4))
    fig.canvas.header_visible = False
    plt.semilogx(x, y, 'x-', color='red')  
    tics=x.tolist()

    ax.grid(which='major', color='k', alpha=0.7) 
    ax.grid(which='minor', color='k', alpha=0.3)
    ax.set_xticks(x);  
    ax.set_yticks(np.arange(0,110,10));
    plt.title('grain size distribution');
    plt.xlabel('grain size d [mm]');
    plt.ylabel('grain fraction < d ins % of total mass');
    ax.set_xlim(0, 30)
    from matplotlib.ticker import StrMethodFormatter
    ax.xaxis.set_major_formatter(StrMethodFormatter('{x:0.2f}'))


style = {'description_width': '200px'}    

Inter=widgets.interact_manual(SA, 
                       mu= widgets.FloatText(description="6 mm", style=style),
                       m1= widgets.FloatText(description="2 mm",style=style),
                       m2= widgets.FloatText(description="0.6 mm", style=style),
                       m3= widgets.FloatText(description="0.2 mm", style=style),
                       m4= widgets.FloatText(description="0.06 mm", style=style),
                       ml= widgets.FloatText(description="0.01 mm", style=style))


# In[3]:


def SA2(d10, d60, t):
    U = d60/d10
    K_h =  0.0116*(0.7+0.03*t)*d10**2
    print("\n The coefficient of non-uniformity: {0:0.2f}".format(U), "\n")
    print("The Hydraulic Conductivity based on Hazen Formula: {0:0.2e} m/s".format(K_h))

style = {'description_width': '200px'}    

Inter=widgets.interact_manual(SA2, 
                       d10= widgets.FloatText(description="d10 (mm)", style=style),
                       d60= widgets.FloatText(description="d60 (mm)",style=style),
                       t= widgets.FloatText(description="Temperature (°C)", style=style))


# In[ ]:




