#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import ipysheet as ips
import panel as pn
from scipy import stats 
pn.extension("katex") 


# # Tutorial 4 #
# 
# + **solutions for homework problems 1 – 4**
# 
# + **tutorial problems on effective conductivity and flow nets**
# 
# + **homework problems on effective conductivity and flow nets**
# 
# 
# 
# 
# 
# 
# 
# ### Solutions for Homework Problems 1 – 2 ###
# 
# 
# 

# In[2]:


#
r1_1 = pn.pane.Markdown("""

### Homework Problem 1 ###

The pressure head in an aquifer extending over 200 km<sup>2</sup> is decreased by 1.60 m.
Determine the loss of groundwater in the aquifer for two scenarios:
A. The aquifer is unconfined (storage coefficient 0.13).
B. The aquifer is confined (storage coefficient 0.0005).

""",width = 800, style={'font-size': '13pt'})  

r1_2= pn.pane.PNG("images/T03_H1.png", width=350)
#r1_2 = pn.pane.PNG("images/T03_H1.PNG") 

### Tutorial Problem 7 – Solution ###

#<img src="images/T03_H1.PNG" alt="Grosser Garten Map"  width="40%" height="100%" >

r1_3 = pn.pane.Markdown(""" 
### Solution - Homework Problem 1 ###
<br> 
Relevant information can be found in Lecture L03, Slides- 28-30

""",width = 800, style={'font-size': '13pt'})  

r1_3b = pn.pane.LaTeX(r""" 
<br> 
The relevant equations is:<br>
$$
S = \Delta V_w/(A\cdot \Delta H)
$$

""",width = 800, style={'font-size': '13pt'}) 
pn.Column(r1_1, r1_2, r1_3, r1_3b)   


# In[3]:


# Given 
A = 200 # km^2, aquifer area
D_h = 1.6 # m, head decrease
S_u = 0.13 # (-), Storativity unconfined aquifer
S_c = 0.0005 # (-) Storage coefficient, confined aquifer

# Solution
DV_wu = A*S_u*D_h * 10**6 # m^3 change in water volume unconfined aquifer
DV_wc = A*S_c*D_h* 10**6  # m^3 change in water volume unconfined aquifer

# output

print("Change in water volume in unconfined aquifer is: {0:1.1e}".format(DV_wu),"m\u00b3 \n")
print("Change in water volume in confined aquifer is: {0:1.1e}".format(DV_wc),"m\u00b3")


# ## Homework Problem 2
# 
# Conduct a sieve analysis for a dried soil sample (see data in the table below)
# 
# 1. Draw the granulometric curve (cumulative mass distribution) and briefly characterise the sediment with regard to its major constituent(s).
# 2. What is the coefficient of uniformity? 
# 

# In[4]:


#
title = ["mesh   size  [mm] ", "residue in the sieve [g] ", "∑Retained %", "Commulative Passed %"]
Size = [6.3, 2, 0.63, 0.2, 0.063, "< 0.063 /cup"]
passed = [11, 62, 288, 189, 42, 10]
s2 = ips.sheet(rows=6, columns=4, row_headers=False, column_headers=title)
ips.column(0, Size, row_start=0) 
ips.column(1, passed, row_start=0); s2 


# In[5]:


# Solution of problem 2

t_sample = np.sum(passed) # g, add the residue column to get total mass
retained_per = passed/t_sample *100 # %, # retain percentage residue/total mass
retain_per_cumsum =np.cumsum(retained_per) # get the cummulative sum of the reatined
passing_cumper = 100 - retain_per_cumsum # substract 100-cummsum to get passing % - the last column

#Output
s3 = ips.sheet(rows=6, columns=4, row_headers=False, column_headers=title)
ips.column(0, Size, row_start=0) 
ips.column(1, passed, row_start=0); 
ips.column(2, retained_per, row_start=0); 
ips.column(3, passing_cumper, row_start=0); s3 


# In[6]:


# Plotting granulometric curve

plt.rcParams['axes.linewidth']=2
plt.rcParams['grid.linestyle']='--'
plt.rcParams['grid.linewidth']=1
x = np.append([20], Size[:5]) # adding for all left over.
y = np.append([100],passing_cumper[:5])
fig = plt.figure(figsize=(9,6));
plt.plot(x, y, 'x-', color='red', lw=2.5); 
tics=x.tolist()
plt.xscale('log');lw=2.5
plt.grid(which='major', color='k', alpha=0.7) 
plt.grid(which='minor', color='k', alpha=0.3)
plt.xticks(x, tics);  
plt.yticks(np.arange(0,110,10));
#plt.title('grain size distribution (combined wet sieving and sedimentation analysis)');
plt.xlabel('grain size d [mm]');
plt.ylabel('Cummulative Passed fraction %');

plt.annotate('', xy=(0.20, 10),  xycoords='data', xytext=(0.045, 10), arrowprops=dict(arrowstyle='->', color="b", lw=2.5),ha='right', va='top',)
plt.annotate('', xy=(1.1, 60),  xycoords='data', xytext=(0.045, 60), arrowprops=dict(arrowstyle='->', color="b", lw=2.5),ha='right', va='top',)
plt.annotate(r'$d_{60}$', xy=(1, 60),  xycoords="data", xytext=(0.85, -3),color='red',size=12, arrowprops=dict(arrowstyle='<-', color="b", lw=2.5),ha='left', va='bottom',)
plt.annotate(r'$d_{10}$', xy=(0.20, 10),  xycoords='data', xytext=(0.235, 1.5),color='red',size=12, arrowprops=dict(arrowstyle='<-', color="b", lw=2.5),ha='right', va='top',)
plt.rcParams["font.weight"] = "bold"   

plt.savefig("fig6.png")

mpl_pane = pn.pane.Matplotlib(fig, dpi=144)


# In[7]:


# From the figure
d_10 = 0.22 # mm,approx, diameter 10% passing, see the arrow bottom in x-axis
d_60 = 1.0 # mm, approx diameter 10% passing, see the arrow bottom in x-axis

c_u = d_60/d_10 # [], coefficient of uniformity

#Output
print("The coefficient of uniformity is: {0:1.1f}".format(c_u)) 
r2_1 = pn.pane.Markdown("""
**Major constituents: coarse sand/medium sand** """, width=600, style={'font-size': '13pt', 'color': 'blue'} )
pn.Row(r2_1) 


# In[8]:


# Tutorial Problem 11- Effective Conductivity and flow nets
r5_1 = pn.pane.Markdown("""
#Tutorial Problems on Effective Conductivity and Flow Nets
""", width = 900) 

r5_2 = pn.pane.Markdown("""
###Tutorial Problem 11: Effective Hydraulic Conductivity
A sandy layer with a thickness of 2.5 m is embedded between two gravel layers. B
oth gravel layers have a thickness of 1.5 m and a hydraulic conductivity of 3.7·10<sup>-3</sup> m/s. 
Steady-state groundwater flow is in parallel to the layering. 
A hydraulic gradient of 0.001 and an overall discharge of 1 m³/d per unit width have been determined.
<br><br>
a. Determine the effective hydraulic conductivity.<br><br>
b. What is the hydraulic conductivity of the sand layer?<br><br>
c. Which effective hydraulic conductivity would be obtained if flow was assumed perpendicular to the layering?<br><br>
d. Calculate effective hydraulic conductivity if the angle between the flow direction and the layering equals 45°.
""", style={'font-size': '13pt'})

pn.Column(r5_1, r5_2)  


# In[9]:


# Solution of Problem 11
r5_3 = pn.pane.PNG("images/T03_TP11_a.png", width=400)
r5_4 = pn.pane.LaTeX(r"""
Known relationships are (see Lecture 05, Slides 8-13, 22):
$$
Q = WmK\frac{\Delta H}{L}
$$
$$
K = \frac{Q/W}{m\cdot \Delta H \cdot L}
$$
Weighted arithmetic mean to determine hydraulic conductivity for sand:

$$
K = \frac{1}{m}\sum_{i=1}^n m_i\cdot K_i
$$
where $i$ is different layers
""", width = 500, style={'font-size': '13pt'})
spacer2 = pn.Spacer(width=100)

pn.Row(r5_3, spacer2, r5_4)  


# In[10]:


#Given Solution of 11 a, b

Q = 2 # m^3/d, discharge
W = 1 # m, per unit width
K_g = 3.7*1E-3# m/s, conductivity of gravel layer 
m_g = 1.5 # m, thickness of gravel layer
m_s = 2.5 # m, thickness of sand layer
m = 2*m_g + m_s # m. total thickness of aquifer
Dh_L = 0.001 # (-), hydraulic gradient


#Solution of 11a
Keff_h = (Q/W)/(m*Dh_L) # m/d, conductivity
Keff_hs = Keff_h/(24*3600)# m/s, conductivity unit changed

#Solution of 11b
# K_eff = (2*m_g*K_g + m_s*K_g)/m

K_s = ((m*Keff_hs - 2*m_g*K_g))/m_s  

print("Effective horizontal hydraulic conductivity (Keff_h) = {0:1.2f}".format(Keff_h), "m/d\n" ) 
print("Effective horizontal hydraulic conductivity (Keff_hs) = {0:1.3E}".format(Keff_hs), "m/s\n" )
print("Hydraulic conductivity of sand layer (K_s) = {0:1.1E}".format(K_s), "m/s" )     


# In[11]:


#Given Solution of 11 c, d

r5_5 = pn.pane.PNG("images/T03_TP11_b.png", width=200) 
r5_6 = pn.pane.PNG("images/T03_TP11_c.png", width=200) 

r5_7 = pn.Column(r5_5, r5_6) 

r5_8 = pn.pane.LaTeX(r"""
Vertical effective conductivity is given by weighted harmoninc mean
$$
K = \frac{m}{2\cdot \frac{m_g}{K_g} + \frac{m_s}{K_s} }
$$
<br>
For inclined aquider the effective conductivity is:

$$
K = \frac{1}{\frac{\cos^2\theta}{K_h} + \frac{\sin^2\theta}{K_v}}
$$

""", style={'font-size': '13pt'})

pn.Row(r5_7,spacer2, r5_8) 


# In[12]:


# Solution of 11c

Keff_v = m/(2*(m_g/K_g)+ (m_s/K_s))

#Given 
theta = 45 # theta 
theta_r = 45*(np.pi)/180 # degree to radian conversion
K_h = Keff_hs # m/s, solution from 11a
K_v = Keff_v # m/s, solution from 11c

# solution from 11d
Keff_i = 1/((np.cos(theta_r)**2/K_h)+(np.sin(theta_r)**2/K_v))


print("Effective vertical hydraulic conductivity (Keff_v) = {0:1.2E}".format(Keff_v), "m/s\n" ) 
print("Effective inclined hydraulic conductivity (Keff_i) = {0:1.2E}".format(Keff_i), "m/s" ) 


# In[13]:


#
r6_1 = pn.pane.Markdown("""
### Tutorial Problem 12: Hydrologic Triangle
The figure below shows the position of four groundwater observation wells with measured hydraulic heads in m a.s.l. 
<br> <br>
**a.** Sketch head isolines for intervals of 1 m by applying the hydrologic triangle method.<br><br>
**b.** Indicate the flow direction.

""",width = 400, style={'font-size': '13pt'})

r6_2 = pn.pane.PNG("images/T03_TP12_a.png", width=400) 

pn.Row(r6_1,spacer2, r6_2) 


# In[14]:


# 
r6_3 = pn.pane.Markdown("""
### Solution of Tutotrial Problem 12

Step 1. Connects all the points
""", width=600)

r6_2.object = "images/T03_TP12_b.png"
r6_3


# In[15]:


#
r6_4 = pn.pane.Markdown("""
### Solution of Tutotrial Problem 12
Step 2. Divide the connected lines at equal head-level (here = 1 m)
""", width=600)
r6_2.object = "images/T03_TP12_c.png"


# In[16]:


#
r6_4 = pn.pane.Markdown("""
### Solution of Tutotrial Problem 12
Step 3. Join all the equal head lines 
""", width=600)
r6_2.object = "images/T03_TP12_d.png"


# In[17]:


r6_4 = pn.pane.Markdown("""
### Solution of Tutotrial Problem 12
Step 4. Mark the flow direction from higher head towards lower head
""", width=600)
r6_2.object = "images/T03_TP12_e.png"


# In[18]:


#
r7_1 = pn.pane.Markdown("""
##Tutorial Problem 13: Flow Nets##

Sketch head isolines and streamlines for the two configurations a) and b) of a well doublette shown below. In both cases flow nets should be sketched without and with the uniform flow component.

""",width=800,  style={'font-size': '13pt'})

r7_2 = pn.pane.Markdown("""
 a) withdrawal at both wells:<br><br><br>
""",width=400,  style={'font-size': '13pt'})

r7_3 = pn.pane.PNG("images/T03_TP13_a.png", width=200)  

r7_4 = pn.Column(r7_2,r7_3)

r7_5 = pn.pane.Markdown("""
 b) Injection and withdrawl wells:<br><br><br>
""",width=400,  style={'font-size': '13pt'})

r7_6 = pn.pane.PNG("images/T03_TP13_b.png", width=200)  

r7_7 = pn.Column(r7_5,r7_6)
r7_8 = pn.Row(r7_4, r7_7) 
pn.Column(r7_1, r7_8) 


# In[19]:


r8_1= pn.pane.Markdown("""
#Homework Problems on  Effective Conductivity and Flow Nets <br><br><br> 
""", width = 800, style={'font-size': '13pt'})


r8_2= pn.pane.Markdown("""
#There is no obligation to solve homework problems!
""", width = 800, style={'font-size': '13pt', 'color':'red'})

pn.Column(r8_1,r8_2)  


# In[20]:


#
r9_1= pn.pane.Markdown("""
###Homework Problem 5: Effective Hydraulic Conductivity
A gravel layer with a thickness of 2.5 m is embedded between two sand layers. Both sand layers have a thickness of 
1.5 m and a hydraulic conductivity of 3.7·10<sup>-4</sup> m/s. Steady-state groundwater flow is perpendicular to the layering. 
An overall head difference of 5.5 cm and a discharge of 500 l/d per unit area have been determined <br><br>

**a.** Determine the effective hydraulic conductivity.<br><br>
**b.** What is the hydraulic conductivity of the gravel layer?<br><br>
**c.** Which effective hydraulic conductivity would be obtained if flow was assumed to be in parallel with the layering?<br><br>
**d.** Calculate effective hydraulic conductivity if the angle between the flow direction and the layering equals 30°. <br>

""", width = 900, style={'font-size': '13pt'})
r9_1


# In[21]:


#
r10_1= pn.pane.Markdown("""
###Homework Problem 6: Hydrologic Triangle
The figure below shows the position of five groundwater observation wells with measured hydraulic heads in m a.s.l. 
 <br><br>

**a.** Sketch head isolines for intervals of 1 m by applying the hydrologic triangle method.
<br><br>
**b.** Indicate the flow direction.<br><br>
""", width = 500, style={'font-size': '13pt'})
r10_2 = pn.pane.PNG("images/T03_TH6.png", width=400)  

pn.Row(r10_1, r10_2)


# In[22]:


#
r11_1= pn.pane.Markdown("""
###Homework Problem 7: Flow Nets
Sketch head isolines and streamlines for the well doublette shown below. 
In this case, injection and withdrawal of groundwater is superimposed to a uniform flow component.
 <br><br><br><br><br><br>
 """, width = 900, style={'font-size': '13pt'})

r11_2 = pn.pane.PNG("images/T03_TH7.png", width=400)  

r11_3= pn.pane.Markdown("""
 <br><br><br><br><br><br>
 """, width = 900, style={'font-size': '13pt'})
pn.Column(r11_1, r11_2, r11_3)


# In[ ]:




