#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


# In[2]:


df = pd.read_csv("dataset.csv")
df.head(5)


# In[3]:



fig = plt.figure(figsize=(10,6)) 
ax  = plt.subplot()

ax.plot(df["A"], df["B"], "-", label="effective porosity")  
ax.plot(df["C"], df["D"], "--", label="(Well sorted)")  
ax.plot(df["E"], df["F"],"-.", label="Total porosity")  
ax.plot(df["G"], df["H"],"+-", label="(well sorted)")  
ax.plot(df["I"], df["J"],'*-', label="specific retention")  

plt.legend() 

ax.set_xscale("log")
ax.set_xlim(0.0001, 200)
ax.set_ylim(0,65)

fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
yticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(yticks)

#x_fmt = mtick.FormatStrFormatter('%e')
#ax.xaxis.set_major_formatter(x_fmt)


ax.set_ylabel("Porosity")
ax.set_xlabel("Particle size (mm) ")

ax2 = ax.twiny() # add second x-axis
ax2.xaxis.set_ticks_position("bottom")
ax2.xaxis.set_label_position("bottom")
ax2.spines["bottom"].set_position(("axes", -0.15))
ax2.set_frame_on(True)
#ax2.patch.set_visible(False)

ax2.set_frame_on(True)
ax2.tick_params(direction='out', length= 15, width=2, colors='r',
               grid_color='r', grid_alpha=0.5, axis='x', rotation=90, which="minor")

ax2.set_xscale("log")
vals = [0.0001, 0.002, 0.06, 2.0, 63, 1000] 
ax2.set_xticks(vals, minor=True)    
ax2.set_xticklabels(vals, minor=True) ;
ax2.set_xlim(0.0001, 200)  


plt.setp(ax2.get_xmajorticklabels(), visible=False); # remove the major xaxis label

fig.text(0.15,-0.02 , 'Clay', ha='left', va='top', size=12, fontweight='bold')
fig.text(0.35,-0.02 , 'Silt', ha='left', va='top', size=12, fontweight='bold')
fig.text(0.52,-0.02 , 'Sand', ha='left', va='top', size=12, fontweight='bold')
fig.text(0.7,-0.02 , 'Gravel', ha='left', va='top', size=12, fontweight='bold')


# In[4]:


ax2.sexlabel[0].set_visible(False)


# In[ ]:




