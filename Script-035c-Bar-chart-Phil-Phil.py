#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import os
sns.set_style('whitegrid')

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-GeomorphPhil.csv")
#myplot = df['plate_sunda']
phil = df.plate_phil

phil.plot(kind ='bar', color=sns.color_palette('plasma'))
plt.title('Distribution of observation sample points \nacross the Philippine Plate, Philippine Trench area')
plt.xlabel('Bathymetric cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), ("profile1", "profile2", "profile3", "profile4", "profile5",
            "profile6", "profile7","profile8", "profile9", "profile10",
            "profile11", "profile12", "profile13", "profile14", "profile15",
            "profile16", "profile17", "profile18", "profile19", "profile20",
            "profile21", "profile22", "profile23", "profile24", "profile25"), rotation=45, fontsize=8)
plt.ylabel('Number of observation ponts', fontsize=10, fontfamily='sans-serif')
plt.annotate('B', xy=(0.01, 1.05), xycoords="axes fraction", fontsize=18,
          bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

plt.show()


# In[ ]:




