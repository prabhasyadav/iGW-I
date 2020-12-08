#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import panel as pn
from scipy import stats 
pn.extension('katex', 'mathjax') 


# # Tutorial 6 - Tutorial Problems on Flow in Confined/Unconfined Aquifer #
# 
# + **solutions for homework problems 3 – 4**
# 
# + **tutorial problems on flow in confined and unconfined aquifers**
# 
# + **homework problems on flow in confined and unconfined aquifers**
# 
# 
# 
# 
# 
# 
# 
# ## Solutions for Homework Problems 3 – 4 ##
# 
# 

# ### Homework Problem 3 ###

# In[2]:


#
r3_1 = pn.pane.Markdown("""
## ##


**A**. Derive an expression for hy-draulic conductivity K for the constant-head permeameter shown in the figure.<br><br>
**B**. The hydraulic conductivity of a sample (length 10 cm, dia-meter 4 cm) is to be determined. 
The water depths a<sub>1</sub> and a<sub>2</sub> equal 6 cm and 3 cm, resp. A water volume of 250 ml passed the sample during an experimental period of 36 s. <br> <br>
**C**. Which material could be contained in the sample?
""", style={'font-size': '12pt'})
spacer2=pn.Spacer(width=50)
r3_2 = pn.pane.PNG("images/T06_TH3.png", width=500)
pn.Row(r3_1,spacer2, r3_2)  


# ### Solution of the Homework Problem 3 ###

# In[3]:


#
r3_3 = pn.pane.Markdown("""
###  """, width = 700, style={'font-size': '13pt'}) 

r3_4 = pn.pane.LaTeX(r"""
General formula for constant-head permeameter:
$$
K = \frac{QL}{A(h_{in}-h_{out})}
$$
<br>
The column outlet is chosen as the reference level 
$z = 0$ with the $z-$axis pointing up-ward. As a consequence, we have $z = L$ at the inlet. <br> <br> <br> <br>
""", style={'font-size': '12pt'})

r3_5 = pn.pane.LaTeX(r"""
At The Outlet: <br>
pressure head =  $a_2$  <br>
elevation head = 0 <br>
$h_{out}$ = $a_2$ <br>
""", width = 300, style={'font-size': '12pt'})

r3_6 = pn.pane.LaTeX(r"""
At The Inlet: <br>
pressure head = _a<sub>1</sub>_ <br>
elevation head = $L$<br>
$h_{in}$ = $a_1+ L$ <br>

""", width = 300, style={'font-size': '12pt'})

r3_7 = pn.pane.LaTeX(r"""
head difference: <br>
$$h_{in}-h_{out} = a_{1} + L - a_{2}$$<br>
hydraulic conductivity:
$
K = \frac{QL}{a_1 + L - a_2}
$
""", width = 800, style={'font-size': '12pt'})

C1 = pn.Row(r3_5, r3_6)  

r3_2.object = "images/T06_TH3a.png" 

pn.Column(r3_3, r3_4, C1, r3_7)  


# In[4]:


# Problem 3b, Given are:
L = 10# cm, length of column 
a1 = 6# cm, pressure head at 1 
a2 = 3# cm, pressure head at 2 
d = 4 # cm, diameter of the column
Q = 250/36 # ml/s = 250 cm³/36s, discharge 
A = np.pi*(d/2)**2 # cm^2 Area of the column

#calculation
K = Q*L/(A*(a1+L-a2))# cm/s, Conductivity

#output
print('\033[1m' + 'Results are:' + '\033[0m \n')
print("The conductivity of the column is:{0:1.3f}".format(K), "cm/s \n")
print("The conductivity of the column is:{0:1.3E}".format(K/100), "m/s\n")

r3_8 = pn.pane.Markdown("""
The sample in the column is: **Coarse sand - Fine gravel**
""", width=400)  

pn.Row(r3_8) 


# ### Homework Problem 4 ###

# In[5]:


# given data - you may change the number

t = np.array([0, 5, 18, 23, 27, 29]) # min, given time
Dh = np.array([36.9, 33.6, 26.3, 23.9, 22.1, 21.3]) # cm, head difference 

# creating data table
data = {"Time (min)": t, "Δh (m)": Dh}
df = pd.DataFrame(data)
df1 = df.T


r_h4 = pn.pane.Markdown("""
A Darcy experiment is performed by a falling-head permeameter using water at 20°C. 
Length and diameter of the sample are 20 cm and 6 cm, resp. The inner tube diameter is 4 cm. 
The following data are available for the time-dependent hydraulic head difference : 
""",width = 600, style={'font-size': '12pt'})


spacer2=pn.Spacer(width=50)

pn.Column(r_h4,spacer2, df1)


# In[6]:


r_h4c = pn.pane.Markdown("""
**A.** Convert times to seconds and plot the logarithm of the ratios of head differences ln(Δh(0)/Δh(t)) vs. time t. 
(Use the coordinate system on next page). <br><br>
**B.** Determine the slope of the correspon-ding regression line.<br><br>
**C.** Determine hydraulic conductivity K.<br><br>
**D.** Determine intrinsic permeability k.<br>
""", width=500, style={'font-size': '12pt'})

r_h4e = pn.pane.PNG("images/T06_TH4b.png", width=350)
spacer2=pn.Spacer(width=50)


pn.Row(r_h4c, spacer2, r_h4e)  


# ### Solution of Homework Problem 4 ### 

# In[7]:


#
r4_1 = pn.pane.LaTeX(r"""
The formula for variable-head permeameter:
$$K = \frac{d_t^2 L}{d_t^2 t} \cdot \ln \frac{ h_{in}(0)-h_{out}}{h_{in}(t) - h_{out}} = \frac{d_t^2 L}{d_e^2 t}\cdot \ln\frac{\Delta h(0)}{\Delta h(t)}$$
Rearrangement shows that the natural logarithm of $\Delta h(0)/\Delta h(t)$ depends linearly on time $t$: 
$$
\ln\frac{\Delta h(0)}{\Delta h(t)} = \frac{K \cdot d_e^2 L}{L\cdot d_t^2} \cdot t
$$
$$\text{slope} =\frac{K\cdot d_e^2}{L\cdot d_t^2}$$
$$K = L \frac{d_t^2 }{d_e^2}\cdot \text{slope}$$
""",width=800, style={'font-size': '12pt'} )

r4_1
 


# In[8]:


#Caclulation

t_s = t*60 # s, time in second
Dh0_Dht = Dh[0]/Dh # (-), Delta h(0)/Delta h(t)
ln_Dhodht = np.log(Dh0_Dht)# (-), ln(Delta h(0)/Delta h(t))

slope, intercept, r_value, p_value, std_err = stats.linregress(t_s, ln_Dhodht) # linear regression


# result table
data2 = {"Time (s)": t_s, "Δh(0)/Δh(t)":Dh0_Dht,"ln (Δh(0)/Δh(t)": ln_Dhodht}
df2 = pd.DataFrame(data2)

fig = plt.figure()
plt.plot(t_s, ln_Dhodht, 'o', label=' provided data');
pred = intercept + slope*t_s
plt.plot(t_s, pred, 'r', label='y={:.2e}x+{:.2e}'.format(slope,intercept)) ;
plt.xlabel(r"$t (s)$");
plt.ylabel(r"$\ln\frac{\Delta h (0)}{\Delta h (t)}\;\:(-)$");
plt.grid();
plt.legend(fontsize=11) 
plt.text(150, 0.42,'$R^2 = %0.2f$' % r_value)
plt.close() # otherwise we have 2 figure
r4_2 = pn.pane.Matplotlib(fig, dpi=300)

pn.Row(df2,spacer2,r4_2)  


# In[9]:


#Solution of 4C
# Given 
L = 20 # cm, Length of the column
d_t = 4 # cm, diameter of the tube
d_c = 6# cm, diameter of the column
slope = 3.14e-04 # 1/s, from fitting see plot

K = L*(d_t**2/d_c**2)*slope # cm/s, conductivity calculated using eqn from previous slide

#output
print('\033[1m' + 'Results are:' + '\033[0m \n')
print("The conductivity in the column is: {0:1.2e}".format(K), "cm/s\n")
print("The conductivity in the column is: {0:1.2e}".format(K/100), "m/s\n")

#Solution of 4D
# Given
rho_w = 998.2 # kg/m^3, density of water
eta_w = 1.0087E-3# kg/(m-s), viscocity of water
g = 9.81 # m/s^2, accl. due to gravity

k = K/100*eta_w/(rho_w*g)# m^2, K = k*ρ/n
k_D = k/0.987E-12 # D, 1D = 0.987E10-12 m^2

print("The permeability of the media is: {0:1.2e}".format(k), "m\u00b2 \n")  
print("The permeability of the media in Darcy's unit is: {0:1.2f}".format(k_D), "D")  


# ## Tutorial Problems ##
# 
# ### Tutorial Problem 16- flow in confined aquifer ###

# In[10]:


r16_2 = pn.pane.LaTeX(r"""
A confined aquifer is 30 m thick and 5 km wide. Two observation wells are located 1.5 km apart
in the direction of flow. The head in well 1 is 90 m and in well 2 it is 85.0 m. The hydraulic conductivity
is 1.5 m/d. 
<br><br>
1. What is the total daily flow of water through the aquifer?
<br><br>
2. What is the elevation of the potentiometric surface at a point located 0.5 km from well $h_1$
and 1 km from well $h_2$?
""",width = 600, style={'font-size': '12pt'})  

r16_3 = pn.pane.PNG("images/T06_TP16.png", width=350)

r16_4 = pn.pane.Markdown("""
### Solution of Problem 20:###
""",width = 600, style={'font-size': '12pt'}) 


pn.Row(r16_2, r16_3)


# ### Solution of Problem 16 ###

# In[11]:


# solution
r16_6 = pn.pane.LaTeX(r"""
From Darcy Law:
$$ q' = K b \frac{dh}{dL} \qquad\qquad \text{(eq. 1A)}$$
where,
$q'$ is the flow per unit width [L$^2$T$^{-1}$], <br>
$b$ is aquifer thicknes [L]<br>
$K$ is Hydraulic Conductivity [LT$^{-1}$]<br>
and $\frac{dh}{dl}$ = hydraulic gradient [-]<br><br>

Since the thickness of the aquifer is uniform, any hydraulic head between two known 
heads ($h_1$ and $h_2$) can be obtained by rearranging the above equation, from
$$
h_2 = h_1 - \frac{q'}{Kb}x
\qquad\qquad \text{(eq. 1B)}$$
where $x$ is the distance from $h_1$
""",width = 900, style={'font-size': '12pt'})  

r16_6


# In[12]:


# Given are:
m_1 = 30 # m, uniform thinckness of aquifer 
w_1 = 5 # km, width of the aquifer
d_l = 1.5 # km, distance between wells
hy1_w1 = 90 # m, head in well 1
hy1_w2 = 85 # m, head in well 2
K_1 = 1.5 # m/d, conductivity in aquifer
d_x = 0.5 # km, distance from head 1

# interim calculation
w_1m = w_1*1000 # m, widht of the aquifer
d_lm = d_l*1000 # m, distance between wells
d_xm = 0.5*1000 # m, distance from head 1

#Solution 1
dh_y1 = (hy1_w1 - hy1_w2)/d_lm # (-), head gradient
Q_y1 = K_1*m_1*dh_y1*w_1m # m^3/day, discharge using the first eq. above.

#Solution 2 
w_2 = d_xm # m, distance from well 1 
q_1 = Q_y1/w_1m # m^2/d, flow per unit width
h_y1 = hy1_w1-(q_1/(K_1*m_1))*w_2 # head at 0.3 Km from Well 1, using the second equation 


#output
print('\033[1m' + 'Results are:' + '\033[0m \n')
print("The daily discharge from the aquifer is: {0:1.2f}".format(Q_y1), "m\u00b3/d\n")
print("The head at 0.3 Km from well 1 is : {0:1.2f}".format(h_y1), "m")


# ### Tutorial Problem 17- flow in unconfined aquifer ###

# In[13]:


r17_1 = pn.pane.LaTeX(r""" 
Discharge from an unconfined aquifer presented in the figure below in which $h_1 = 20$ m, $h_2 = 10$ m, and $L = 50$ m 
is to be obtained. Other information available are that the aquifer is 30 m wide and has a uniform conductivity 
$K = 5 \times 10^{-6}$ m/s. Also known are that the Duipuit assumptions applies to this unconfined aquifer. 
""",width = 500, style={'font-size': '12pt'})  

r17_2 = pn.pane.PNG("images/T06_TP17.png", width=400)

pn.Row(r17_1, r17_2) 


# ### Solution Tutorial Problem 17 ###

# In[14]:


r17_4 = pn.pane.LaTeX(r"""
As Dupuit assumptions are valid, the discharge per unit width of aquifer ($q'$) 
can be obtained from
$$
q' = -Kh\frac{dh}{dx} \qquad\qquad \text{eq. (3A)}
$$
where $h$ is saturated thickness of aquifer located at $x$ distance from $h_1$ end.
From figure, at $x = 0$, $h = h_1$ and at $x = L$, $ h = h_2$. Based on this
differential equation eq. (3A) can be directly integrated after separation of variable to obtain $q'$, i.e.,
$$
\int_0^L q'dx = -K\int_{h_1}^{h_2}h dh
$$
Integration leads to
$$
q'x\Big|^L_0 = -K\frac{h^2}{2}\Big|_{h_1}^{h^2}
$$
resulting to 
$$
q'L = -K\Bigg( \frac{h_2^2}{2} - \frac{h_1^2}{2}\Bigg)
$$

and $q'$ is then obtained from

$$
q' = -\frac{1}{2}K\Bigg( \frac{h_2^2 -h_1^2 }{L}\Bigg) \qquad\qquad \text{eq. (3B)}
$$
""",width = 700, style={'font-size': '12pt'})  

r17_4


# In[15]:


#Solution of Tutorial Problem 22:
# Given

h3_1 = 20 # m, aquifer head at point 1
h3_2 = 10 # m, aquifer head at point 1
K3 = 5 * 10**-6 # m/s uniform conductivity of aquifer
L3 = 50 # m, length of the aquifer
W3 = 30 # m, width of the aquifer

#Calculation
q3 = -1/2*K3*(h3_2**2 - h3_1**2)/L3 # m^2/s, unit width discharge using eq. 3B
Q3 = q3 * W3 # m^3/s, total dischage from given width

#output
print('\033[1m' + 'Results are:' + '\033[0m \n')
print("Discharge per unit width of aquifer is: {0:1.2e}".format(q3), "m\u00b2/s \n")
print("Discharge from the given width of aquifer is: {0:1.2e}".format(Q3), "m\u00b3/s") 


# ## Homework Problems Flow problems ##
# 
# These problems will require you to make some research. I will suggest that you check the **Groundwater** book by **R. Allan Freeze** and **John A. Cherry**. The book is now freely available at [https://gw-project.org/books/groundwater/](https://gw-project.org/books/groundwater/)
# 
# **There is no-obligation to submit the homework problems**
# 
# 
# ### Homework Problem 8 - confined aquifer ###

# In[16]:


rh8_2 = pn.pane.LaTeX(r""" 
Presented below in the figure is the available information of an aquifer cross-section. 
The aquifer is confined and of variable thickness across the cross-section. It has a uniform conductivity 
$5.6 \times 10^{-5}$ m/s. The total Discharge from the aquifer of width 500 m is required to be obtained.
""",width = 400, style={'font-size': '12pt'})  

rh8_3 = pn.pane.PNG("images/T06_HP8.png", width=500)

pn.Row(rh8_2, rh8_3)


# ### Homework Problem 9 - unconfined aquifer ### 
# 

# In[17]:


rh9_2 = pn.pane.LaTeX(r"""
In a schematic below an unconfined aquifer is found to divide 2 rivers of differnt stages $h_1 = 30$ m and $h_2 = 10$ m. 
The aquifer of length $L = 50$ m and with uniform conductivity $K = 5\times 10^{-6}$ m/s is found to receive recharge at 
the rate ($w$) of 0.01 m/d. <br>
a) What will be the hydraulic head and discharge per unit width ($q'$) in the aquifer at 5 m 
from the left river. <br>
b) What will the head at the same location when aquifer receives no recharge. 

""",width = 900, style={'font-size': '12pt'})  

rh9_3 = pn.pane.PNG("images/T06_HP9.png", width=450)

pn.Column(rh9_2, rh9_3)


# In[ ]:




