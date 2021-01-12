#!/usr/bin/env python
# coding: utf-8

# # Contaminant Concentration

# 
# ## Task 1
# A saline solution with a concentration of 370mg/l is itroduced to a 2-m-longsand column in which the pores are initially filled with distilled water.If the solution drains through the column at an average linear velocity of 0.79 m/day and the dynamic dispersivity of the sand columnis 15 cm, what would the conceration of the effluent be at 1.8 days after the flow begins?
# 
# source: "Applied Hydrogeology" by C.W. Fetter <br>
# 

# In[1]:


import math
import scipy.special as sc


# In[2]:


# A.inputs
C0 = 370  #mg/l initial concentration
L = 2 #m length of the sand column
Vx = 0.79  #m/d linear velocity of groundwater flow
Disp = 0.15 #m dispersivity of sand column
t = 1.8  #days after the flow begins
print("A. Given information: ")
print("Initial concentration = {} mg/l\nlength of the sand column = {} m\nLinear velocity of groundwater flow = {} m/d\nDispersivity = {} m\nTime={} d".format(C0, L, Vx, Disp, t),"\n")



# B.Calculations of :
DL=Disp*Vx # longitudinal dispersivity coefficient

X=(L-(Vx*t))/(2*((DL*t)**0.5))#  Error functions
Y=(L+(Vx*t))/(2*((DL*t)**0.5))#  Error functions
C=(C0/2)*(sc.erfc(X)+(math.exp((Vx*L)/DL)*sc.erfc(Y)))# Concentration after t days

#  Defining a concentration function and conditional statemen based on error functions
print("B. Calculations: ")

if X>3 and Y<3:
    sc.erfc(X)==0, print("Error function of X [erfc(X)] is negligible or zero\n")
    C=(C0/2)*(math.exp((Vx*L)/DL)*sc.erfc(Y))
    rsults=C  
else :
    (math.exp((Vx*L)/DL)*sc.erfc(Y))==0, print("Error function of Y [erfc(Y)] is negligble or zero\n")
    C=(C0/2)*(math.erfc(X))
    results= C

    
# C.output
print("C. Output: ")
print("Concentration after 1.8 days is: ", C, "mg/l")
   


# In[ ]:




