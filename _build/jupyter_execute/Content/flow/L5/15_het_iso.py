#!/usr/bin/env python
# coding: utf-8

# ```{sidebar} Additional Material : Lecture Slides
# ```{toggle} Additional Material
# 
# <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSV04S9lhhZF2brpVIleI_UJYLVbrErYTtzE_XAY97ypV4QsGUpzkqxJ0BB3AZhpA/embed?start=false&loop=false&delayms=3000" frameborder="0" width="480" height="389" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
# 

# # Aquifer Heterogeneity and Anisotropy #
# 
# _(The contents presented in this section were re-developed principally by [Prof. B. R. Chahar](http://web.iitd.ac.in/~chahar/) and Dr. P. K. Yadav. The original contents are from Prof. Rudolf Liedl)_
# 
# ---
# 
# ### Motivation
# 
# The last lecture introduces aquifer properties such hydraulic conductivity, storativity, porosity. The key assumption in that lecture was that the aquifer is an 1D unit, e.g., the Darcy column, and that its properties do not vary in space. In contrast to these, an aquifer is more accurately represented by a 3D system and its properties vary both in space and directions. In fact variations of hydraulic conductivity ($K$), a most critical aquifer quantity, are dominant in most cases. Variations of $K$ can be observed at very small spatial scales and directions. Thus, aquifer properties that depends on $K$ also varies. Consequently, aquifer properties such as $K$ takes a tensor form- a quantity whose magnitude is space and direction dependent. 
# 
# In the picture below ({numref}`aquifer-het`) the 3-D spatial variability of aquifer properties is illustrated by a 2-D vertical cross-section. The picture of the outcrop show some form of a layered system, with each layer likely possessing individual subsurface properties. 
# 
# ```{figure} images/L5_f1.png
# ---
# scale: 70%
# align: center
# name: aquifer-het
# ---
# Aquifer Heterogeneity
# ```

# ## Heterogeneity 
# 
# A solid or a porous medium is **homogeneous** if its property do not vary in space. In contrast, the porous medium is **heterogeneous**, or also sometime termed inhomogeneous, if at least one of its properties varies in space. In groundwater studies, heterogeneity or homogeneity is generally associated with hydraulic conductivity $(K)$ of the aquifer. In many practical applications, properties such as strativity and porosity are treated as spatially constant or homogeneous. This is usually done for two reasons:
# 
# - the spatial variability of hydraulic conductivity is much more pronounced than that of storativity and porosity, and
# - very limited data are available of the spatial variability of storativity and porosity. 
# 
# Thus, an aquifer is:
# 
# > homogeneous if $K (x, y, z) = K$, and 
# 
# > heterogeneous if $K (x, y, z) \neq K$
# 
# For heterogeneous aquifer it is not required that $K$ is varying in all directions, i.e., varying of $K$ can be restricted to one or two spatial coordinates. 
# 
# Heterogeneity in aquifer can exist in many configurations. But they are broadly categorized to the following three classes:
# 
# > **layered heterogeneity**: common in sedimentary systems and unconsolidated deposits.
# 
# > **discontinuous heterogeneity**: due to presence of faults, e.g., at the contact between overburden-bedrock.
# 
# > **trending heterogeneity**: Common in the aquifers with active sedimentation processes
# 
# Aquifer properties such as storativity and porosity are affected by heterogeneity but they are often considered spatially constant in practical applications. This is because
# 
# - The spatial variability of hydraulic conductivity is much more pronounced than any other aquifer property, and
# 
# - Only limited spatial variability data are available for storativity or porosity. 
# 
# Heterogeneity play a significant role in controlling the flow of groundwater, but its quantification is more relevant to the transport of chemicals in groundwater. 

# ### Effective Hydraulic Conductivity
# 
# It is possible to represent the spatial distribution of
# hydraulic conductivity in a heterogeneous aquifer by an _average_
# value such that steady-state groundwater discharge remains the
# same as in the heterogeneous case. Such obtained _average_ $K$ value is termed as **effective hydraulic conductivity**. In other words, it can be mentioned that the effective hydraulic conductivity characterizes a
# fictitious homogeneous aquifer with the same discharge and the
# same overall head difference under steady-state conditions as some
# heterogeneous aquifer to be investigated.
# 
# The quantification of _effective hydraulic conductivity_ is straight-forward for perfectly layered systems, which can be seen as an idealized representation of natural layering. In more natural systems with complex heterogeneous configurations, cumbersome mathematical derivations are required to obtain effective $K$. 
# 
# In the next few sections, effective hydraulic conductivity for ideal layered system is derived.

# ## Layered Systems
# 
# ### Case I - Flow Parallel to Layering 
# 
# A confined aquifer consisting of $n$ layers is considered. In the set-up (see {numref}`flow-parallel`), the layer boundaries are parallel to each other and groundwater flow is parallel to the layering.
# 
# 
# ```{figure} images/L5_f2.png
# ---
# scale: 50%
# align : center
# name: flow-parallel
# ---
# Flow parallel to layering
# ```
# 
# The analysis is required to consider the aquifer as a _single entire aquifer unit_ and a set of _layered aquifer unit_. Data of both units are to be considered. 
# 
# 
# ````{panels}
# :body: text-justify
# :header: text-center
# 
# **Data for a single entire aquifer unit are:**
# ^^^
# - $W$ = width (extension perpendicular to cross-section, see figure)
# 
# - $L$ = flow distance along the layer
# 
# - $\Delta h$ = total head loss corresponding to flow length
# 
# - Q = the total discharge. 
# 
# ---
# 
# **Data for set of layered aquifer unit are:**
# ^^^
# - $i$ = layer numbers $(i = 1,2,3 ..., n)$
# 
# - $m_i$ = thickness of $i^{th}$ layer
# 
# - $K_i$ = conductivity of $i^{th}$ layer
# ````
# 
# With these informations available, using volumetric budget and Darcy's law the _effective hydraulic conductivity_ $K$ can be quantified from the following steps:
# 
# I. Total thickness: $m = \sum\limits_{i=1}^n m_i$
# 
# II. Volumetric budget: $Q =  \sum\limits_{i=1}^n Q_i$
# 
# III. Head loss in $i^{th}$ layer: $\Delta h_i = \Delta h$
# 
# IV. Darcy's law for $i^{th}$ layer: $Q_i = - wm_iK_i\frac{\Delta h}{L} $ 
# 
# V. Darcy's law for the homogeneous aquifer to replace the layered system: $Q = -wmK\frac{\Delta h}{L}$
# 
# 
# ```{note}
# As flow is parallel to the layering, the head loss in individual layer equals the total head loss (step. 3)
# ```
# 
# Summing the discharge in each layer (step 4) will result to the discharge of the homogeneous aquifer (step 5), i.e., we can equate step 4 and step 5 as:
# 
# $$
# - w \cdot m \cdot K \cdot \frac{\Delta h}{L} = \sum\limits_{i=1}^n\bigg(- w \cdot m_i \cdot K_i\cdot\frac{\Delta h}{L}\bigg)
# $$
# 
# Constant quantities from the right-hand side can be taken out of summation and equated with the left side. This leads to:
# 
# $$
# {- w}\cdot m \cdot K \cdot \frac{\Delta h}{L} = {- w} \cdot \frac{\Delta h}{L} \cdot \sum\limits_{i=1}^n( m_iK_i)
# $$
# providing
# 
# $$
# m\cdot K = \sum\limits_{i=1}^n( m_iK_i)
# $$
# 
# As a result, the effective hydraulic conductivity of a layered system when the flow is parallel to the layering equals
# 
# $$
# K = \frac{\sum\limits_{i=1}^n(m_i K_i)}{m}
# $$
# 
# In the above equation, effective hydraulic conductivity $K$ is obtained as the _weighted arithmetic average_ of layer conductivities $K_i$. Weights correspond to relative thickness $m_i/m$. Thus, the _largest term_ in the sum contributes most to the arithmetic average. Thus, the effective hydraulic conductivity $K$ can be approximated from
# 
# $$
# K \approx \frac{\max (m_i\cdot K_i)}{m}
# $$

# ### Example problem  ###
# 
# ```{admonition} Flow parallel to layering
# Calculate the effective hydraulic conductivity of the layer system consisting of 3 layers if the flow is parallel to the stratification.
# 
# ```

# In[1]:


print("\033[1m Provided are: \033[0m \n")

#Thickness of i-th layer [m]
m1 = 3 
m2 = 2.5
m3 = 1.75

#conductivity of i-th layer [m/s]
K1 = 3.5e-3
K2 = 2e-2
K3 = 5e-4
print("thickness of layer 1 = {}".format(m1), "m\nthickness of layer 2 = {}".format(m2),"m\nthickness of layer 3 = {}".format(m3), "m\n\nconductivity of layer 1 = {:02.1e}".format(K1),
      "m/s\nconductivity of layer 2 = {:02.1e}".format(K2), "m/s\nconductivity of layer 3 {:02.1e}".format(K3), "m/s")


# In[2]:


import numpy as np

#Thickness of i-th layer [m]
m1 = 3 
m2 = 2.5
m3 = 1.75

#conductivity of i-th layer [m/s]
K1 = 3.5e-3
K2 = 2e-2
K3 = 5e-4

#intermediate calculation
m = m1+m2+m3

#solution
K = (m1*K1+m2*K2+m3*K3)/m

print("\n\033[1mSolution:\033[0m\nThe resulting hydraulic conductivity of the layer system is \033[1m{:02.1e} m/s\033[0m.".format(K))


# ### Case 2 - Flow Perpendicular to Layering
# 
# In the second case the the flow _perpendicular_ to the layering is considered. Just as in the _parallel_ flow case, the aquifer in this case also is a confined aquifer with $n$ layers (see {numref}`flow-perpendicular`).
# 
# ```{figure} images/L5_f3.png
# ---
# scale: 50%
# align : center
# name: flow-perpendicular
# ---
# Flow perpendicular to layering
# ```
# 
# ````{panels}
# :body: text-justify
# :header: text-center
# 
# **Data for a single entire aquifer unit are:**
# ^^^
# - $A$ = total cross-sectional area
# 
# - $\Delta h$ = total head loss
# 
# - $Q$ = total discharge
# 
# -------
# And, the available data for the _layered units_ are:
# ^^^^^
# - $i$ = layer number $i$ $(i = 1,2,3, \ldots, n)$
# 
# - $m_i$ = thickness of $i^{th}$ layer
# 
# - $K_i$ = Hydraulic conductivity of $i^{th}$ layer
# ````
# 
# These data combined with _equation of continuity_ and _Darcy's Law_ can be used to obtain the effective hydraulic conductivity of the system in which flow is perpendicular to the layers. The following steps are required:
# 
# I. Total thickness: $m = \sum\limits_{i=1}^n m_i $
# 
# II.   Equation of continuity: $Q_i = Q$
# 
# II.  Cross-sectional area for layer: $A_i = A $
# 
# IV. Decomposition of head loss: $\Delta h = \sum\limits_{i=1}^n \Delta h_i $
# 
# V. Darcy's law for layer $i$:
# 
# $$Q_i = - A_i K_i \frac{\Delta h_i}{m_i}$$
# 
# $$\Delta h_i = -\frac{Q_i m_i}{A_i K_i} = - \frac{Q m_i}{A K_i}$$
# 
# VI. Similarly the Darcy's law for the homogeneous aquifer to replace the layered system: 
# 
# $$Q = - A K \frac{\Delta h}{m}$$
# 
# $$\Delta h = - \frac{Q m}{A K }$$
# 
# VII. The head loss from step 4 can be equated with the sum of head loss of each layered unit (from step 5), i.e.,
# 
# $$
# \frac{Q\cdot m}{A\cdot K}
# =\sum\limits_{i=1}^n\frac{Q\cdot m}{A\cdot K}
# $$
# 
# The constants $Q$ and $A$ can be taken out of the summation, this leads to
# 
# $$
# \frac{ {-Q}\cdot m}{ A\cdot K}
# =\frac{ {-Q}}{A}\sum\limits_{i=1}^n\frac{m_i}{K_i}
# $$
# 
# As a result, the effective hydraulic conductivity of a layered system for a flow perpendicular to the layering equals
# 
# $$
# K = \frac{m}{\sum\limits_{i=1}^n\frac{m_i}{K_i}}
# $$
# 
# In the above equation, effective hydraulic conductivity $K$ is obtained as the _weighted harmonic average_ of layer conductivities $K_i$. Weights
# correspond to relative thicknesses $m_i/m$. Thus, the largest term in the sum contributes most to
# the harmonic average and therefore, the effective hydraulic conductivity can be approximated from
# 
# $$
# K \approx \frac{m}{{\max\big(\frac{m_i}{K_i}}\big)}
# $$
# 

# ### Example problem  ###
# 
# ```{admonition} Flow perpendicular to layering
# Calculate the effective hydraulic conductivity of the layer system consisting of 3 layers if the flow is perpendicular to the layering.
# ```

# In[3]:


print("\033[1m Provided are:\033[0m")

#Thickness of i-th layer [m]
m1 = 3 
m2 = 2.5
m3 = 1.75

#conductivity of i-th layer [m/s]
K1 = 3.5e-3
K2 = 2e-2
K3 = 5e-4

print("thickness of layer 1 = {}".format(m1), "m\nthickness of layer 2 = {}".format(m2),"m\nthickness of layer 3 = {}".format(m3), "m\n\nconductivity of layer 1 = {:02.1e}".format(K1),
      "m/s\nconductivity of layer 2 = {:02.1e}".format(K2), "m/s\nconductivity of layer 3 {:02.1e}".format(K3), "m/s")


# In[4]:


#Thickness of i-th layer [m]
m1 = 3 
m2 = 2.5
m3 = 1.75

#conductivity of i-th layer [m/s]
K1 = 3.5e-3
K2 = 2e-2
K3 = 5e-4

#intermediate calculation
m = m1+m2+m3

#solution
K = m/(m1/K1+m2/K2+m3/K3)


print("\n\033[1mSolution:\033[0m\nThe resulting hydraulic conductivity of the layer system is \033[1m{:02.1e} m/s\033[0m.".format(K))


# ### Summary: Effective Conductivity of Layered Aquifers ###
# 
# - **For flow parallel to layering:** <br>
# Effective hydraulic conductivity equals the _weighted arithmetic mean_ of layer conductivities.
# 
# - **Flow perpendicular to layering:** <br>
# Effective hydraulic conductivity equals the _weighted harmonic mean_ of layer conductivities.
# 
# - **Weights** in both cases are given by relative layer thicknesses $m_i/m$
# 
# - It can be mathematically shown that the harmonic mean of a set of
# positive numbers cannot exceed the arithmetic mean of the same set. Both means are identical only if all numbers in the set are identical.
# Apart from this very special case, we have 
# 
# 
# ```{Note}
# > ***_harmonic mean < arithmetic mean._*** 
# ```
# 
# This implies that the flow direction perpendicular to the layering is associated with a smaller effective hydraulic conductivity than the flow direction parallel to the layering.
# 
# 
# 

# ## Hydraulic Resistance 
# 
# The _Hydraulic Resistance_ $(R)$ provide an alternative approach to express conductivity. It is defined as a reciprocal to hydraulic conductivity $(K)$, i.e.,
# 
# $$
# R = \frac{1}{K}
# $$
# 
# This implies that large $K$ corresponds to small $R$ and vice-versa. Considerations about effective hydraulic conductivities of layered
# aquifers can be transferred to hydraulic resistances by recalling
# that the arithmetic mean of positive numbers coincides with the
# harmonic mean of reciprocal numbers and vice versa. This can be used in the following manner:
# 
# - **For _flow parallel to layering_:**
# 
# As Effective hydraulic conductivity equals the weighted arithmetic mean of layer conductivities, the reciprocal of this, i.e., the effective hydraulic resistance, will equal the weighted harmonic mean of layer resistances.
# 
# Furthermore, if all layer thicknesses are identical $(m_i =$ const.) and flow is parallel to layering, the largest discharge passes through the layer with
# highest hydraulic conductivity (smallest hydraulic resistance). In this case, the discharge through each layer is proportional to layer conductivity or inversely proportional to layer resistance.
# 
# - **For _flow perpendicular to layering_:**
# 
# In this case the effective hydraulic conductivity equals the weighted harmonic
# mean of layer conductivities. This leads to Effective hydraulic resistance equaling the weighted arithmetic mean of layer resistances.
# 
# Similar to the _flow parallel to the layering,_ if all layer thicknesses are identical ($m_i =$ const.) and flow is perpendicular to layering, the largest hydraulic gradient is across the layer with lowest hydraulic conductivity (highest hydraulic resistance). In this case, the _head gradient_ across each layer is proportional to layer resistance or inversely proportional to layer conductivity.

# ### Example problem  ###
# 
# ```{admonition} Hydraulic Resistance
# Find the hydraulic resistance with the given hydraulic counductivity
# ```

# In[5]:


print("\033[1m Provided are:\033[0m \n")
K = 5e-4 # m/s, hydraulic conductivity
print("Hydraulic conductivity = {:02.1e} m/s".format(K))


# In[6]:


K = 5e-4 # m/s, hydraulic conductivity
#solution
R = 1/K
print("\n\033[1mSolution:\033[0m\n\nThe resulting hydraulic resistance is \033[1m{:02.1e} s/m\033[0m.".format(R))


# ## Aquifer Anisotropy
# 
# A solid or a porous medium is **isotropic** if its (all) properties are independent of _direction._ Conversely, a solid or a porous medium is **anisotropic** if at least one of its property is dependent on direction. Thus, isotropic (or anisotropic) property of porous media refines the concept of homogeneity (or heterogeneity). The key difference being that anisotropy of aquifer is associated only with hydraulic conductivity as other aquifer properties like storativity or porosity cannot depend on direction. Groundwater flow (and more so solute transport) is affected by anisotropy. However, in unconsolidated aquifers the impact of heterogeneity is usually more important.
# 
# Figure below ({numref}`Iso-Anisotropy`) explains the concept of isotropy more clearly. The direction dependency of $K$ is represented by the arrows diagram.
# 
# ```{figure} images/L5_f4.png
# ---
# scale: 40%
# align : center
# name: Iso-Anisotropy
# ---
# Isotropy and Anisotropy in aquifers
# ```
# 
# ### Anisotropy and scale effects
# 
# The effective hydraulic conductivity of layered aquifers was shown earlier to depend on the orientation of the flow direction relative to layering, i.e., parallel versus perpendicular. On a larger scale, it may not be possible to identify or resolve heterogeneities associated with example thin layers, small lenses, shape and orientation of grains (see figure above). Nevertheless, $K$ is found to be direction-dependent when groundwater flow is quantified at the larger scale. In these case, small-scale heterogeneity (e.g., due to layering) expresses itself as anisotropy of hydraulic conductivity at the larger scale.

# ### Indices and functional arguments to describe anisotropy
# 
# One could consider heterogeneity as a property of entirety. While function arguments point towards heterogeneity, _indices_ are
# used to express that hydraulic conductivity depends on direction. Considering a 3-D Cartesian coordinate system, the directional dependent hydraulic conductivity can be represented by $K_x$, $K_y$ and $K_z$ in parallel with the $x-$, $y-$ and $z-$axis, respectively. Within these, one could distinguish between horizontal conductivities ($K_x$ and $K_y$) with the vertical conductivity $K_z$. More often, anisotropy is observed only between horizontal and vertical directions (i.e., along $x$ or $y$ and $z$ directions), while isotropy is observed along horizontal directions ($x$ and $y$ direction). Thus, symbols $K_h$ representing $K_x = K_y$ and $K_v$ representing $K_z$ can be used to denote horizontal and vertical hydraulic conductivity, respectively. 
# 
# ### Concept of the hydraulic conductivity ellipse
# 
# Let us consider an aquifer with horizontal conductivity $K_h$ and vertical hydraulic conductivity $K_v$. Let us assume that the flow in the aquifer is in some arbitrary direction characterized by the angle $\theta$ between the flow direction and horizontal plane (see {numref}`K-ellipse`). 
# 
# ```{figure} images/L5_f5.png
# ---
# scale: 55%
# align : center
# name: K-ellipse
# ---
# hydraulic conductivity ellipse
# ```
# 
# In this case, it can be shown that the effective hydraulic conductivity $K$ is
# 
# $$
# K = \frac{1}{\frac{\cos^2\theta}{K_h}+\frac{\sin^2\theta}{K_v}} 
# $$
# 
# If the angle $\theta$ is varied, the above equation defines an ellipse (also called "hydraulic conductivity ellipse") with semi-axes equal to $\surd{K_h}$ and $\surd{K_v}$, respectively. The square root of $K$ can be visualised by the length of a line segment parallel to the direction of flow. This line segment extends from the centre to the perimeter of the ellipse.

# ### Example problem  ###
# 
# ```{admonition} Hydraulic Resistance
# Find resulting hydraulic conductivity from provided horizontal and vertical conductivities.
# ```

# In[7]:


print("\n\033[1mProvided are:\033[0m\n")
Kh =  1e-3 #horizontal hydraulic conductivity [m/s]
Kv =  1e-4 #vertical hydraulic conductivity [m/s]
theta = 50 #angle between flow direction ans horizontal plane [°]
print("horizontal hydraulic conductivity = {:02.1e}".format(Kh), "m/s\n" "vertical hydraulic conductivity = {:02.1e}".format(Kv), "m/s\n"
      "angle = {}°\n".format(theta))


# In[8]:


#solution
K = 1 /((np.cos(theta)**2/Kh)+(np.sin(theta)**2/Kv))


print("\033[1mSolution:\033[0m\n\nThe resulting hydraulic conductivity is \033[1m{:02.1e} m/s\033[0m.".format(K))


# ## Combining Heterogeneity and Anisotropy
# 
# The distinction between_Homogeneous, Heterogeneous, isotropic and anisotropic aquifer or any combination of them can be more clearly understood from the figure (for vertical $x-z$ plane).
# 
# ```{figure} images/L5_f6.png
# ---
# scale: 55%
# align : center
# name: Het_Aniso
# ---
# Heterogeneity and Anisotropy in aquifer
# ```

# ## Chapter Quiz

# In[9]:


from jupyterquiz import display_quiz
import json
with open("L5Q.json", "r") as file:
    questions=json.load(file)
    
display_quiz(questions)


# In[ ]:





# In[ ]:




