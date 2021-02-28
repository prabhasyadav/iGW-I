#!/usr/bin/env python
# coding: utf-8

# ## Type curve and fitting pumping data tool ##
# 
# ### How to use this tool ###
# 
# 1. Go to the Binder by clicking the rocket button (top-right of the page)
# 
# 2. Execute the code cell with libraries 
# 
# 3. Provide pumping data: **t_m** for time in _minutes_ and **s_m** for drawdown in _meters_. Pls. do not change the name **t_m** and **s_m**.
# 
# 4. Execute the data code cell - and in the table check top 5 data points. 
# 
# 5. Execute the next code cell - 4 interactive boxes will appear change- discharge $Q$ and distant of observation $r$ value are known value. Change the default value in the box with your own values.
# 
# 6. Change the value of Transmissivity ($T$) and Storage coefficient ($S$) and check the fits in the graph.
# 
# 7. Step 6 should be continued until desired fit is observed in the graph.
# 
# #### Running the tool offline ####
# 
# + In the offline mode, you can use your own data (user_data.csv). You should use the sample data file provided [here:](https://prabhasyadav.github.io/iGW-I/data/user_data.csv)
# 
# + In the cell where data is put, uncomment cells with this forms #1-3. And comment out (use #) the uncommented line t_m and s_m   
# 
# + Do not change the name of the csv file **user_data.csv** and also the column titles (**Time (min)** and **Drawdown (m)** ).
# 
# + Follow steps 4-7 from above. {doc}`/contents/flow/lecture_03/13_gw_storage` 
# 
# The codes are licensed under CC by 4.0 [(use anyways, but acknowledge the original work)](https://creativecommons.org/licenses/by/4.0/deed.en)
# 

# #### Python `Libraries` Cell ####
# 
# `expi` function from `scipy.special`s that provides easy calculation of well function, and `interactive`, `widgets` and `Layout` from `ipywidget` - for interactive activities, are **special** functions used in this tool.
# 
# `numpy` for computation, `matplotlib.pyplot` for plotting and `pandas` for tabulation, are most general libraries for our works.
# 
# Please execute the cell before moving to the next step.

# In[1]:


# used library
#usual libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# specific libraries
from ipywidgets import interactive, widgets, Layout # for interactive plot with slider
from scipy.special import expi # for well function


# #### `Input Data` Cell ####
# 
# The next cell is for providing pumping data. You can change the value of variables **t_m** and **s_m**. Please do not change the name of the variable. Also, for offline mode - you have an option to upload your `.csv` data.
# 
# Make sure to execute this cell below and check the output table before moving to the next step.
# 
# (_Default data are from {doc}`/contents/tutorials/tutorial_07/tutorial_07`_)

# In[2]:


# input data must be in *.csv format. Time data must be in "min", and Drawdown in "m". 
#This can only be done in offline mode currently. Remove numbered comments #1, from below

#1 data = pd.read_csv("user_data.csv", sep = ",", usecols =["Time (min)", "Drawdown (m)"])

#2 t_m= data19.values[:,0] # extracting time data and converting to numpy array
#3 s_m= data19.values[:,1]

# You can change the data in t_m and s_m. Pls. comment if you are using offline and import your date (csv file)
t_m =np.array([1, 2,    3,    4,    5,    7,    9,   12,   18,   23,   33, 41,   56,  126,  636, 1896])
s_m = np.array([0.01, 0.03, 0.05, 0.06, 0.07, 0.09, 0.12, 0.14, 0.16, 0.17, 0.18, 0.19, 0.2 , 0.22, 0.3 , 0.32])


t_s = t_m*60 # sec- converting time to sec.

d = {'time (s)': t_s, 'drawdown (m)': s_m}
df = pd.DataFrame(data=d, index=None) 
df.head(5) # change 5 to larger number if you want to see more data in the table.


# #### The **main** ``function`` cell ####
# 
# The cell provide the main function `well_f` for running the tool. `well_f` requires 4 inputs in the order: **Transmissivity(m\u00b2/s)**, **Storage coefficient (-)**, **distance to observation well (m)**, and **discharge (m\u00b3/s)**
# 
# These value should be appropriately modified to make data fit the Type curve. 
# 
# After the cell is executed, 4 boxes with default value of the arguments will appear. You can interactively change the values in the boxes and visually see the fit. 
# 

# In[3]:


def W(u):  
    return  -expi(-u) # provides the well function

def well_f(T, S_c, r, Q): # provides the fit curve for given r and Q
    
        
    # calculated function see L07-slide 31
    u_1d = 4*T*t_s/(S_c*r**2) # calculating 1/u
    w_ud = 4*np.pi*s_m*T/Q   # well function

    # plots
    u_1 = np.logspace(10,-1,250, base=10.0)
    w_u =W(1/u_1) 
    
    plt.figure(figsize=(9,6));
    plt.loglog(u_1, w_u, label = "Type curve"); 
    plt.loglog(u_1d, w_ud, "o", color="red", label = "data")
    plt.ylim((0.1, 10));plt.xlim(1, 1e5)
    plt.grid(True, which="both",ls="-") 
    plt.ylabel(r"W(u)");plt.xlabel(r"1/u")
    plt.legend()
    
style = {'description_width': 'initial'}
layout=Layout(width='250px')
interactive_plot = interactive(well_f, 
                            T   = widgets.FloatText(value= 0.00322, description='Transmissivity  (m\u00b2/s):', disabled=False, style=style, layout=layout,), 
                            S_c = widgets.FloatText(value= 7.97e-03, description='Storage Coefficient (-):', disabled=False, style=style, layout=layout), 
                            r   = widgets.FloatText(value= 9.85, description='Obs. well location (m):', disabled=False, style=style, layout=layout), 
                            Q   = widgets.FloatText(value= 0.0025, description='Discharge (m\u00b3/s):', disabled=False, style=style, layout=layout)) 
display(interactive_plot)


# In[ ]:




