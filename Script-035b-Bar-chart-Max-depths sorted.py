#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import os
sns.set_style('whitegrid')

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
#df
myplot = df['Min']

myplot
myplot.sort_values().plot(kind ='bar', color=sns.color_palette('tab20c'))

plt.title('Bar plot for the bathymetry of the Mariana Trench \nDistribution of depths by 25 profiles (sorted)')
plt.xlabel('Bathymetric profiles, nr. 1-25, sorted', fontsize=10, fontfamily='sans-serif')
plt.ylabel('Depths, m', fontsize=10, fontfamily='sans-serif')

plt.annotate('B', xy=(0.93, .1), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
plt.show()





