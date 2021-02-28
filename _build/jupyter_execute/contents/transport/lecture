#!/usr/bin/env python
# coding: utf-8

# ## Retardation Factor

# In[1]:


print("\033[1m\033[4mA quick example:\033[0m You can change the provided values.\n")
print("Calculate the retardation factor.\n\n\033[1mProvided are:\033[0m")

ne = 0.4 #effective porosity [-]
rho = 1.25 # density of solid material [kg/m³]
Kd = 0.2 # distribution or partition coefficient [m³/kg]

#intermediate calculation
rho_b = (1-ne)*rho

#solution
R=1+(rho_b/ne)*Kd

print("effective porosity = {}\ndensity of solid material = {} kg/m³\nDistribution or partition coefficient = {} m³/kg\n".format(ne, rho, Kd))
print("\033[1mSolution:\033[0m\nThe resulting retardation factor is \033[1m{:02.4}\033[0m.".format(R))


# In[ ]:




