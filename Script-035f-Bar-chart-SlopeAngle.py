#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import os
sns.set_style('whitegrid')

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-GeomorphPhil.csv")
#myplot = df['plate_sunda']
sa = df['tan_angle']

sa.plot(kind ='bar', color=sns.color_palette('gist_heat'))
plt.title('Philippine Trench: slope steepness \nalong the 25 profiles (tangent angles °)')
plt.xlabel('Bathymetric cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), ("profile1", "profile2", "profile3", "profile4", "profile5",
            "profile6", "profile7","profile8", "profile9", "profile10",
            "profile11", "profile12", "profile13", "profile14", "profile15",
            "profile16", "profile17", "profile18", "profile19", "profile20",
            "profile21", "profile22", "profile23", "profile24", "profile25"), rotation=45, fontsize=8)
plt.ylabel('Slope angles, tangent °', fontsize=10, fontfamily='sans-serif')
plt.annotate('C', xy=(0.01, 1.05), xycoords="axes fraction", fontsize=18,
          bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

plt.show()


# In[ ]:




