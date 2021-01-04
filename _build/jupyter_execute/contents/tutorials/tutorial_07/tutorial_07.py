#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import panel as pn
pn.extension('katex') 


# # Tutorial 7 - Wells #
# 
# 
# <br>
# 
# 1. **Solution of Homework Problems 5 -6**
# <br>
# 2. **Tutorial Problems on Wells**
# <br>
# 3. **Homework Problems on Wells**
# 
# <br>
# 
# 
# 
# 
# 
# 
# 
# ## Homework Problem 5: Effective Hydraulic Conductivity ##

# In[2]:


r9_1= pn.pane.Markdown("""
A gravel layer with a thickness of 2.5 m is embedded between two sand layers. Both sand layers have a thickness of 
1.5 m and a hydraulic conductivity of 3.7·10<sup>-4</sup> m/s. Steady-state groundwater flow is perpendicular to the layering. 
An overall head difference of 5.5 cm and a discharge of 500 l/d per unit area have been determined <br><br>

**a.** Determine the effective hydraulic conductivity.<br><br>
**b.** What is the hydraulic conductivity of the gravel layer?<br><br>
**c.** Which effective hydraulic conductivity would be obtained if flow was assumed to be in parallel with the layering?<br><br>
**d.** Calculate effective hydraulic conductivity if the angle between the flow direction and the layering equals 30°. <br>

""", width = 900, style={'font-size': '12pt'})
r9_1


# ### Solution ###
# 
# The given problem can be visualized as:
# 
# <img src= "images/T07_fH5.png" alt="HW-P5" class="bg-primary" width="350px">
# 
# We will use Darcy's law for the homogeneous system, which is given as
# 
# $$
# Q/A = K_{eff} \cdot \Delta h/m
# $$
# where $m = 2\times m_1 + m_2$ is the total thickness
# 
# For vertical flow, the effective conductivity is $K_v$
# 
# $$
# K_v = \frac{m}{\sum\limits_{i=1}^n\frac{m_i}{K_i}}
# $$
# 
# $$
# K_h = \frac{\sum\limits_{i=1}^n m_i\cdot K_i}{m}
# $$
# 
# And for the inclined flow, the known relation fro $K_{eff}$ is
# 
# $$
# K_\theta = \frac{1}{\frac{\cos^2\theta}{K_h}+ \frac{\sin^2\theta}{K_v}}
# $$

# In[3]:


# Given

Q_A = 500 # L/d/m^2, discharge/m^2
D_h = 5.5 # cm, head difference
m1= m3 = 1.5 # m, layer thickness for layer 1 and 3
K1= K3 = 3.7e-4 # m/s, Conductivity of layer 1 and 3
m2 = 2.5 # m, thickness of layer 2

# interim calculation
Q_Am = Q_A/1000 # m/d/m^2, discharge/m^2 - unit change
D_hm = D_h/100 # m, unit change, head difference
m = m1+m2+m3 # m, total thickness

# solution part a. (from the first equation above)

K_eff = Q_Am*m/D_hm # m/d, Q/A*m/Dh => Q/A is given
K_effs = K_eff/(24*60*60)

#output
print("\033[1m Result of HW Problem 5(a) are:\033[0m\n")
print("The effective conductivity is {0:0.1f}".format(K_eff), "m/d \n")
print("The effective conductivity is {0:0.2e}".format(K_effs), "m/s")


# In[4]:


# solution 5b and 5c

K_v = K_effs # m/s, Keff = Kv

# Re-organizing the second equation above
# Solution

K2 = m2/((m/K_v) - 2*(m1/K1)) # m/s, conductivity of layer 2

#output
print("\033[1m Result of HW Problem 5(a) is:\033[0m\n")
print("The conductivity of layer 2 is {0:0.2e}".format(K2), "m/s \n")


# In[5]:


# Solution of part 5(c) and 5(d)

# 5(c) can be obtained from the third equation above.

K_h = (m1*K1+m2*K2+m3*K3)/m

# 5(d) can be obtained from the last equation above.

theta = 30 # degrees

# interim calculation 
theta_r = theta*np.pi/180 # radian, degree must be changed into radian

K_theta = 1/((np.cos(theta_r)**2/K_h)+ (np.sin(theta_r)**2/K_v))

# output

#output
print("\033[1m Result of HW Problem 5(c) and 5(d) are:\033[0m\n")
print("The effective horizontal conductivity is {0:0.2e}".format(K_h), "m/s \n")
print("The effective conductivity when the discharge is 30 degree inclined is {0:0.2e}".format(K_theta), "m/s")


# ## Homework Problem 6: Flow net using triangulation ##

# In[6]:


r10_1= pn.pane.Markdown("""
The figure below shows the position of five groundwater observation wells with measured hydraulic heads in m a.s.l. 
 <br><br>

**a.** Sketch head isolines for intervals of 1 m by applying the hydrologic triangle method.
<br><br>
**b.** Indicate the flow direction.<br><br>
""", width = 500, style={'font-size': '13pt'})
r10_2 = pn.pane.PNG("images/T07_fH6.png", width=400)  

pn.Row(r10_1, r10_2)


# #### Solution of Homework Problem 6 ####

# In[7]:


# solution

img_1 = pn.pane.PNG("images/T07_fH6a.png", width=400)
img_2 = pn.pane.PNG("images/T07_fH6b.png", width=400)
img_3 = pn.pane.PNG("images/T07_fH6c.png", width=400)
img_4 = pn.pane.PNG("images/T07_fH6d.png", width=400)
img_5 = pn.pane.PNG("images/T07_fH6e.png", width=700)

tabs = pn.Tabs(('Step 1', img_1), ("Step 2", img_2), ("Step 3", img_3), ("Step 4", img_4), ("Step 5", img_5) )
tabs


# ## Homework Problem 7: Flow Nets wells ##

# In[8]:


#
r11_1= pn.pane.Markdown("""
###Homework Problem 7: Flow Nets
Sketch head isolines and streamlines for the well doublette shown below. 
In this case, injection and withdrawal of groundwater is superimposed to a uniform flow component.
 <br><br><br>
 """, width = 900, style={'font-size': '12pt'})

r11_2 = pn.pane.PNG("images/T07_fH8a.png", width=500)  

r11_3= pn.pane.Markdown("""
 <br><br>
 """, width = 900, style={'font-size': '12pt'})
pn.Column(r11_1, r11_2, r11_3)


# #### Solution of Homework Problem 7 ####
# 
# The flow-net of the above scenario can be as shown in the figure below:
# 
# <img src= "images/T07_fH8.png" alt="HW-P7" class="bg-primary" width="550px">

# ## Tutorial Problems on Wells ##
# 
# ### Tutorial Problem 18 ###

# In[9]:


#
r3_1 = pn.pane.Markdown("""

A pumping test was conducted with a constant water withdrawal rate of 9 m³/h. The table shows the time-drawdown series recorded at an observation well which is located 9.85 m apart from the pumping well. The aquifer thickness is 5 m. 
Determine the storage coefficient, the transmissivity and the hydraulic conducti-vity by using the Theis method.
To this end, it is necessary to complete the table on the right such that data are made available for further steps (see next page).
<br><br><br> 
""",width = 600, style={'font-size': '12pt'})  
#data
t_m =np.array([1, 2,    3,    4,    5,    7,    9,   12,   18,   23,   33, 41,   56,  126,  636, 1896])
s_m = np.array([0.01, 0.03, 0.05, 0.06, 0.07, 0.09, 0.12, 0.14, 0.16, 0.17, 0.18, 0.19, 0.2 , 0.22, 0.3 , 0.32])


d = {'time (min)': t_m, 'drawdown (m)': s_m}
df = pd.DataFrame(data=d, index=None) 
df1= df.set_index('time (min)')
pn.Row(r3_1, df1)  


# ### Solution of Problem 18 ###
# **See L08 - slides 29-33 for more information on this problem**

# In[10]:


# Problem 18 solution contd.
r3_2 = pn.pane.Markdown("""
As a first approach, the graphical solution of the problem is to be determined, i.e. double-logarithmic data and type curve sheets are compared as follows:
<br> <br> 

1. Plot data for _s_ vs. _t/r<sup>2</sup>_ in the data sheet.<br>

2. Determine coordinates of the match point _A_ on the type curve sheet, e.g. _1/u<sub>A</sub>_ = 1 and _W<sub>A</sub>_ = 1.<br>

3. Put the data sheet on top of the type curve sheet and shift it in parallel to the coordinate axes until data points 
fall on the type curve as close as possible.<br>
4. Determine coordinates of the match point _A_ on the data sheet: 

**_As our course is online this semester, we will follow the computational approach, see below:_**
""",width = 600, style={'font-size': '12pt'})

#given
r = 9.85 # m, observation well distance
t_s = t_m*60 # s, converting time in s
t_r2 = t_s/r**2# s/m^2,  finding t/r^2 

#output
d2= {'time (s)': t_s, 'drawdown (m)': s_m, "t/r\u00b2 (s/m\u00b2)": t_r2}  
df2 = pd.DataFrame(data=d2) 
df3 = df2.set_index('time (s)')
pn.Row(r3_2, df3.head(10))  # only top 10 data shown


# In[11]:


print("\033[1m The given data:\033[0m\n")

Q_h = 9 # m^3/h - well discharge
m = 5 # m, aquifer thickness
r = 9.85 # m, observation- well location from pumping well

# interim calculation
Q_s = Q_h/3600 # m^3/s, unit- change of discharge

print("The avialable information in addition to data are:\n")
print("The well discharge, Q =  {} m\u00b3/s \n".format(Q_s))
print("The aquifer thickness, m =  {} m \n".format(m))
print("The Observation well location, r =  {} m \n".format(r))


# In[12]:


from ipywidgets import interact, widgets # for interactive plot with slider
from scipy.special import expi #

def W(u):  
    return  -expi(-u) # provides the well function

def well_f(T, S_C, r, Q): # provides the fit curve for given r and Q
    
        
    # calculated function see L07-slide 31
    u_1d = 4*T*t_s/(S_C*r**2) # calculating 1/u
    w_ud = 4*np.pi*s_m*T/Q   # well function

    # plots
    u_1 = np.logspace(10,-1,250, base=10.0)
    w_u =W(1/u_1) 
    
    plt.figure(figsize=(9,6));
    plt.loglog(u_1, w_u); 
    plt.loglog(u_1d, w_ud, "o", color="red"  )
    plt.ylim((0.1, 10));plt.xlim(1, 1e5)
    plt.grid(True, which="both",ls="-") 
    plt.ylabel(r"W(u)");plt.xlabel(r"1/u")


# In[13]:


# select the starting value for T and S_c- this has to be iteratively done.

T = 0.00322 # m^2/S - check value for Transmissivity
S_c = 7.97e-03 # (-), the storage coefficient
Q = Q_s

well_f(T, S_c, r, Q)


# In[14]:


# Compute condutivity based on the fit

K = T/m # m/s, conductivity of the aquifer.

print("The conductivity of the aquifer, K = {0:0.2e} m/s".format(K))


# ### Tutorial Problem 19 ###
# 
# A pumping test is conducted in a confined aquifer with thickness _m_ = 14.65 m. 
# The pumping rate is kept constant at _Q_ = 50 m<sup>3</sup>/h and the corresponding drawdown 
# _S_ is recorded in an observation well at a distance _r_ = 251.32 m from the pumping well (see table).
# 
# 1. Determine storage coefficient _S_,  transmissivity  _T_ and hydraulic conductivity _K_ by employing 
# the Theis method (graphical solution).<br><br>
# 2. What is the drawdown in the pumping well (radius including gravel pack: _r<sub>w</sub>_ = 0.3 m) after 500 min?                               (Hint: Use the approximation          W(u) ≈ –0.5772 – lnu + u which is valid for u << 1) 
# <br><br>
# 3. How big is the radius of influence according to Siechardt's equation?
# <br><br>
# 
# 
# ### Solution of Problem 19 ### 
# **See L07 - slides 29-33 for more information on this problem**

# In[15]:


data19 = pd.read_csv("T07_TP19_data.csv", sep = ",", usecols =["Time (min)", "Drawdown (m)"])

df_t1= data19.values[:,0]
df_s1= data19.values[:,1]

d = {'time (min)': df_t1, 'drawdown (m)': df_s1}
df = pd.DataFrame(data=d, index=None) 
df.head(5)


# In[16]:


#given

# make sure the time data is named "t_s" and drawdown is named s_m
t_s = df_t1*60 # s, converting time in sec
s_m = df_s1 # m, drawdown data

m_19 = 14.65 # m, aquifer thickness
Q_19 = 50 # m^3/h, pumping rate 
r_19 = 251.32 # m, distance of observation well

#interim calculation
t_19r2 = t_s/r_19**2 # s/m^2,  finding t/r^2 
Q_19s = Q_19/3600 # m^3/s, pumping rate in s- unit change

#output
d2= {'time [min]': df_t1, 'drawdown [m]': df_s1, "t/r\u00b2 (s/m\u00b2)": t_19r2}  
df2 = pd.DataFrame(data=d2, index=None) 
df2.head(5)


# In[17]:


# Fitting the typ curve

# Trial data - chage T and S_c data to fit the curve

T_19 = 0.00138 # m^2/s, transmissivity
S_19= 2.21e-05 # (-), storage coefficient

# fit -  make sure to write the variable name correctly

well_f(T_19,S_19,r_19, Q_19s) 


# In[18]:


# Solutions and output

K_19 = T_19/m_19

#output
print("\033[1m The results are:\033[0m\n")
print("The Transmissivity at the site is: {0:1.2e}".format(T_19), "m\u00b2/s\n")
print("The Storage coefficient at the site is: {0:1.3e}".format(S_19), "\n")  
print("The Conductivity at the site is: {0:1.1e}".format(K_19), "m/s") 


# In[19]:


# solution 19(b) and 19(c)

# Given 
r_19w = 0.3 # m, radius of the well
t_19m = 500 # min, given time in min, 

#interm calculation
t_19s = t_19m*60 # s, tive converted to second

#Calculations
u_19 = (S_19*r_19w**2)/(4*T_19*t_19s)
W_19b = -0.5772 - np.log(u_19)+u_19 # using the given approximate of W(u)
s_19b = (Q_19s*W_19b)/(4*np.pi*T_19) # see L07 - slide 32

# Solution of 19C: 
#How big is the radius of influence according to Siechardt‘s equation? 
# (L07, slide 27)

R_19 = 3000*s_19b*np.sqrt(K_19) 

#output
print("\033[1m The results are:\033[0m\n")
print("u = {0:1.2e}".format(u_19), "\n")
print("W(u)= {0:1.2f}".format(W_19b), "\n")  
print("The drawdonw at the site is: {0:1.2f}".format(s_19b), "m \n")
print("The radius of influence is is: {0:1.2f}".format(R_19), "m")


# ## HOME WORK PROBLEMS ##
# 
# 
# **Effective Conductivity and Wells**
# 
# <br><br>
# 
# <font size="4" color="red">There is no obligation to submit the homework</font>
# 
# <br>
# 
# **Pls. submit within two weeks if you wish to.**
# 
# ### Homework Problem 10 ###

# A pumping test is conducted to determine hydraulic properties (storage coefficient $S$, the transmissivity $T$ and the hydraulic conductivity $K$) of 
# the aquifer. of a confined aquifer. For this purpose, a constant 
# pumping rate of 1219 m<sup>3</sup>/d is established and drawdown is recorded in an observation well. This problem is to be 
# solved with the Theis method implemented in the code below.<br><br>
# 
# The code generates the typ curve based on your date of birth (ddmmyyyy). To use the code, you will provide different value of $T$ and $S$ and make a match of the data with the typ-curve.
# 
# Code (2 cells below)

# In[20]:


# Functions to generate well-function (this is another method based on scipy library)

from scipy.special import expi
def W(u): 
    return -expi(-u)

#Generate your data and function required to solve

def data(Q, DOB, S, T):

    '''
    Q = pumping rate in m^3/s, 
    DOB- date of birth (ddmmyyyy), 
    S = Storage Coeff. and 
    T = Transmissivity (m^2/s)
    '''
    S_dob = sum(int(DOB) for DOB in str(DOB)) # add numbers in your DOB
    d_t = np.array([3.5, 5, 6.2, 8, 9.2, 12.4, 16.5, 20, 30, 60, 100, 200, 320, 380, 500])
    d_d = np.array([0.12, 0.23, 0.31, 0.41, 0.47, 0.64, 0.82, 0.92, 1.2, 1.74, 2.14, 2.57, 3, 3.1, 3.34])
    data_t = d_t/(S_dob/22)**3 # min, time based on DOB
    data_d = d_d/(S_dob/22) # m, drawdown data based on DOB
    dist = 251/(S_dob/22) # m, distance to observation well based on DOB
    Aq_t = 15/(S_dob/22) # m, aquifer thickness based on DOB
    
    i_u = (4*T*data_t*60)/(S*dist**2) 
    W_u = (4*np.pi*data_d*T)/(Q)
    return i_u, W_u


# In[21]:


#Solution 
#Q = pumping rate in m^3/s, DOB- date of birth (ddmmyyyy), S = Storage Coeff. and T = Transmissivity (m^2/s)
# Change the value in the bracket to find the fit

i_u, W_u = data(Q=2.41E-02, DOB=11111945, S=3.53e-05, T = 2.70e-03)

#interim calculation to get typ-curve
u_1 = np.logspace(10,-1,250, base=10.0) # setting the value of u
w_u =W(1/u_1) # finding W(1/u) : as we use 1/u in the typ curce

# Output
dx_1 = {"1/u":i_u, "W(u)":W_u}; dfx_a = pd.DataFrame(dx_1); figs = plt.figure(figsize=(9,6)) 
plt.loglog(u_1, w_u) # typ curve
plt.loglog(i_u, W_u, "ro" ) # your data
plt.title("The typ curve"); plt.ylim((0.1, 10)); plt.xlim(1, 1e5)
plt.grid(True, which="both",ls="-"); plt.ylabel(r"W(u)");plt.xlabel(r"1/u"); plt.close()
rx_2 = pn.pane.Matplotlib(figs, dpi=300); pn.Row(dfx_a, rx_2) 


# In[ ]:




