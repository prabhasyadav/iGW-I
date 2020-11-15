#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import panel as pn
pn.extension("katex") 


# # Tutorial 3 #
# 
# + **tutorial problems on Darcy's law and intrinsic permeability**
# 
# 
# + **homework problems on Darcy's law and intrinsic permeability**
# 
# 
# 
# ### Tutorial Problems on ###
# 
# + Darcy's Law and 
# + Intrinsic Permeability

# ### Tutorial Problem 7: Flow Direction and Hydraulic Gradient
# 
# Indicate the direction of flow shown in the figure in next slides, and determine the hydraulic gradient for a Darcy column with length L = 50 cm! (Figures not to scale.)
# 
# #### Tutorial Problem 7 – Solution ####
# 
# **The relevant topic is covered in Lecture 04, slide 8**
# 

# In[8]:


png_pane = pn.pane.PNG("images/T02_TP7_a1.png", width=600)
png_pane


# In[9]:


# Image (a)
L = 0.5 # m, length of the column
Ea_hl = 0.2 #, m, elevation head, left 
Pa_hl = 0.1 #, m  pressure head, left
Ea_hr = 0.2 #, m, elevation head, right
Pa_hr = 0.3 #, m  pressure head, right
Ha_hl = Ea_hl + Pa_hl # m, hydraulic head, left
Ha_hr = Ea_hr + Pa_hr # m, hydraulic head, right
DH_a = Ha_hr - Ha_hl
H_ga = DH_a/L#, no unit, hydraulic gradient 

print("Hydraulic head LEFT: {0:1.1f}".format(Ha_hl),"m"); print("Hydraulic head RIGHT:: {0:1.1f}".format(Ha_hr),"m") 
print("Hydraulic Head Difference: {0:1.1f}".format(DH_a),"m");print("Hydraulic gradient: {0:1.1f}".format(H_ga)) 
png_pane.object = "images/T02_TP7_a2.png" 


# In[10]:


png_pane2 = pn.pane.PNG("images/T02_TP7_b1.png", width=500)
png_pane2 


# In[11]:


# Image (b)
L = 0.5 # m, length of the column
Eb_hl = 0.2 #, m, elevation head, left 
Pb_hl = 0.1 #, m  pressure head, left
Eb_hr = 0.05 #, m, elevation head, right
Pb_hr = 1.3 #, m  pressure head, right
Hb_hl = Eb_hl + Pb_hl # m, hydraulic head, left
Hb_hr = Eb_hr + Pb_hr # m, hydraulic head, right
DH_b = Hb_hr - Hb_hl
H_gb = DH_b/L#, no unit, hydraulic gradient 
print("Hydraulic head LEFT: {0:1.1f}".format(Hb_hl),"m");print("Hydraulic head RIGHT:: {0:1.1f}".format(Hb_hr),"m") 
print("Hydraulic Head Difference: {0:1.1f}".format(DH_b),"m");print("Hydraulic gradient: {0:1.1f}".format(H_gb)) 
png_pane2.object = "images/T02_TP7_b2.png" 


# In[12]:


png_pane3 = pn.pane.PNG("images/T02_TP7_c1.png", width=400)
png_pane3 


# In[13]:


# Image (c)
L = 0.5 # m, length of the column
Ec_hl = 0.3 #, m, elevation head, left 
Pc_hl = 0.1 #, m  pressure head, left
Ec_hr = 0.2 #, m, elevation head, right
Pc_hr = 0.2 #, m  pressure head, right
Hc_hl = Ec_hl + Pc_hl # m, hydraulic head, left
Hc_hr = Ec_hr + Pc_hr # m, hydraulic head, right
DH_c = Hc_hr - Hc_hl
H_gc = DH_c/L#, no unit, hydraulic gradient 
print("Hydraulic head LEFT: {0:1.1f}".format(Hc_hl),"m");print("Hydraulic head RIGHT:: {0:1.1f}".format(Hc_hr),"m") 
print("Hydraulic Head Difference: {0:1.1f}".format(DH_c),"m");print("Hydraulic gradient: {0:1.1f}".format(H_gc)) 
png_pane3.object = "images/T02_TP7_c2.png" 


# In[14]:


png_pane4 = pn.pane.PNG("images/T02_TP7_d1.png", width=400)
png_pane4 


# In[15]:


# Image (d)
L = 0.5 # m, length of the column
Ed_hl = 0.3 #, m, elevation head, left 
Pd_hl = 0.1 #, m  pressure head, left
Ed_hr = 0.2 #, m, elevation head, right
Pd_hr = 0.1 #, m  pressure head, right
Hd_hl = Ed_hl + Pd_hl # m, hydraulic head, left
Hd_hr = Ed_hr + Pd_hr # m, hydraulic head, right
DH_d = Hd_hr - Hd_hl
H_gd = DH_d/L#, no unit, hydraulic gradient 
#output
print("Hydraulic head LEFT: {0:1.1f}".format(Hd_hl),"m");print("Hydraulic head Right:: {0:1.1f}".format(Hd_hr),"m") 
print("Hydraulic Head Difference: {0:1.1f}".format(DH_d),"m");print("Hydraulic gradient: {0:1.1f}".format(H_gd)) 
png_pane4.object = "images/T02_TP7_d2.png" 


# ### Tutorial Problem 8  ###

# The hydraulic conductivity of a fine sand sample was found to be equal to $1.36\times 10^{-5}$ m/s in a Darcy experiment using water at a temperature of $20^\circ$C. What is the intrinsic permeability of this sample? Give results in cm$^2$ and D.
# (density of water at $20^\circ$C: 998.2 kg/m$^3$; dynamic viscosity of water at $20^\circ$C: $1.0087 \times 10^{-3}$ Pa$\cdot$s;  1 D = $0.987\times 10^{-12}$ m$^2$) 
# 
# #### Tutorial Problem 8  - Solution ####
# 
# **Relevant topics are covered in Lecture 04 slides 18-20.**
# 
# Relationship between hydraulic conductivity $K$ and intrinsic permeability $k$ from lecture notes:
# $$
# K_{water} = k\cdot \frac{\rho_{water}\cdot g}{\eta_{water}}
# $$
# 
# Solve for , $k$
# 
# $$
# k = \frac{\eta_{water}\cdot K_{water}}{\rho_{water}\cdot g}{}
# $$

# In[16]:


#Given
Darcy = 0.987 * 10**-12 # m^2, 1D = 0.987*10^-12 m^2 
nu_w = 1.00087*10**-3 # Pa-S dynamic viscosity of water
K_w = 1.36*10**-5 # m/s Conductivity of water
g = 9.81 # m/s^2 accln due to gravity
rho_w = 998.2 # kg/m^3, density of water

# Solution
k = (nu_w*K_w)/(rho_w*g)#, m^2, permeability of water
k_D = k/Darcy


print("The permeability is {0:1.1E}".format(k),"m\u00b2")  
print("The permeability in Darcy unite is: {0:1.2f}".format(k_D),"D") 


# ### Tutorial Problem 9: Constant-Head Permeameter ###

# In[17]:


## Tutorial Problem 9: Constant-Head Permeameter

r1 = pn.pane.LaTeX(r"""
(a). Derive the expression for $K$ given below.
$$
K = \frac{QL}{A(h_{in}-h_{out})}
$$

(b). The hydraulic conductivity of a medium sand sample (length 15 cm, 
cross-sectional area 25 cm$^2$) is to be determined. The hydraulic head 
difference is 5 cm and a water volume of 100 cm³ pas-sed the sample during 
an experimental period of 12 min.
<br><br>

(c). How long would 100 cm$^3$ diesel (density: 0.85 g/cm$^3$, dynamic viscosity: 3.5$\cdot 10^{-3}$ 
Pa$\cdot$s at 20$^\circ$C) need to pass the sample under a head difference of 5 cm (density and 
dynamic viscosity of water at 20$^\circ$C: 998.2 kg/m$^3$ and 1.0087$\cdot 10^{-3}$ Pa$\cdot$s, resp.)?
""", width=450, style={'font-size': '12pt'}) 
spacer = pn.Spacer(width=100)

r2 =pn.pane.PNG("images/T02_TP9.png", width=400) 

pn.Row(r1,spacer, r2) 


# In[18]:


### Tutorial Problem 9 – Solution ###

r1 = pn.pane.LaTeX(r""" Solution Problem 9: <br>

The relevant topic can be found in lecture 04, slides 15, 18-20
<br><br>

Let the reference datum be at the bottom. Then from Darcy's Law:
$$Q= -A\cdot K\frac{h_{out}-h_{in}}{L}$$
With,


Q = discharge [L$^3$/T]<br> 
L =column length [L]<br>
A = cross-sectional area of column [L$^2$]<br>
K = hydraulic conductivity [L/T]<br>
h$_{in}$ =hydraulic head at column inlet [L]<br>
h$_{out}$ = hydraulic head at column outlet [L]<br>
<br>
Solve for $K$:
$$
K= \frac{Q\cdot L}{A\cdot(h_{in}-h_{out})}
$$

If the reference level $(z = 0)$ is located at the downgradient overflow, then set $h_{out} = 0$.
""", width= 500, style={'font-size': '13pt'} ) 
spacer = pn.Spacer(width=100)

r2 =pn.pane.PNG("images/T02_TP9a.png", width=300) 

pn.Row(r1,spacer, r2, width=1000)    


# In[19]:


#Given (solution on 9b)
L = 15 #cm, length of column
A = 25 # cm^2, surface area of column
h_diff = 5 # cm, h_in-h_out
Q = 100/12 # cm^3/min discharge per min

# Solution using derived equation in first part of the problem
# K = QL/A(h_in- h_out)

K = (Q*L)/(A*h_diff)# cm/min, required conductivity 
K_1 = K*10**-2/60 #, m/s, conductivity in m/s

#output
print("The conductivity in column is {0:1.2E}".format(K),"cm/min") 
print("The conductivity in column is {0:1.2E}".format(K_1),"m/s \n") 

if K_1 <= 1.67*10**-4:
    print("Fine to medium sand")
else:
    print("to check further") # to be completed later.


# Continue solution on 9c
# 
# Discharge and Darcy's law: $Q_{water} = \frac{V}{t_{water}}=-A\cdot K_{water}\cdot\frac{\Delta h}{L}$
# 
# Solve for $t_{water}$:   $t_{water} = \frac{V}{Q_{water}}=-\frac{V}{A\cdot K_{water}\cdot\Delta h/L} = -\frac{V\cdot L}{A\cdot K_{water}\cdot\Delta h}$
# 
# Same step for $t_{diesel}$:   $t_{diesel}  = -\frac{V\cdot L}{A\cdot K_{diesel}\cdot\Delta h}$
# 
# 
# 
# time ratio:$\frac{t_{diesel}}{t_{water}} = \frac{-\frac{V\cdot L}{A\cdot K_{diesel}\cdot\Delta h}}{-\frac{V\cdot L}{A\cdot K_{water}\cdot\Delta h}} = \frac{K_{water}}{K_{diesel}}$
# 
# Use relationship between conductivity $K$ and permeability $k$ from lecture notes (slides 18)
# $$\frac{K_{water}}{K_{diesel}} = \frac{k\cdot \frac{\rho_{water}\cdot g}{\eta_{water}}}{k\cdot \frac{\rho_{diesel}\cdot g}{\eta_{diesel}}} = \frac{\rho_{water}\cdot\eta_{diesel}}{\rho_{diesel}\cdot\eta_{water}}$$
# 
# Solve for $t_{diesel}$
#  

# In[20]:


# Given data

rho_w = 920.2 # kg/m^3, density of water at 20°C
eta_w = 1.0087*10**-3#, Pa-S dynamic viscosity of water
rho_d = 0.85 # g/cm^3, density of diesel at 20°C
eta_d = 3.5*10**-3#, Pa-S dynamic viscosity of diesel
V_d = 100 # cm^3 volume of diesel
t_w = 12 # min, time taken by water

# Calculations

t_d = (rho_w*eta_d)/(rho_d*1000*eta_w)*t_w 

# multiplied by 1000 to convert unit g/cm^3 to kg/m^3

print("The time required for diesel will be: {0:0.2f}".format(t_d), "min") 


# ### Tutorial Problem 10: Falling-Head Permeameter ###

# In[21]:


# Tutorial Problem 10

r10_1 = pn.pane.LaTeX(r"""
$$
K = \frac{d_t^2 L}{d_c^2 L}\cdot \ln\frac{h_{in}(0)-h_{out}}{h_{in}(t)-h_{out}}
$$
""", width=400, style={'font-size': '12pt'})

r10_2 = pn.pane.Markdown("""
1. Derive the expression for K given above.
<br><br>
2. The hydraulic conductivity of a fine sand sample (length 15 cm, diameter 10 cm) is to be determined. 
The hydraulic head difference at the beginning and at the end of the experiment after 528 min is 5 cm and 0.5 cm, resp. 
The inner tube diameter is 2 cm. 

""", width= 500, style={'font-size': '12pt'})

r10_2a = pn.pane.Markdown("""
### Tutorial Problem 10: Solution ###
<br>
**Relevant information can be found in Lecture 04, Slides 14 and 16**
""", width= 500, style={'font-size': '12pt'})

col1 = pn.Column(r10_1, r10_2, r10_2a)

r10_3 =pn.pane.PNG("images/T02_TP10.png", width=350)
spacer3 = pn.Spacer(width=50) 
pn.Row(col1, spacer3, r10_3) 


# In[22]:


# Tutorial Problem 10: Solution

r10_a1 = pn.pane.LaTeX(r"""
Darcy's Law:
$$
Q(t) = -A_c \cdot K\cdot\frac{h_{out} - h_{in}(t)}{L} 
$$

Volumetric budget for standpipe:
$$
Q(t) = -\frac{dV_t}{dt}(t) = -A_t \cdot \frac{dh_{in}}{dt}(t) 
$$
with <br> 
$A_t$ = cross-sectional area of standpipe [L$^2$]<br>
$V_t$ = water volume in standpipe [L$^3$]<br>
<br>
combine Darcy's law and the volumetric budget:
$$
-A_t \cdot \frac{dh_{in}}{dt}(t) =  -A_c \cdot K\cdot\frac{h_{out} - h_{in}(t)}{L}
$$

solve for $dh_{in}/dt$:
$$
\frac{dh_{in}}{dt} = \frac{K}{L}\frac{A_c}{A_t}(h_{out}-h_{in}) = \frac{K}{L}\bigg(\frac{d_c}{d_t}\bigg)^2(h_{out}-h_{in})
$$

""", style={'font-size': '13pt'})
r10_a2 =pn.pane.PNG("images/T02_TP10.png", width=300)


pn.Row(r10_a1, r10_a2) 


# In[23]:


#
r10_a3 = pn.pane.LaTeX(r"""
Equation for falling head: $ \frac{dh_{in}}{dt}  = \frac{K}{L}\big(\frac{d_c}{d_t}\big)^2(h_{out}-h_{in}) $
<br> <br>
This equation is an ordinary differential equation of first order. 
Providing hydraulic head $h_{in}(0)$ at the beginning of the experiment $(t = 0)$, it 
may be solved by separation of variables:
$$
\frac{dh_{in}}{h_{out}-h_{in}} = \frac{K}{L}\bigg(\frac{d_c}{d_t}\bigg)^2 dt
$$
integrations on both sides by considering the initial condition:
$$
\int_{h_{in}(0)}^{h_{in}(t)}\frac{dh_{in}}{h_{out}-h_{in}} = \int_0^t \frac{K}{L}\bigg(\frac{d_c}{d_t}\bigg)^2 dt = \frac{K}{L}\bigg(\frac{d_c}{d_t}\bigg)^2 \int_0^t dt
$$
determine integral functions:
$$
\Bigg[-\ln(h_{out} - h_{in}) \Bigg]_{h_{in}(0)}^{h_{in}(t)} = \frac{K}{L}\bigg(\frac{d_c}{d_t}\bigg)^2 [t]_0^t 
$$ 
insert limits of integration:
$$
-\ln\frac{h_{out}-h_{in}(t)}{h_{out}-h_{in}(0)} = \frac{K}{L}\bigg(\frac{d_c}{d_t}\bigg)^2 t 
$$
solve for K:
$$
K = \bigg(\frac{d_c}{d_t}\bigg)^2 \frac{L}{t}\ln\frac{h_{in}(0)-h_{out}}{h_{in}(t)-h_{out}}
$$
""", width=600, style={'font-size': '12pt'})
r10_a3


# In[24]:


# Given

L = 15 # cm, length
L_m = L/100 # m, length
d_c = 10 # cm, diameter column
d_t = 2 # cm, diameter tube
h_d0 = 5 # cm, head difference at start
h_dt = 0.5 # cm, head difference at time t
t = 528 # min, total time  
t_s = 528*60 # sec, total time in seconds

#solution using the developed equation 

K = (d_t/d_c)**2 * ((L_m)/t_s)*np.log(h_d0/h_dt)

#Output
print("The conductivity in column is {0:1.2E}".format(K),"m/s \n") 

if K < 1.67*10**-5:
    print("Silt or silty sand")
else:
    print("to check further") # to be completed later.


# ### HOME WORK PROBLEMS ###
# 
# 
# **Darcy's Law and Intrinsic Permeability**
# 
# _There is no obligation to solve homework problems!_
# 
# **Try to submit within next 2 weeks.**
# 
# 
# 
# 
# 

# In[28]:


#
r_h3a = pn.pane.Markdown("""
### Homework Problem 3 ###


**A**. Derive an expression for hydraulic conductivity *_K_* for the constant-head permeameter shown in the figure.<br><br>
**B**. The hydraulic conductivity of a sample (length 10 cm, diameter 4 cm) is to be determined. 
The water depths a<sub>1</sub> and a<sub>2</sub> equal 6 cm and 3 cm, resp. A water volume of 250 ml passed the sample during an experimental period of 36 s. <br> <br>
**C**. Which material could be contained in the sample?
""", width = 400, style={'font-size': '12pt'})
spacer2=pn.Spacer(width=50)

r_h3b = pn.pane.PNG("images/T02_TH3.png", width=500)

pn.Row(r_h3a,spacer2, r_h3b) 


# 
# ### Homework Problem 4 ###
# 
# 

# In[26]:


#
r_h4 = pn.pane.Markdown("""
A Darcy experiment is performed by a falling-head permeameter using water at 20°C. 
Length and diameter of the sample are 20 cm and 6 cm, resp. The inner tube diameter is 4 cm. 
The following data are available for the time-dependent hydraulic head difference : 
""", style={'font-size': '12pt'})

r_h4b = pn.pane.PNG("images/T02_TH4a.png", width=400)

r_h4c = pn.pane.Markdown("""
**A.** Convert times to seconds and plot the logarithm of the ratios of head differences ln(Δh(0)/Δh(t)) vs. time t. 
(Use the coordinate system on next page). <br><br>
**B.** Determine the slope of the corresponding regression line.<br><br>
**C.** Determine hydraulic conductivity K.<br><br>
**D.** Determine intrinsic permeability k.<br>

""", style={'font-size': '12pt'})
r_h4d = pn.Column(r_h4, r_h4b, r_h4c)
r_h4e = pn.pane.PNG("images/T02_TP10.png", width=400)
spacer2=pn.Spacer(width=50)
pn.Row(r_h4d, spacer2, r_h4e) 


# In[27]:


#
fig, ax = plt.subplots(figsize=(8, 6))  
plt.grid(axis='y', linestyle='--')   
plt.xlim((0, 1800)); plt.ylim((0,0.7)) 
plt.xlabel("t(s)", fontsize=12 )
plt.ylabel(r"ln($\Delta h(0)/\Delta h(t)$)(-)", fontsize=12); 

