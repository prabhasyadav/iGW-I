#!/usr/bin/env python
# coding: utf-8

# ## Simulating Mass Budget ##
# 
# #### How to use the tool? ####
# 
# 1. Go to the Binder by clicking the rocket button (top-right of the page)
# 2. Execute the code cell
# 3. Change the values of different quantities in the box.
# 
# This tool can also be downloaded and run locally. For that download the _deacy.ipynb_ file and execute the process in any editor (e.g., JUPYTER notebook, JUPYTER lab) that is able to read and execute this file-type.
# 
# The code may also be executed in the book page.
# 
# The codes are licensed under CC by 4.0 [(use anyways, but acknowledge the original work)](https://creativecommons.org/licenses/by/4.0/deed.en)

# In[1]:


# Used library
import numpy as np # for calculation
import matplotlib.pyplot as plt # for plots
import pandas as pd  # for table
import ipywidgets as widgets  # for widgets

# The main function

def mass_bal(n_simulation, MA, MB, MC, R_A, R_B):
    
    A = np.zeros(n_simulation) # creat an array with zros
    B = np.zeros(n_simulation)
    C = np.zeros(n_simulation) 
    time  = np.arange(n_simulation)
    
    for i in range(0,n_simulation-1):
        A[0] = MA  # starting input value
        
        B[0] = MB
        C[0] = MC
        A[i+1] = A[i]-R_A*A[i]
        B[i+1] = B[i]+R_A*A[i]-R_B*B[i] 
        C[i+1] = C[i]+R_B*B[i]
        summ = A[i]+B[i]+C[i]
        
    d = {"Mass_A": A, "Mass_B": B, "Mass_C": C, "Total Mass": summ}
    df = pd.DataFrame(d) # Generating result table
    label = ["Mass A (g)", "Mass B (g)", "Mass C (g)"]
    fig = plt.figure(figsize=(6,4))
    plt.plot(time, A, time, B, time, C, linewidth=3);  # plotting the results
    plt.xlabel("Time [Time Unit]"); plt.ylabel("Mass [g]") # placing axis labels
    plt.legend(label, loc=0);plt.grid(); plt.xlim([0,n_simulation]); plt.ylim(bottom=0) # legends, grids, x,y limits
    plt.show() # display plot
    
    return print(df.round(2)) 

# Widgets and interactive

N = widgets.BoundedIntText(value=20,min=0,max=100,step=1,description= '&Delta; t (day)',disabled=False)

A = widgets.BoundedFloatText(value=100,min=0,max=1000.0,step=1,description='M<sub>A</sub> (kg)',disabled=False)

B = widgets.BoundedFloatText(value=5,min=0,max=1000.0,step=1,description='M<sub>B</sub> (kg)',disabled=False)

C = widgets.BoundedFloatText(value=10,min=0,max=1000,step=0.1,description='M<sub>C</sub> (kg)',disabled=False)

RA = widgets.BoundedFloatText(value=0.2,min=0,max=100,step=0.1,description='R<sub>A</sub> (day<sup>-1 </sup>)',disabled=False)

RB = widgets.BoundedFloatText(value=0.2,min=0,max=100,step=0.1,description='R<sub>B</sub> (day<sup>-1 </sup>)',disabled=False)

interactive_plot = widgets.interactive(mass_bal, n_simulation = N, MA=A, MB=B, MC=C, R_A=RA, R_B=RB,)
output = interactive_plot.children[-1]  
#output.layout.height = '350px'
interactive_plot

