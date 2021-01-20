#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# x from 0 to 30
x = 30 * np.random.random((20, 1))

# y = a*x + b with noise
y = 0.2 * x + 3.0 + np.random.normal(size=x.shape)

# create a linear regression model
model = LinearRegression()
model.fit(x, y)

# predict y from the data
x_new = np.linspace(0, 30, 100)
y_new = model.predict(x_new[:, np.newaxis])

# plot the results
plt.figure(figsize=(6, 4))
ax = plt.axes()
ax.scatter(x, y, c="red", label = "data")
ax.plot(x_new, y_new, label = "prediction")

ax.set_ylabel(r'Discharge (m$^3$/s)')
ax.set_xlabel('Hydraulic Head (m)')

ax.axis('tight')
plt.legend();

plt.savefig("M11_fXXYY.png")


# In[ ]:




