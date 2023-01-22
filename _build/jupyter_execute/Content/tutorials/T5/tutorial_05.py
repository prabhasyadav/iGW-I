#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import panel as pn
pn.extension('katex', 'mathjax') 


# # Aquifer Heterogeneity/Anisotropy
# 

# ### Tutorial Problem 12: Hydrologic Triangle

# In[2]:


r6_1 = pn.pane.Markdown("""
The figure below shows the position of four groundwater observation wells with measured hydraulic heads in m a.s.l. 
<br> <br>
**a.** Sketch head isolines for intervals of 1 m by applying the hydrologic triangle method.<br><br>
**b.** Indicate the flow direction.

""",width = 400, style={'font-size': '13pt'})

r6_2 = pn.pane.PNG("images/T05_TP12_a.png", width=400) 

spacer2 = pn.Spacer(width=100)


pn.Row(r6_1,spacer2, r6_2) 


# ### Solution of Tutotrial Problem 12
# 
# The following 4 steps are to be performed:
# 
# - **Step I**   : Connects all the points
# - **Step II**  : Divide the connected lines at equal head-level (here = 1 m)
# - **Step III** : Join all the equal head lines 
# - **Step IV**  : Mark the flow direction from higher head towards lower head

# In[3]:


# solution Tutorial problem 12
img_0 = pn.pane.PNG("images/T05_TP12_a.png", width=400)
img_1 = pn.pane.PNG("images/T05_TP12_b.png", width=500)
img_2 = pn.pane.PNG("images/T05_TP12_c.png", width=500)
img_3 = pn.pane.PNG("images/T05_TP12_d.png", width=500)
img_4 = pn.pane.PNG("images/T05_TP12_e.png", width=700)

tabs = pn.Tabs(('Given Head values', img_0), ('Step I: Connects points', img_1), ("Step II: Divide line", img_2), ("Step III: Join lines", img_3), ("Step IV: Mark flow direction", img_4))
tabs


# ### Tutorial Problem 13: Flow Nets ###

# In[4]:


#
r7_1 = pn.pane.Markdown("""


Sketch head isolines and streamlines for the two configurations a) and b) of a well doublette shown below. In both cases flow nets should be sketched without and with the uniform flow component.

""",width=800,  style={'font-size': '13pt'})

r7_2 = pn.pane.Markdown("""
 a) withdrawal at both wells:<br><br><br>
""",width=400,  style={'font-size': '13pt'})

r7_3 = pn.pane.PNG("images/T05_TP13_a.png", width=200)  

r7_4 = pn.Column(r7_2,r7_3)

r7_5 = pn.pane.Markdown("""
 b) Injection and withdrawl wells:<br><br><br>
""",width=400,  style={'font-size': '13pt'})

r7_6 = pn.pane.PNG("images/T05_TP13_b.png", width=200)  

spacer3 = pn.Spacer(width=200)

r7_7 = pn.Column( r7_5, r7_6)
r7_8 = pn.Row(r7_4, spacer3 , r7_7) 
pn.Column(r7_1,  r7_8) 


# ### Solution of Tutorial Problem ###
# 
# This is to be sketched and demonstrated.

# ### Tutorial Problem 14 (special topic) ###
# 
# From the laboratory test the degree of saturation($\theta$) of the unsaturated core (temperature = 9$^\circ C$) sample was
# found to be 30% and relative permeability ($k_r$) is assumed to be 0.1.  From the grain analysis the sample was determined to be predominantly 
# medium sand (intrinsic permeability, $k = 1.61 \times 10^{-7}$ cm$^2$). Provided that density ($\rho$) and dynamic 
# viscosity of water ($\mu$) at 9$^\circ C$ is 999.73 kg/m$^3$ and 0.0013465 N$\cdot$s/m$^2$ respectively, find the conductivity of the 
# sample. What will be the conductivity of the same sample when the moisture content is 1% ($k_r \approx 0.001$) and 80% ($k_r \approx 0.4$). Explain the effect of moisture content on the sample.
# 
# ### Solution of Tutorial Problem 14 ###
# 
# **Lecture contents on the topic in L02- slides 02, 22 & 26**
# 
# Hydraulic conductivity of the unsaturated sample ($\theta < 100\%$) can be obtained from the following expression:
# 
# $$
# K(\theta) = \bigg(\frac{k\rho g}{\mu}\bigg)k_r(\theta)
# $$

# In[5]:


# Given 
kr_30  = 0.1 # (-), relative permeability for moist. cont. 30%
i_p = 1.61 * 10**-7 # cm^2, intrinsic permeability
rho = 999.73 # kg/m^3, Sample density
mu = 0.0013467 #  N-s/m^2, dynamic visc.
g_c = 9.81 # N/kg, force unit used for gravitational constant

# Solutions 1
i_pm = i_p/10000 # m^2 unit conversion for int. permeab.
K_30 = (i_p*rho*g_c/mu)*kr_30

# Solution 2  when moisture content is 1% and 80%
kr_1 = 0.001 # (-), relative permeability for moist. cont. 1%
kr_80 = 0.4 # (-), relative permeability for moist. cont. 80%
K_1 = (i_p*rho*g_c/mu)*kr_1
K_80 = (i_p*rho*g_c/mu)*kr_80

# output

print("The conductivity of water when moisture content is 30%  is: {0:1.1e}".format(K_30),"m/s \n")
print("The conductivity of water when moisture content is 1%  is: {0:1.1e}".format(K_1),"m/s \n")
print("The conductivity of water when moisture content is 80%  is: {0:1.1e}".format(K_80),"m/s \n")
print("The conductivity of media increases very rapidly with increase of moisture content")


# ### Tutorial Problem 15 ###

# In[6]:


r2_2 = pn.pane.LaTeX(r"""

From the analysis of laboratory results the unsaturated hydraulic conductivity fits the following exponential 
model as a function of pressure head ($\psi$): $K(\psi) = K_s \exp(\alpha\cdot \psi)$, 
with $K_s$ [LT$^{-1}$] the saturated hydraulic conductivity and $\alpha$ [L$^{-1}$] a fit parameter. 
For the pressure head measurements and the data provided in the figure below, find $K(\psi)$. 
Also, find the Darcy velocity for this case.
""", width = 900, style={'font-size': '13pt'}) 

r2_3 =pn.pane.PNG("images/T05_TP15.png", width=400)


pn.Column(r2_2, r2_3) 


# ### Solution Tutorial Problem 15 ###

# In[7]:


# Given

K_s = 2 # cm/d # saturated conductivity
al_a = 0.04 # 1/cm, fit constant
Ph_a = -100 # cm, pressure head at A
Ph_b = -90 # cm, pressure head at B
Z_a = 300 # cm, elevation head at A from datum
Z_b = 200 # cm, elevation head at B from datum

# Solution 1 
Ph_m = (Ph_a+Ph_b)/2 # mean pressure head
K_psi = K_s*np.exp(al_a*Ph_m) # cm/d, from the given model

#Solution 2
H_A = Ph_a+Z_a # cm, hydraulic head at A
H_B = Ph_b+Z_b # cm, hydraulic head at B
dh_dz = (H_B - H_A)/(Z_b - Z_a) # (-), hydraulic head gradient
q_z = -K_psi*dh_dz # cm/d, Darcy velocity 

print("The unsaturated conductiviy of the sample is: {0:1.3f}".format(K_psi), "cm/d\n")
print("The Darcy velocity is: {0:1.3f}".format(q_z), "cm/d\n") 
print("The negative sign indicates the direction opposite to increase in z.") 


# ## Homework Problems ##
# 
# ### Homework Problem 6: Hydrologic Triangle ###

# In[8]:


r10_1= pn.pane.Markdown("""
The figure below shows the position of five groundwater observation wells with measured hydraulic heads in m a.s.l. 
 <br><br>

**a.** Sketch head isolines for intervals of 1 m by applying the hydrologic triangle method.
<br><br>
**b.** Indicate the flow direction.<br><br>
""", width = 500, style={'font-size': '13pt'})
r10_2 = pn.pane.PNG("images/T05_TH6.png", width=400)  

pn.Row(r10_1, r10_2)


# ### Homework Problem 7: Flow Nets

# In[9]:


#
r11_1= pn.pane.Markdown("""
Sketch head isolines and streamlines for the well doublette shown below. 
In this case, injection and withdrawal of groundwater is superimposed to a uniform flow component.
 <br><br><br><br><br><br>
 """, width = 900, style={'font-size': '13pt'})

r11_2 = pn.pane.PNG("images/T05_TH7.png", width=600)  

r11_3= pn.pane.Markdown("""
 <br><br><br><br><br><br>
 """, width = 900, style={'font-size': '13pt'})

pn.Column(r11_1, r11_2, r11_3)


# In[ ]:




