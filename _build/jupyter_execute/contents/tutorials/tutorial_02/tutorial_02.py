#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import panel as pn
pn.extension("katex", "mathjax")  


# # Tutorial 2 - Aquifer and Storage Properties #
# 
# _(The contents presented in this section were re-developed principally by Dr. P. K. Yadav. The original contents are from Prof. Rudolf Liedl)_

# ### Tutorial Problem 1 ###

# In[2]:


#
r1_1 = pn.pane.Markdown("""

The park called ,,Grosser Garten'' in Dresden is underlain by an unconfined aquifer consisting of 
alluvial deposits. How much additional water is stored under the park if groundwater levels 
rise by 3 m during a wet period?
""", style={'font-size': '12pt'})

spacer = pn.Spacer(width=50) 

r1_2 = pn.pane.PNG("images/T02_TP1.png", width=500)

pn.Row(r1_1,spacer, r1_2)


# In[3]:


#
r1_3 = pn.pane.Markdown("""

### Tutorial Problem 1 – Solution ###


**For details check lecture slide: L02- 8**
<br><br>

The basic configuration of an unconfined aquifer:

""", style={'font-size': '12pt'})

spacer = pn.Spacer(width=50) 

r1_4 = pn.pane.PNG("images/T02_TP1_2.png", width=600)

pn.Row(r1_3,spacer, r1_4)  


#<img src="images/T01_TP1_2.PNG" alt="Grosser Garten Map"  width="100%" height="100%" > 


# In[4]:


# The given information of the problem are

L = 2 # km as length of garten
W = 1 # km as Width of garten
DP = 3 # m change in pressure head
n = 0.3 # porosity that we assume to be 30%
A = L * W *1e6 # m^2, Area unit convered.
DV = A * DP # m^3, increase in total volume due to change in pressure head
AW = n * DV # m^3, additional Water volumne

print("Park Area is {0:1.1f}".format(A),"m\u00b2")  
print("Increase in total volume: {0:1.1E}".format(DV),"m\u00b3") 
print("Additional water volume: {0:1.1E}".format(AW),"m\u00b3") 


# ### Tutorial Problem 2 ###

# In[5]:


#
r2_1 = pn.pane.Markdown("""
The lithological information derived from three boreholes is given in the figure below.
Try to correlate the layers to obtain a 2D cross section of the subsurface structure.
""", style={'font-size': '12pt'})

r2_2 = pn.pane.PNG("images/T02_TP2_1.png", width=400)

r2_3 = pn.pane.Markdown("""
### Tutorial Problem 2 – Solution ###

**For details check lecture slide: L03-15**.<br>

Few correlations between the layers are presented in the figure below:
""", style={'font-size': '12pt'})

R1 = pn.Row(r2_1, r2_2) 
pn.Column(R1, r2_3)


# In[6]:


# SOlution 2

img_1 = pn.pane.PNG("images/T02_TP2_1.png", width=500)
img_2 = pn.pane.PNG("images/T02_TP2_2.png", width=300)
img_3 = pn.pane.PNG("images/T02_TP2_3.png", width=300)
img_4 = pn.pane.PNG("images/T02_TP2_4.png", width=300)

tabs = pn.Tabs(('Sample', img_1), ("Solution 1", img_2), ("Solution 2", img_3), ("Solution 3", img_4))
tabs


# ### Tutotorial Problem 3 ###

# In[7]:


r3_1 = pn.pane.Markdown("""

This problem addresses a confined aquifer with a thickness of 61 m and a specific storage of 
1.2 X 10<sup>-5</sup> 1/m. Due to water injection the pressure head rises by 0.75 m on average over an area 230 m in diameter.
How much water is injected?

""", width=950, style={'font-size': '12pt'}) 

r3_2 = pn.pane.Markdown("""
### Tutorial Problem 3 – Solution ###

**For details check lecture slide: L03-28** <br><br>

Basic configuration of a confined aquifer:
<br><br>
""", style={'font-size': '12pt'})

r3_3 = pn.pane.PNG("images/T02_TP3.png", width=600)

r3_4= pn.pane.LaTeX(r"""
specific storage: <br> $S_s = \frac{\Delta V_w}{V_T \cdot \Delta \psi } $ <br>
with <br>
$\Delta V_w$ = change in water volume [L$^3$] <br>
$V_T$ = total volume [L$^3$]<br>
$\Delta \psi$ = change in pressure head [L]
""", style={'font-size': '12pt'}) 

r3_5 = pn.Row(r3_3, r3_4)
pn.Column(r3_1, r3_2, r3_5)   


# In[8]:


# Given data
d = 230 # m,  diameter of the aquifer
m = 61 # m, thickness of the aquifer
Ss = 1.2 * 10e-5 # 1/m, specific storage
DP_h = 0.75 # m, pressure head difference

# Calculations

A = np.pi *(d/2)**2 # m^2, area of the aquifer
Vt = A*m # m^3 Total volume of the aquifer
DV_w = Ss*Vt*DP_h # m^3, additional water volume

print("The Aquifer Area is {0:1.2E}".format(A),"m\u00b2") 
print("The Total Volume is {0:1.2E}".format(Vt),"m\u00b3") 
print("The Additional Water is {0:1.2f}".format(DV_w),"m\u00b3")   


# ### Tutorial Problem 4:  ###

# In[9]:


# Tut Problem 4
rx_1 = pn.pane.Markdown("""
We consider an unconfined aquifer with a storage coefficient of 0.19. What will be the change
in water volume if the following drawdowns are observed in four sub-areas in a dry period:
""", width = 700, style={'font-size': '12pt'})
rx_1


# In[10]:


#
Head = ["Sub-Area", "Size, (Km2)", "drawdown (m)", "Change in water volume (m3)"]
Sub_Area = ["A", "B", "C", "D"] #name 
Size = [36, 18, 72, 85] # km^2, area
Drawdown = [0.85, 1.09, 1.65, 2.37] # m, equivalent to change in pressure head
Q4t = np.transpose([Sub_Area, Size, Drawdown])

data = {"Sub-Area": Sub_Area, "Size, (Km2)": Size, "drawdown (m)": Drawdown, }
df1= pd.DataFrame(data)
df1.set_index('Sub-Area')


# ### Tutorial Problem 4 – Solution ###
# 
# **For details check lecture slides L03 - 28, 29 and 31**
# 
# In unconfined aquifer Stortavity ($S$) is used instead of storage coefficient $S_s$. They both are related with thickness ($m$) as:
# 
# $$
# S = S_s \times m
# $$
# and so in unconfined aquifer, we get:
# 
# $$S = \frac{\Delta V_w}{A \cdot \Delta \psi } $$
# 
# with <br>
# $\Delta V_w$ = change in water volume [L$^3$³] <br>
# $A$ = Domain area [L$^2$]<br>
# $\Delta \psi$ = change in pressure head [L]

# In[11]:


# Given information
s = 0.19 
Size = [50, 18, 72, 85] # km^2, area
Drawdown = [0.85, 1.09, 1.65, 2.37] # m, equivalent to change in pressure head

# Solution part
Vol_cha = s*np.multiply(Size, Drawdown)*10**6 # m^3, vol change = s*area size * drawdawn

# output printing
data2 = {"Sub-Area": Sub_Area, "Size, (Km2)": Size, "drawdown (m)": Drawdown, "Change in volume (Km3)":Vol_cha/1e9  }
df2= pd.DataFrame(data2)
df3= df2.set_index('Sub-Area')

print(df3, "\n")
print("The total change in the volume of water is: {0:0.3f} Km\u00b3".format(sum(Vol_cha/1e9)))


# ### Tutorial Problem 5:  ###
# 
# A confined aquifer is considered in this problem. Specific storage and total porosity equal $7.5\times 10^{-6}$ 1/m and 30%, respectively. 
# What is the compressibility of the porous medium? (compressibility of water: $4.6\times 10^{-10}$ m$^2$/N, density of water: 998 kg/m$^3$)
# 
# ### Tutorial Problem 5 – Solution ###
# 
# **For details check slide nr. L03-28**
# 
# Specific Storage, 
# 
# $$S_s = (n\alpha_w + \alpha_{pm})\rho_w g$$
# 
# with: $n$ = Total porosity [-]<br>
# $g$ = acceleration due to gravity [L/T$^2$] <br>
# $\alpha_w$ = compressibility of water [LT$^2$/M]   <br> 
# $\alpha_{pm}$ =	compressibility of porous 	medium [LT$^2$/M]<br> 
# $\rho_w$ = density of water [M/L$^3$]
# 
# Solve for $\alpha_{pm}$: $\frac{S_s}{\rho_w g} -n\alpha_w = \alpha_{pm}$

# In[12]:


# Given data
 
n = 0.3 # unitless, total porosity
rho_w = 998 # kg/m3, density of water
g = 9.81 # m/s2, accl. due to gravity
alpha_w = 4.6*1e-10 # m2/N, compressibility of water
S_s = 7.5*1e-6 # 1/m, specific storage 

# calculated land subsidence (LS)
alpha_pm5 = S_s/(rho_w*g) - n*alpha_w

print("The Compressibility of Porous mdeid is {0:0.2E}".format(alpha_pm5), "m\u00b2/N")


# ### Tutorial Problem 6:  ###
# 
# Due to water extraction from a confined aquifer the pressure head is
# lowered by 183 m. The following aquifer parameters are available: storage
# coefficient = $5\times10^{-4}$, total porosity = 0.33, thickness (before water
# extraction) = 80 m, compressibility of the porous medium = $6.9\times 10^{-8}$ m²/N and the density of water is 998 kg/m$^3$
# 
# What is the amount of land subsidence resulting from the water extraction?

# ### Tutorial Problem 6 – Solution ###
# 
# **For details see slide nr. L03-25 and 26**<br>
# 
# Change in total volume due to $\Delta p_{pm}$ :
# 
# $$ \Delta V_T = \alpha_{pm} V_T\rho_w g \Delta \psi $$ 
# <br>
# with:
# 
# $\alpha_{pm}$ =	compressibility of porous medium [LT$^2$/M] <br>    
# $V_T$ = total volume [L$^3$] <br>                 $\rho_w$ = density of water [M/L$^3$] <br>         $g$ = acceleration of gravity [L/T$^2$] <br>       $\Delta \psi$ = change in pressure head [L]
# 
# $\Delta V_T = A\times\Delta m$ and <br>
# $V_T = A\times m$ and <br>
# with $A$ = area of the aquifer [L/T$^2$] and <br> 
# $m$ = Thickness of the aquifer [L].
# Substituting these relation in the above equation we get:
# 
# $$ \Delta m = \alpha_{pm} m\rho_w g \Delta \psi $$ 
# <br>

# In[13]:


# Given data
alpha_pm = 6.9 * 1e-8 # m2/N, compressibility of porous medium 
m = 80 # m, thickness
rho_w = 998 # kg/m3, density of water
g = 9.81 # m/s2, accl. due to gravity
DP_h = 30 # m, change in pressure head

# calculated land subsidence (LS)
LS = alpha_pm*m*rho_w*g*DP_h

print("The land subsidence is {0:0.2f}".format(LS), "m")


# ## HOME WORK PROBLEMS ##
# 
# ### Homework Problem 1 ###
# 
# The pressure head in an aquifer extending over 200 km$^2$ is decreased by 1.60 m.
# Determine the loss of groundwater in the aquifer for two scenarios:
#   The aquifer is unconfined (storage coefficient 0.13).
#   The aquifer is confined (storage coefficient 0.0005).

# 
# ### Homework Problem 2 ###
# 
# Conduct a sieve analysis for a dried soil sample (see data in the table below)
# 
# 1. Draw the granulometric curve (cumulative mass distribution) and briefly characterise the sediment with regard to its major constituent(s).
# 2. What is the coefficient of uniformity?

# In[14]:


#
Head = ["mesh size [mm]", "residue in the sieve [g] ", "∑ total", "∑ / ∑total"]
Size = [6.3, 2, 0.63, 0.2, 0.063, "< 0.063 /cup"]
residue = [11, 62, 288, 189, 42, 8]


data3 = {"mesh size [mm]": Size, "residue in the sieve [g] ": residue}
df4= pd.DataFrame(data3)
df4.set_index("mesh size [mm]")


# In[ ]:




