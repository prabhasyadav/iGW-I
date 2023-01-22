#!/usr/bin/env python
# coding: utf-8

# ## Simulating Effective hydraulic conductivity ## 
# 
# 
# #### How to use the tool? ####
# 
# 1. Go to the Binder by clicking the rocket button (top-right of the page)
# 2. Execute the code cell
# 3. Change the values of different quantities (layer thickness and corresponding conductivity) in the box and click the **run interact**.
# 4. For re-simulations - changes the input values in the boxes and click the "**run interact**" button. 
# 
# This tool can also be downloaded and run locally. For that download the [**_effective_K.ipynb_**](https://github.com/prabhasyadav/try1/blob/main/content/tools/effective_K.ipynb) file from the book GitHub site, and execute the process in any editor (e.g., JUPYTER notebook, JUPYTER lab) that is able to read and execute this file-type.
# 
# The codes are licensed under CC by 4.0 [(use anyways, but acknowledge the original work)](https://creativecommons.org/licenses/by/4.0/deed.en)

# In[1]:


#
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual
plt.rcParams["font.weight"] = "bold"
plt.rcParams["font.size"] = 8
import warnings
warnings.filterwarnings('ignore')


def eff_K(M1, M2, M3, K1, K2, K3):
    
    K = [K1, K2, K3]
    K_f = ["%0.2e" %elem for elem in K]
    INPUT = {"Thickness [L]": [M1, M2, M3], "Hydraulic Conductivity [L/T]": K_f}
    index = ["Layer 1", "Layer 2", "Layer 3"]
    df = pd.DataFrame(INPUT, index=index)
    tt = M1+M2 + M3  # m, totial thickness
    
    # finding relative thickness, 
    RL1, RL2, RL3 = M1/tt, M2/tt, M3/tt 
    HRL1, HRL2, HRL3 = 1/K1, 1/K2, 1/K3 
    WHK1, WHK2, WHK3 = RL1*K1, RL2*K2,RL3*K3
    WHR1,WHR2, WHR3 = RL1/K1, RL2/K2, RL3/K3 
    
    # creating intermediate table
    RL =  [RL1, RL2, RL3]
    HRL = [HRL1, HRL2, HRL3]
    WHK = [WHK1, WHK2, WHK3]
    WHR = [WHR1,WHR2, WHR3]
    RL_f = [ '%.2f' %elem for elem in RL ]
    HRL_f = [ '%.2e' %elem for elem in HRL ]
    WHK_f = [ '%.2e' %elem for elem in WHK ]
    WHR_f = [ '%.2e' %elem for elem in WHR ]
    
    index2 = ["Layer 1", "Layer 2", "Layer 3", "Sum"]
    CAL1 = {"Relative Thickness [-]":RL_f, "Hydraulic Resistance [T/L]":HRL_f,
            "Weighted Hyd. Cond. [L/T]": WHK_f, "Weighted Hyd. Resistance [T/L]": WHR_f}
    df2 = pd.DataFrame(CAL1)
    
    print("\n\n\033[1m Intermediate Calculations: \033[0m \n")
    print(df2, "\n")
    
    # calculations Parallel flow
    HR_eff = sum(WHR)
    HR_eff_a = max(WHR)

    HC_eff = 1/HR_eff
    HC_eff_a = 1/HR_eff_a
    
    RT1 = 0 
    RT2 = RT1+RL1
    RT3 = RT2+RL2
    RT4 = 1
    
    RH1 = 1
    RH2 = 1-HC_eff*WHR1
    RH3 = HC_eff*WHR3 
    RH4 = 0

      # creating data table 
    RH = [RH1, RH2, RH3, RH4]
    RH_f = ["%0.2f" %elem for elem in RH]
    RT = [RT1, RT2, RT3, RT4]
    RT_f = ["%0.2f" %elem for elem in RT] # 0.2f is for number format

    df3 = {"Relative Thickness [-]": RT_f, "Relative Head [-]": RH_f}
    df3 = pd.DataFrame(df3)
    

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_xlim(0, 1.01); ax.set_ylim(0,1.01)
    ax.xaxis.set_ticks_position('top') 
    ax.xaxis.set_label_position('top') 
    ax.set_xlabel("Relative head [-]", fontsize=12)  
    ax.set_ylabel("Relative thickness [-]", fontsize=12)  
    plt.gca().invert_yaxis()
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    ax.axhline(y=0, color='r', linewidth=2)
    ax.axhline(y=RT2, color='r', linewidth=2)
    ax.axhline(y=RT3, color='r', linewidth=2)
    ax.axhline(y=RT4, color='r', linewidth=2)
    ax.plot(RH, RT)

    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    
    print("\n\n\033[1m Parallel flow: \033[0m \n")
    
    print("The Effective Hydraulic Conductivity is: {0:0.2e}".format(HC_eff), "m/s\n")
    print("The Approximate Effective Hydraulic Conductivity is: {0:0.2e}".format(HC_eff_a), "m/s\n")
    print("The Effective Hydraulic Resistance is: {0:0.2e}".format(HR_eff), "s/m\n")
    print("The Approximate Effective Hydraulic Resistance is {0:0.2e}".format(HR_eff_a), "s/m\n")
    
    print(df3, "\n")
    plt.show(fig)
    
    # Perpendendicular flow
    
    WHK_eff = sum(WHK)
    WHK_eff_a = max(WHK)

    WHR_eff = 1/WHK_eff
    WHR_eff_a = 1/WHK_eff_a

    RD1 = WHK1/WHK_eff
    RD2 = WHK2/WHK_eff
    RD3 = WHK3/WHK_eff

    RD = [RD1, RD2, RD3]
    RD_f = ["%0.2f" %elem for elem in RD]

    df4 = pd.DataFrame({"Relative Discharge [-]": RD_f}, index= index)
    
    fig2 = plt.figure()
    plt.gca().invert_yaxis()
    ay = fig2.add_subplot(1,1,1)
    ay.barh(index, RD) 
    plt.xticks(np.arange(0, 1.1, 0.1))
    ay.set_xlabel("Relative discharge [-]", fontsize=12)
    ay.set_xlabel("Layer number", fontsize=12)
    

    
    print("\n\033[1m Perpendicular flow: \033[0m \n")
    
    print("The Effective Hydraulic Conductivity is: {0:0.2e}".format(WHK_eff), "s/m \n")
    print("The Approximate Effective Hydraulic Conductivity is {0:0.2e}".format(WHK_eff_a), "s/m\n")
    print("The Effective Hydraulic Resistance is: {0:0.2e}".format(WHR_eff), "m/s\n")
    print("The Approximate Effective Hydraulic Resistance is: {0:0.2e}".format(WHR_eff_a), "m/s\n\n")
    
    print(df4, "\n")
    plt.show(fig2)
    
style = {'description_width': 'initial'}    
Inter=widgets.interact_manual(eff_K, 
                       M1= widgets.FloatText(description="Layer Thickness 1", style=style),
                       K1= widgets.FloatText(description="Hydraulic Conductivity 1",style=style),
                       M2= widgets.FloatText(description="Layer Thickness 2", style=style),
                       K2= widgets.FloatText(description="Hydraulic Conductivity 2", style=style),
                       M3= widgets.FloatText(description="Layer Thickness 3", style=style),
                       K3= widgets.FloatText(description="Hydraulic Conductivity 3", style=style))


# In[ ]:




