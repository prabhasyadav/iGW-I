#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ipywidgets as widgets
get_ipython().run_line_magic('matplotlib', 'widget')
import warnings; warnings.simplefilter('ignore')


# # Subsurface Structure

# ## Porous Media
# The general definition of the porous media is a **solid which contains voids**. This definition applies to the subsurface contains solid material plus voids which represent storage and transmission of the water. The voids may have various shapes and contain fluids (mostly air and/or water). Moreover, voids may be connected to or disconnected from each other. 
# Generally voids and their properties are important to determine water storage (how much water is or could be available?) and water transmission (How fast the water can move?). 

# ## Types of porous media in the subsurface

# 
# <img src="images/L02_fig1.png" alt="Unconsolidated porous medium" class="bg-primary" width="300px">
# 
# 
# 1. **unconsolidated porous medium (Sediments)**: it is non-cemented porous media and the grains can be taken away. The formation of such porous media is due to deposition of solid material mostly by water.
# 
# 
# <img src="images/L02_fig3.png" alt="Unconsolidated porous medium" class="bg-primary" width="600px">
# 
# 2. **Consolidated porous medium (Rocks)**: the formation is due to increased pressure acting together with thermal and chemical processes. It has two types:
# 
# > Fractured porous media 
# 
# > Karstified porous media
# 
# <img src="images/L02_fig4.png" alt="Unconsolidated porous medium" class="bg-primary" width="800px">

# ## Porosity (Total porosity):
# Is defined as the volumetric share of voids in a porous media. It is a number between 0 and 1 and can be expressed as percentage (0%: no voids, 100%:no solid)
# 
# $${n}=\frac{V_{v}}{V_{T}}$$
# - $n$= total porosity
# - ${V_{v}}$= voids volume
# - ${V_{T}}$= total volume

# **Sample question**
# 
# If the total volume of a media is 254 cubic meters, and the volume of the void is 27 cubic meters, what is the porosity (give as a percent)?
# 

# In[2]:


# input data
V_T= 254 #m^3 total volume
V_v=27 #m^3 voids volume

#calculations
n=(V_v/V_T)*100

# Output
print(" Total porosity is: {0:0.2f}%".format(n) )


# ### Total porosity of artificial porous media: 
# If “grains” have identical shape and are regularly arranged, it is possible to exactly compute total porosity, the pores should have the same size.
# 
# <img src="images/L02_fig5.png" alt="Total porosity of artificial porous media" class="bg-primary" width="300px">
# 
# 
# 
# - Loose packing(first picture): each hole placed on top of the hole underneath
# 
# - Dense packing (second picture): each hole is placed at the deepest position possible
# 
# These schematics provides a practical range of porosity in the subsurface. The general range is between 25% to about 50%. In more extreme cases porosity higher than 60% is possible, e.g., cobbles, gravel. The other extreme, subsurface with no porosity (0%) is also encountered in the subsurface, e.g., in consolidated rocks. 
# 

# ### Total porosity of natural unconsolidated porous media:
# In the subsurface (natural unconsolidated porous media) there are grains of different size and total porosity depends on the grain size distribution.
# 
# 
# |               | grain  diameter  (mm) | Total  Porosity (%) |
# |---------------|-----------------------|---------------------|
# | Coarse gravel | 20 - 60               | 24 - 36             |
# | Fine gravel   | 2 - 6                 | 25 - 38             |
# | Coarse sand   | 0.6 - 2               | 31 - 46             |
# | Fine sand     | 0.006 - 0.2           | 26 - 53             |
# | Silt          | 0.002 - 0.06          | 34 - 61             |
# | Clay          | < 0.002               | 34 - 60             |
# 
# 
# |           | Total  Porosity (%) |
# |-----------|---------------------|
# | Siltstone | 21 - 41             |
# | Sandstone | 5 - 30              |
# | Basalt    | 3 - 35              |
# | Claystone | 1 - 10              |
# | Limestone | 1 - 10              |
# | Shale     | < 10                |
# | Granite   | < 1                 |
# 
# 
# Total porosity of consolidated porous media (rocks) is usually smaller than total porosity of unconsolidated porous media. However, weathering effect may lead to increase the value of porosity.
# only for unconsolidated porous media, total porosity tends to increase with decreasing grain size.
# 

# # Grain size distribution of unconsolidated porous media
# Unconsolidated porous media are able to store and transmit water that can be influenced by grain size distribution. Therefore, the grain size distribution is frequently determined in laboratory experiments in order to deduce important flow properties. 
# There are five major grain size classes (observed by increasing diameter): clay, silt, sand, and gravel (or debris). The classes for silt, clay and gavel are usually subdivided by “fine”, “medium”, and “coarse” (or “very fine”, “fine”, “medium”, “coarse”, and “very coarse”). Different ranges for individual grain size classes have been defined by different authorities or regulations. However, the standard method to determine the grain size distribution of a sample is sieve analysis.
# 

# ## Classification schemes:
# The diagrams below include a couple of classification schemes to define ranges of grain diameter for clay, silt, sand, and gravel:
# 
# <img src="images/L02_fig7.png" alt="grain size distribution" class="bg-primary" width="600px">
# 
# 
# _USDA: United States Department of Agriculture_, _ISSS: International Soil Science Society (ISSS)_, _MIT: Massachusetts Institute of Technology_, _ASTM: American Society for Testing and Materials_, _AASHTO: American Association of State Highway and Transportation Officials_, _FAA: Federal Aviation Administration_   
# 
# As can be observed that there exist several standards. These are often based on local requirements e.g., based on countries. In Germany the DIN standards are used. 

# ## Sieve analysis:
# The results from a sample consist of different grain size fractions should be transferred on granulometric curve. This curve provides cumulative information; vertical axis shows the mass fraction, and horizontal axis shows the grain diameter. For example, if 1mm grain diameter has 80% of cumulative mass fraction it means that 80% of this sample contains 1mm grain diameter or less than 1 mm (see the picture below).
# 
# **How to get granulometric curve?**
# In order to perform sieve analysis we can use sieve machine. Sieve machine consist of sets of sieves from coarse sieve on top to fine sieve and a cup at the bottom. The mechanism is to shake the set. Finally, each sieve consists of grain sizes which are bigger than the sieve.
# 
# <img src="images/L02_fig15.png" alt="grain size distribution" class="bg-primary" width="600px">
# 
# 
# <img src="images/L02_fig8.png" alt="grain size distribution" class="bg-primary" width="600px">
# 
# 
# **dx and U**: From the granulometric curve, several parameters can be determined in order to characterize the sample. ${d_{x}}$   denotes the grain diameter for which x% (in mass or weight, not volume) of the sieve material is smaller than this diameter.
# 
# <img src="images/L02_fig9.png" alt="grain size distribution" class="bg-primary" width="400px">
# 
#   Grain diameters ${d_{10}}, {d_{60}}, {d_{75}}$ are of practical importance with regard to groundwater flow properties. The     ratio of d60 and d10 is called **coefficient of uniformity, U**:
#   
#   $${U}=\frac{d_{60}}{d_{10}}$$
# 
#   ${d_{75}}$ is specifically used for well construction purpose (not covered by this lecture)

# # Subterranean water
# 
# The subsurface can be regarded as a three-phase system consisting of a solid phase (soil particles), a water phase, and a gas phase. a schematic illustration for voids or pores in an unconsolidated porous medium is given in the figure below. Each phase has similar density and other properties. Sometimes it is possible for the fourth phase which is contamination.Voids are filled with water and gas. The volumetric ratio of water in voids can be calculated by water content.
# 
# ```{image} images/L02_fig10.png
# :height: 200px
# :align: center
# :name: subterranean water
# ```
# 
# ## Water content:
# 
# Water content is defined as the share of water in the porous medium:
# 
# $${\theta}=\frac{V_{w}}{V_{T}}$$
# - ${\theta}$= water content
# - ${V_{w}}$= water volume
# - ${V_{T}}$= total volume
# 
# Water content cannot exceed the total porosity. i.e. θ≤n ( total porosity is independent of the fluid content of porous medium).
# 
# ## Degree of saturation:
# 
# Another way to express the ratio of water in the porous medium is the degree of saturation, i.e. the ratio of water volume to void volume:
# 
# $${S}=\frac{V_{w}}{V_{v}}$$
# - ${S}$= degree of saturation
# - ${V_{w}}$= water volume
# - ${V_{v}}$= voids volume
# 
# The degree of saturation is equal to $\frac{θ}{n}$ . S can vary between 0 to 1 (or between 0% to 100%), S=0 means no water in the voids, whereas S=100 means voids are completely filled with water.
# 

# **sample question**
# 

# ## Forcing act on subterranean water:
# 
# Subterranean water is subject to several forces. The most important ones are:
# 
# - gravity
# - attractive forces between the water molecules (cohesion)
# - attractive forces between water and solids (adhesion)
# 
# <img src="images/L02_fig11.png" alt="Forces on subterranean water" class="bg-primary" width="450px">
# 
# 
# In the figure above, dotted area represent the solid phase. In the pore channel the dominant force is gravity, shown as G. getting closer to the solid surface, adhesive force become more important. The numbers indicate the required pressure to remove the corresponding layer of water from the solid surface. As an example, in order to remove the last layer of water from the solid surface, 31 bar pressure needs to be applied. Another easy way to remove the water is boiling the sample in the oven.
# 
# ## Surface tension:
# 
# Cohesive forces acting on water molecules compensate each other if the molecule is not located near water-air or water-solid interface. This is no longer true at an interface: cohesive interaction is reduced on one side. The resulting force tends to minimize the interface area. Macroscopically, this effect is parametrized by the “surface tension”, which is defined as the energy needed to increase the area of the interface by one unit.
# 
# <img src="images/L02_fig12.png" alt="surface tension" class="bg-primary" width="300px">
# 
# 
# Common units of the surface tension σ are $\frac{J}{m^2}$ or $\frac{N}{m}$ (Its dimension is $\frac{M}{T^2}$). The surface tension of water is about 7.5 . 10 -2 $\frac{N}{m}$ at 10 ֯C.
# 
# ## Capillary action:
# 
# <img src="images/L02_fig13.png" alt="capillary action" class="bg-primary" width="200px">
# 
# 
# Water is subject to capillary action when adhesion is strongr than cohesion. The capillary rise of water in a tube depends on the surface tension and the tube redius. The maximum capillary rise is given by:
# 
# 
# $${h_{c}}=\frac{2\sigma{w}}{\rho_{w}{g}{r}}$$
# 
# - ${h_{c}}$= maximum capillary rise
# - $sigma{w}$= surface tension
# - $\rho_{w}$= water density
# - ${g}$= acceleration of gravity
# - ${r}$= radius of the tube
# 
# ## Capillary action in the subsurface:
# 
# Capillary actions play a dominant role in the subsurface. The capillaries are given by individual pore channels. Poor channels in poorly sorted material may strongly differ in diameter, such that a certain variability in capillary rise is observed.
# 
# <img src="images/L02_fig14.png" alt="capillary action in the subsurface" class="bg-primary" width="600px">
# 
# Left sketch shows the capillary rise in a perfectly sorted material which all the pores have the same size. So capillary rise is similar in every single pores. The right sketch, shows a real situation of subsurface. There are different grain size and then different pore channels, which results in various capillary rise.
# 

# **Sample question**
#  For water at at a tube with a redius R, the surface tension is 73$\frac{g}{s^2}$, the density is 0.999 $\frac{g}{cm^3}$. Compute the rise of water in the capillary tube

# In[3]:


# input data
sigma= 73 #g/s^2 surface tension
rho= 0.999 # g/cm^3 water density
g=980 #cm/s^2 acceleration of gravity

#calculation
h_c=(2*sigma)/(rho*g)

#output
print("The maximum water rise in this tube is: {0:0.2f} 1/R cm".format(h_c))


# In[ ]:




