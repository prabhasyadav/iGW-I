#!/usr/bin/env python
# coding: utf-8

# ## Simulating Seive Analysis ##
# 
# _(The contents presented in this section were re-developed principally by Dr. P. K. Yadav. The original tool, Spreadsheet based, was developed by Prof. Rudolf Liedl)_
# 
# #### How to use the tool? ####
# 
# 1. Go to the Binder by clicking the rocket button (top-right of the page)
# 2. Execute the code cell
# 3. Change the values of different quantities in the box and click the **run interact**.
# 4. From the resulting figure, using your mouse and selecting points in the figure obtain d10 and d60. 
# 5. Execute the second code-cell and provide d10, d60 and temperature date
# 6. Click the exectute button.
# 7. For re-simulations - changes the input values in the boxes and click the "**run interact**" button. 
# 
# This tool can also be downloaded and run locally. For that download the _deacy.ipynb_ file and execute the process in any editor (e.g., JUPYTER notebook, JUPYTER lab) that is able to read and execute this file-type.
# 
# The code may also be executed in the book page. 
# 
# The codes are licensed under CC by 4.0 [(use anyways, but acknowledge the original work)](https://creativecommons.org/licenses/by/4.0/deed.en)

# In[1]:


# used Python library
import numpy as np # for calculation 
import matplotlib.pyplot as plt  # for plotting
import pandas as pd  # for data table
import ipywidgets as widgets # for widgets
get_ipython().run_line_magic('matplotlib', 'widget')
import warnings; warnings.simplefilter('ignore')

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


# **The plot shown is interactive use the pointer and others tools in the graph to obtain d10 and d60 for the next step**

# In[2]:


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




