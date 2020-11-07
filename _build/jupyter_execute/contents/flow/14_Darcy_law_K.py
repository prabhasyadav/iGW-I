#!/usr/bin/env python
# coding: utf-8

# # Lecture 4 - Darcy's Law and Conductivity

# ## Energy and hydraulic head  ## 
# 
# In the last section we learned that _hydrostatic pressure difference_ $p(z)$ will not allow the fully quantify water flow. In fact in addition to $p(z)$ other form of energy must also be considered. 
# 
# The energy available for groundwater flow is given the name _hydraulic head_ $(h)$ or also called _piezometric head_:. It consists of three components, related to 
# 
# > **elevation, 
# pressure and 
# velocity**. 
# 
# The total energy head is expressed by the equation
# 
# $$
# h = z + \frac{p}{\rho g} + \frac{v^2}{2g}
# $$
# 
# where, <br>
# $z$ is the _elevation_ or _datum head_ [L], <br>
# $p$ is the _pressure_
# exerted by water column [M L$^{-1}$ T$^{-2}$],<br> 
# $\rho$ is the density of fluid [M L$^{-3}$],<br> 
# $g$ is the acceleration due to gravity [LT$^{-2}$], and <br> 
# $v$ is velocity of flow [LT$^{-1}$].
# 
# Note that the $h$ has the dimension of length [L].  In groundwater flow, the velocity is so low
# that the energy contained in velocity can be neglected when computing the total energy.
# Thus, the hydraulic head (as represented in Figure **@ALEX link it pls.**) is written as
# 
# $$
# h = z + \frac{p}{\rho g} 
# $$
# 
# The above equation says that Water flow is governed by differences in hydraulic head and not by differences in pressure head alone.
# 
# It is to be noted that $z$ depends on the orientation. In the above equation $+z$ is considered oriented upward (based on conventional sign convention). If $z-$axis is oriented downwards, we have
# 
# $$
# h = \frac{p}{\rho g}-z 
# $$
# 

# ## Hydraulic head and discharge - when there is no discharge ##
# 
# Consider the figure below:
# 
# <a href="fig1"></a><img src="images/L4_f1.png" alt="Hydraulic Head" width="600" height="1000">
# 
# 
# The pressure head: $p(z) = p_L + \rho \cdot g \cdot (L-z)$ <br>
# The hydraulic head (piezometric head): $h(z) = \frac{p(z)}{\rho \cdot g } + z = \frac{p_L + \rho \cdot g \cdot (L-z) }{\rho \cdot g } + z = \frac{p_L}{\rho \cdot g}+ L = \text{Const}$<br>
# 
# In the figure above the hydraulic head difference between two points ($z=0$ and $z=L$) are exactly equal, i.e., $\Delta h = 0$. This refers to the system with no energy gradient and hence a _no flow_ system. 

# ## Hydraulic head and discharge - when there will be a discharge ##
# 
# Now consider the figure below
# 
# <a href="fig2"></a><img src="images/L4_f2.png" alt="Hydraulic Head II" width="400" height="1000">
# 
# Here there is clear difference between the elevation head ($z_1$ and $z_2$), which is taken from a reference level ($z=0$ in this case. Average Sea Level (ASL), is often use for this reference). Also differing are pressure heads ($p_1$ and $p_2$). Therefore, the $h(z)$ in this case are:
# 
# $$
# \begin{align}
# h_1 &= \frac{p_1}{\rho \cdot g} + z_1 \\
# h_2 &= \frac{p_2}{\rho \cdot g} + z_2
# \end{align}
# $$
# 
# As can be observed from the figure, in this case $h_1<h_2$. Thus, analogus to flow of energy - i.e., from higher energy level to the lower energy level, the flow in this example case is from cross-section 2 towards cross section 1.
# 
# It is to be noted that the _magnitude_ of the hydraulic head ($h$) rather than the _orientation_ of the set-up determines the direction of discharge.
# 
# Also, important to note is that the _differences of hydraulic head_ $(\Delta h)$ is independent of of the position of the origin of the reference axis  ($z$-axis in the above case).

# **@Anne/@Sophie - pls add a numerical problem here. Pls. check at the botton of the page problems suggested by Prof. Chahar. Pls. note that the problem should be a few line codes.**

# ## Darcy's Law
# 
# Groundwater in its natural state is invariably moving. This movement is governed by
# established hydraulic principles. Darcy's Law is a phenomenologically derived
# constitutive equation that describes the flow of a fluid through a porous medium.
# Darcy's Law along with the equation of conservation of mass is equivalent to the
# groundwater flow equation, one of the basic relationships of hydrogeology. It is also
# used to describe oil, water, and gas flows through petroleum reservoirs.
# 
# The law was formulated by Henry Darcy (Darcy, 1856) based on the results of experiments on the flow
# of water through beds of sand (Figure **@Alex pls. link fig. L4_f3.png**)  shows a schematic setup). In the experiments, _area of cross section_  ($A$ [L$^2$] $= \text{Const}$) was kept constant. Constant discharge ($Q= \text{Const}$) was applied and the sand medium was fully saturated, i.e., voids between sand grains were completely filled with water.
# 
# <a href="fig3"></a><img src="images/L4_f3.png" alt="Darcy's Set-up" width="400" height="600">

# From the experiments Darcy observed that the _volume of water per unit time_ passing through a porous medium
# 
# - is _directly proportional_ to the  $A$ [L$^2$] and the head difference between inlet and outlet $(h_1 – h_2)$ [L], and 
# - is inversely proportional to the _length of the medium_ $L$ [L] 
# 
# i.e.,
# 
# $$
# \frac{\text{Vol}}{t}= Q \propto A (h_1 - h_2)\frac{1}{L}
# $$
# 
# which in terms of specific discharge $q$, or discharge velocity or Darcy velocity $v$ [LT$^{-1}$] is
# 
# $$
# q = v = \frac{Q}{A}= - K\frac{\partial h}{\partial L} = - K\,i
# $$
# 
# where constant of proportionality $K =$ _hydraulic conductivity_ [LT$^{-1}$]; and $i = \partial h/ \partial L =$
# _hydraulic gradient_ = rate of head loss per unit length of medium [ ]. It iThe _negative sign_
# indicates that the total head is decreasing in the direction of flow because of friction or
# resistance

# **@Anne/@Sophie - pls add a numerical problem here. Pls. check at the botton of the page problems suggested by Prof. Chahar. Pls. note that the problem should be a few line codes.**

# Darcy's law is a simple mathematical statement which neatly summarizes several
# familiar properties that groundwater flowing in aquifers exhibits, including: 
# > 1.  if there
#  is no hydraulic gradient (difference in hydraulic head over a distance), no flow occurs
#  (this is hydrostatic conditions), 
# 
# > 2. if there is a hydraulic gradient, flow will occur from
#  a high head towards a low head (opposite the direction of increasing gradient, hence the
# negative sign in Darcy's law), 
# 
# > 3.  the greater the hydraulic gradient (through the same
# aquifer material), the greater the discharge, and 
# 
# > 4.  the discharge may be different
# through different aquifer materials (or even through the same material, in a different
# direction) even if the same hydraulic gradient exists.

# ### Darcy's law and analogous physical systems ###
# 
# Darcy's law is analogous to pipe flow in which energy is dissipated over the distance to overcome frictional loss resulting
# from fluid viscosity. 
# 
# It also forms the scientific basis of permeability used in the earth
# sciences. 
# 
# It may be noted Darcy's law is analogous to Fourier's law in the field of heat conduction, Ohm's law in the field of electrical networks, or Fick's law in diffusion theory.

# ## Hydraulic Conductivity and Intrinsic Permeability ##

# _Hydraulic Conductivity ($K$)_ appeared in the Darcy's law as a constant of proportionality, i.e., it is the fundamental quantity that is required to describe groundwater flow. Therefore we illustrate this further,
# 
# A medium has a _unit hydraulic conductivity_ if it will transmit in _unit time_ a _unit volume of groundwater_ at the prevailing kinematic viscosity through a cross section of _unit area_ measured at _right angles_ to the direction of flow, under a _unit hydraulic gradient_. 
# 
# The hydraulic conductivity of a soil or rock depends on a variety of
# physical factors, important ones are:
# - porosity, 
# - particle size and distribution, 
# - shape of particles,
# - arrangement of particles.
# 
# Also, hydraulic conductivity is depends on the property of the fluid e.g., density, viscosity 
# 
# In general for unconsolidated porous media,$K$ varies with _square_ of particle size; clayey materials exhibit low values of $K$, whereas
# sands and gravels display high values
# 
# Typical values for hydraulic conductivity (see figure XX for more comprehensive listing):
# 
# | Media Type      | hydraulic conductivity (m/s) |
# | ----------- | ---: |
# | Gravel     | $10^{-2} – 10^{-1}$ |
# | coarse sand   | $\approx 10^{-3}$ |
# | medium sand   | $10 ^{-4} – 10^{-3}$ |
# | fine sand  | $10^{-5} – 10^{-4}$        |
# | Silt  | $10^{-9}  – 10^{-6} $     |
# | Clay  | $< 10^{-9} $     |

# **@Anne/@Sophie - pls add a numerical problem here. Pls. check at the botton of the page problems suggested by Prof. Chahar. Pls. note that the problem should be a few line codes.**

# ### Obtaining Hydraulic Conductivities ###
# 
# The hydraulic conductivity depends on properties of the fluid (density, viscosity,
# temperature) and on properties of the porous medium (effective porosity, grain size
# distribution). It can be obtained by calculation from formulas, laboratory methods, or
# field tests
# 
# The laboratory method can be indirect method or direct method. For example,
# determination of the hydraulic conductivity based on the evaluation of sieve analysis
# data is the indirect laboratory method. On the other hand, the direct method of
# determination of the hydraulic conductivity (e.g. permeameter) is based on some version of Darcy‘s experiment. Advantages of laboratory methods include controlled
# conditions, small sample size (easy handling), lower costs, larger number of
# experiments, etc. While, the disadvantages of laboratory methods are disturbed
# samples, additional pathways at column walls, small sample size (randomly high or low
# K), flushing of fine material, etc.

# #### Hydraulic Conductivities estimations from Sieve analysis ####
# 
# Sieve analysis data can be evaluated to estimate hydraulic conductivity of
# unconsolidated media. There are several _empirical methods_. The simplest one dates back to Hazen (1892):
# 
# $$
# K = 0.0116 \cdot d_{10}^2
# $$
# 
# 
# where, $d_{10}$ = grain diameter (mm) corresponding to $10
# \%$ of cumulative mass fraction. It can be generalized by including temperature ($\theta$ in $^\circ$C). Thus the Hazen formula becomes
# 
# 
# $$
# K = 0.0116 \cdot d_{10}^2 \cdot (0.7 + 0.03\cdot\theta)
# $$
# 
# Hazen's formula is only valid for the indicated units, i.e., conversion of the _unit_ may be required before using the formula.

# **@Anne/@Sophie - pls add a numerical problem here. Pls. check at the botton of the page problems suggested by Prof. Chahar. Pls. note that the problem should be a few line codes.**

# #### Hydraulic Conductivities estimations from Darcy's Law ####
# 
# **Permeameter** is an instrument used to determine hydraulic conductivity of soil samples
# in the laboratory as _direct method_. The design of permeameters is based on Darcy‘s
# experiment. 
# 
# (**@Alex this figure can go on the right side of the text**)
# 
# <a href="fig4"></a><img src="images/L4_f4.png" alt="Permeameter" width="250" height="600">
# 
# There are mainly two types of permeameters
# 1. Constant-head permeameter, and 
# 2. Falling-head permeameter. 
# 

# In **constant-head permeameters* as
# shown in Figure **(@ALEX pls. fix the link)**, the hydraulic heads at inflow and outflow of the Darcy column are
# constant in time. As a consequence, the discharge is not changing with time. 
# 
# <a href="fig5"></a><img src="images/L4_f5.png" alt="Constant-head-Permeameter" width="250" height="600">
# 
# The
# hydraulic conductivity can be obtained by observing discharge and heads and then
# substituting in the below formula that is rearranged form of Darcy’s law from:
# 
# $$
# K = \frac{QL}{A(h_{in}- h_{out}}
# $$
# 
# where $Q$ =discharge[L$^3$T$^{-1}$];<br>
# $L$ = length of sample [L]; <br> $A$ = cross-sectional area of sample [L$^2$]; <br>
# $h_{in}$ = hydraulic head at column inlet [L];<br>
# $h_{out}$ = hydraulic head at column outlet [L];<br>
# $\Delta h$ = $h_{in} - h_{out}$
# 
# $h_{out}$ can be set equal to zero as only head differences are important.

# @Anne/@Sophie - pls add a numerical problem here. Pls. check at the botton of the page problems suggested by Prof. Chahar. Pls. note that the problem should be a few line codes.

# In falling-head permeameter as shown in Figure **(@Alex, pls. fix the link)** the hydraulic head at the outflow of
# the Darcy column is not changing, but the hydraulic head at the inflow is decreasing
# with time. 
# 
# <a href="fig6"></a><img src="images/L4_f6.png" alt="Falling-head-Permeameter" width="250" height="600">
# 
# As a result, the discharge also decreases with time. Rewriting Darcy's law for a small time interval
# 
# $$
# K \frac{\pi d_c^2}{4}\big(h_{in} - h_{out}\big)\frac{1}{L}\text{d}t = \frac{\pi d_t^2}{4}\text{d}h 
# $$
# 
# $K$ can be obtained from the above equation by separating the variables and then integrating. The resulting expression for $K$ will be
# 
# $$
# K = \frac{d_t^2 L}{d_c^2}\ln \Bigg(\frac{h_{in}(0) - h_{out}}{h_{in}(t)-h_{out}}\Bigg)
# $$
# 
# where, <br>
# $L$ = length of sample [L];<br> 
# $d_c$ = diameter of sample cylinder [L];<br>
# $d_t$ = diameter of piezometer tube [L]; <br>
# $h_{in}(0)$ = initial hydraulic head at column inlet [L]; <br>
# $h_{in}(t)$ = final hydraulic head at column inlet [L]; <br> 
# $h_{out}$ = hydraulic head at column outlet [L]; <br>
# $h_0 = h_{in}(0) - h_{out}$; <br> 
# $h = h_{in}(t) - h_{out}$
# 
# and $h_{out}$ can be set equal to zero as only head differences are
# important. The hydraulic conductivity can be obtained from the above equation using observed time and corresponding heads. Larger experimental time periods are needed for the falling-head permeameter, in particular if hydraulic conductivity is low. On the other hand, no measurement of discharge or water volume is required.

# **@Anne/@Sophie - pls add a numerical problem here. Pls. check at the botton of the page problems suggested by Prof. Chahar. Pls. note that the problem should be a few line codes.**

# **Field methods** of determination of the hydraulic conductivity include tracer tests, auger hole tests, pumping tests of wells, etc. Field experiments are much more complicated and expensive than laboratory tests. Resulting hydraulic conductivities represent averages over an aquifer volume, which is covered by the experiment. The size of this
# volume depends on subsurface properties and on the experimental method used.

# ### Intrinsic Permeability ###
# 
# A convenient alternative is to write Darcy's equation in a form of **intrinsic permeability**
# where the properties of the medium and the fluid are represented explicitly
# 
# $$
# v = \frac{-k \cdot \rho\cdot g}{\mu}\frac{\partial h}{\partial L}
# $$
# 
# where, $k$ is the intrinsic permeability [L$^2$], and $\eta$ is the dynamic viscosity of fluid [ML$^{-1}$T$^{-1}$] e.g., (Pa-S). The relation between _hydraulic conductivity_ _intrinsic permeability_, therefore, is
# 
# $$
# K = k\cdot \frac{ \rho \cdot g}{\eta}
# $$
# 
# In terms of Kinematic viscosity [L$^2$T$^{-1}$}], $\eta = \rho \cdot \nu$, the above relation becomes
# 
# $$
# K = k\cdot \frac{ g}{\nu}
# $$
# 
# Both density and viscosity are temperature dependent quantites. Their values in field conditions $\approx 10 ^\circ$C and in the laboratory conditions $\approx 20 ^\circ$C are:
# 
# 
# |                            | 10°C        | 20°C         |
# |----------------------------|-------------|--------------|
# | density (kg/m$^3$)      | 999.7       | 999.7        |
# | kinematic viscosity (m$^2$/s) | 1.3101·10$^{-6}$ | 1.0105·100$^{-6}$ |
# | ynamic viscosity (Pa$\cdot$s)  | 1.3097·10$^{-3}$ | 1.3097·100$^{-3}$  |
# |||
# 
# 
# The _intrinsic permeability_ can be written in terms of specific weight or weight density [ML$^{-2}$T$^{-2}$] (or in metric unit- N/m$^3$), $\gamma = \rho\cdot g$ as
# 
# $$
# k = \frac{\eta}{\gamma}K
# $$

# **@Anne/@Sophie - pls add a numerical problem here. Pls. check at the botton of the page problems suggested by Prof. Chahar. Pls. note that the problem should be a few line codes.**

# ### Properties of Intrinsic Permeability ###
# 
# - The value of intrinsic permeability of a porous medium
# equals 1 m$^2$ if a fluid with dynamic viscosity of 1 Pa$\cdot$s can pass through the porous
# medium at a Darcy velocity of 1 m/s under a hydrostatic pressure gradient of 1 Pa/m
# (horizontal flow).
# 
# - The intrinsic permeability is _independent_ of the fluid moving through the medium and depends only upon the medium properties. Intrinsic
# permeability of unconsolidated porous media is roughly proportional to the square of
# the pore diameter.
# 
# - The intrinsic permeability is used primarily when the density or the viscosity of the
# fluid varies with position.
# 
# - The dimension of $k$ is [L$^2$], but when expressed in m$^2$ is so small that square
# micrometers ($\mu$ m)$^2  = 10^{-12}$ m$^2$ is used. In the petroleum industry it is expressed in **Darcy**
# (symbol: D) with conversion factor to SI units is:  1 D $= 0.987\cdot 10^{-12}$ m$^2$. 
# 
# - Intrinsic permeability for a weakly , well and
# highly permeable aquifers vary in the range 10$^{-4}$ to 10$^{-1}$ D, 10$^{-1}$ to 10$^2$ D, and $> 10^2$ D
# respectively
# 
# - Typical value of conductivity and intrinsic permeability is  provided in the fig (from Todd and Mays, 2004) below.
# 
# 
# <a href="fig7"></a><img src="images/L4_f7.png" alt="K and k" width="700" height="600">

# ## Darcy velocity and Interstitial velocity ##
# 
# Darcy velocity $v$ is the _apparent velocity_ or _fictitious velocity_ or _Darcy flux_ (discharge per
# unit area). This value of velocity, often referred to as the _apparent velocity_, is not the
# velocity which the water traveling through the pores is experiencing. The velocity $v$ is
# referred to as the Darcy velocity because it assumes that flow occurs through the entire cross section of the material without regard to solids and pores. Actually water can flow
# though pores only and the pore spaces vary continuously with location within the
# medium. Therefore the actual velocity is nonuniform, involving endless accelerations,
# deceleration, and changes in direction. To define the _actual flow velocity_ or **interstitial
# velocity**, one must consider the microstructure of the rock material. 
# 
# For naturally occurring geologic materials, the microstructure cannot be specified three-
# dimensionally; hence, actual velocities can only be quantified statistically.
# 
# <a href="fig8"></a><img src="images/L4_f8.png" alt="v and v_s" width="300" height="600">
# 
# Actually, the flow is limited to the pores (white spaces in Figure) only so that the
# _average interstitial velocity_ or _actual velocity_ or _seepage velocity_ $(v_s)$ through pore space
# can be determined by applying continuity equation
# 
# $$
# Q = A_s\cdot v_s = Av
# $$ 
# Leading to 
# 
# $$
# v_s = v\frac{A}{A_s} = \frac{v}{\nu_e}
# $$
# 
# where $A$ = total area of soil specimen, and $A_s$ = area of pores only (see Figure). The velocity
# is divided by effective porosity ($\nu_e$) to account for the fact that only a fraction of the total aquifer
# volume is available for flow. This indicates that for a sand with a porosity of 33% the $v_s
# = 3 v$. Thus the average interstitial velocity or seepage velocity or linear velocity through
# pore space is never smaller than Darcy velocity. Sometimes, the average flow velocity of
# water in the pore space is termed _linear velocity_. 

# **@Anne/@Sophie - pls add a numerical problem here. Pls. check at the botton of the page problems suggested by Prof. Chahar. Pls. note that the problem should be a few line codes.**

# ### Typical values of linear velocities ### 
# 
# Typical values for average interstitial velocities or linear velocities in unconsolidated aquifers are 0.5 m/d to 1 m/d and 30
# m/d to 300 m/d in sand and gravel respectively. 
# 
# Linear velocities in fractured or
# karstified aquifers can be rather high along fractures or conduits e.g. 200 m/d to 1.2
# km/d along fractures and 3 km/d to 14 km/d in karst conduits. 
# 
# On the contrary, the
# linear velocities are very low in the rock matrix of consolidated aquifers (1 cm/d or
# even less).

# ### Travel time and Pore volume ### 
# 
# The average linear/pore velocity is the velocity a conservative tracer/dye experiences if
# carried by water through the aquifer. 
# 
# The travel time of water through a column of
# length $L$ is given by 
# 
# $$
# t = L/v_s
# $$
# 
# It is to be noted that the linear/seepage velocity $v_s$ has to be used in travel time computation, not the Darcy velocity. The term _residence time_ is can also be found to be used for referring to _travel time_ .
# 
# Yet another important term that is often found in standard texts is _pore volume_. The _pore volume is the travel time through a column. It can be understood as the _time_ needed to replace the water in the column. In this sense, the pore volume is not a _volume_ but a _time_ (i.e., 1 PV corresponds to the ratio $L/v_s$ ). The pore volume (PV) is frequently used for _normalisation_ purposes in order to better compare column
# experiments conducted under different flow velocities. This is mostly done for studying the transport behaviour of chemicals dissolved in water and their arrivals at the column outlets

# **@Anne/@Sophie - pls add a numerical problem here. Pls. check at the botton of the page problems suggested by Prof. Chahar. Pls. note that the problem should be a few line codes.**

# ## EXAMPLE PROBLEMS SUGGESTED BY PROF. CHAHAR ##
# 
# _@Anne/Sophie pls. see how these fit to the above texts. The problems in this texts should be a very short one. Complex problems can be part of Tutorials. Pls. check T1-T3 and see if these problems fits better there._
# 
# **Problem 1.** <br>
# If the laboratory hydraulic conductivity of a sample of soil is $3.2\times 10^2$ lpd/m at 20°C, what would be the hydraulic conductivity value at 30°C?
# 
# **Problem 2.** <br>
# 
# In a field test it was observed that a time of 5 hour was required for a tracer to travel from one observation well to another. The wells are 30 m apart and the difference in
# their water table elevations is 50 cm. Samples of the aquifer between the wells indicate that
# the porosity is 15%. Compute (a) the hydraulic conductivity of the aquifer assuming it to be
# homogeneous, (b) the actual velocity of flow as indicated by the tracer, (c) the seepage
# velocity, (d) Reynolds number for the flow assuming an average grain size of 1 mm and $\eta$
# (water) at 27°C = 0.008 stoke.
# 
# **Problem 3.** <br>
# 
# In a homogenous isotropic confined aquifer of constant thickness of 20 m,
# effective porosity of 20% and hydraulic conductivity of 15 m/day, two observations well
# 1200 m apart indicate piezometric heads of 4.4 m and 3.0 m, respectively, above msl.
# Assuming uniform flow, average grain diameter of sand 1 mm and kinematic viscosity of
# water = 0.01 cm$^2$/sec, state (a) Whether Darcy's Law is applicable? (b) What is the average
# flow velocity in pores?
# 
# **Problem 4.** <br>
# 
# A confined aquifer is 18.5 m thick. The potentiometric surface elevations at two
# observation wells 822 m apart 25.96 and 24.62 m. If the horizontal hydraulic conductivity of
# the aquifer is 25 m/day, determine flow rate per unit width of the aquifer, specific discharge,
# and average linear velocity of the flow assuming steady unidirectional flow. Effective
# porosity is 0.25.
# 
# **Problem 5.** <br>
# 
# A 35 cm gravel packed well is pumped at a constant rate of 5000 m$^3$/hr from a
# confined aquifer of thickness 50 m, having $D_{10} = 0.23$ mm and D$_{50} = 0.6$ mm. (i) What is the
# domain around the well for which Darcy’s law is applicable, assuming that the law is valid up
# to $R_e$ = 6? (ii) If the gravel pack is 15 cm thick and has  $D_{10}$ =1.5 mm and  $D_{50}$ = 3 mm,
# estimate the Reynolds’s number and the seepage gradient at mid-pack