#!/usr/bin/env python
# coding: utf-8
#
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import os
sns.set_style('whitegrid')
#
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
#
depths = df['Min']
#
fig = plt.figure(figsize=(10.0, 4.0), dpi=300)
fig.suptitle('Bar chart for the bathymetry of the Mariana Trench',
            fontsize=10, fontweight='bold', x=0.5, y=0.99)
#
# subplot 1
ax = fig.add_subplot(121)
ax = depths.plot(kind ='bar', color=sns.color_palette('tab20c'))
plt.title('Distribution of depths by 25 profiles (unsorted)')
plt.xlabel('Profiles, nr. 1-25, unsorted', fontsize=10, fontfamily='sans-serif')
plt.ylabel('Depths, m', fontsize=10, fontfamily='sans-serif')
plt.annotate('A', xy=(0.93, .1), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 2
ax = fig.add_subplot(122)
ax = depths.sort_values().plot(kind ='bar', color=sns.color_palette('tab20c'))
plt.title('Distribution of depths by 25 profiles (sorted)')
plt.xlabel('Profiles, nr. 1-25, sorted', fontsize=10, fontfamily='sans-serif')
plt.ylabel('Depths, m', fontsize=10, fontfamily='sans-serif')
plt.annotate('B', xy=(0.93, .1), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
plt.tight_layout()
fig.savefig('plot_barcharts.png', dpi=300)
plt.show()
