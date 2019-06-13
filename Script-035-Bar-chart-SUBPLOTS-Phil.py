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
df = pd.read_csv("Tab-GeomorphPhil.csv")
sunda = df.plate_sunda
phil = df.plate_phil
sa = df.tan_angle
sth = df.sedim_thick
#
fig = plt.figure(figsize=(10.0, 8.0), dpi=300)
fig.suptitle('Bar charts for the bathymetry of the Philippine Trench',
            fontsize=10, fontweight='bold', x=0.5, y=0.99)
#
# Generate a loop for 25 profiles
names = range(1, 26)
#
# subplot 1
ax = fig.add_subplot(221)
sunda.plot(kind ='bar', color=sns.color_palette('rainbow'))
plt.title('Sample points across Sunda Plate')
plt.xlabel('Cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), (names), rotation=45, fontsize=8)
plt.ylabel('Number of observation ponts', fontsize=10, fontfamily='sans-serif')
plt.annotate('A', xy=(0.05, 0.90), xycoords="axes fraction", fontsize=12,
          bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 2
ax = fig.add_subplot(222)
phil.plot(kind ='bar', color=sns.color_palette('plasma'))
plt.title('Sample points across Philippine Plate')
plt.xlabel('Cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), (names), rotation=45, fontsize=8)
plt.ylabel('Number of observation ponts', fontsize=10, fontfamily='sans-serif')
plt.annotate('B', xy=(0.05, 0.90), xycoords="axes fraction", fontsize=12,
          bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 3
ax = fig.add_subplot(223)
sa.plot(kind ='bar', color=sns.color_palette('gist_heat'))
plt.title('Slope steepness (tangent angles °)')
plt.xlabel('Cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), (names), rotation=45, fontsize=8)
plt.ylabel('Slope angles, tangent °', fontsize=10, fontfamily='sans-serif')
plt.annotate('C', xy=(0.05, 0.90), xycoords="axes fraction", fontsize=12,
          bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 4
ax = fig.add_subplot(224)
sth.plot(kind ='bar', color=sns.color_palette('cool'))
plt.title('Sediment thickness')
plt.xlabel('Cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), (names), rotation=45, fontsize=8)
plt.ylabel('Sediment thickness, m', fontsize=10, fontfamily='sans-serif')
plt.annotate('D', xy=(0.90, 0.90), xycoords="axes fraction", fontsize=12,
          bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
plt.tight_layout()
fig.savefig('plot_4barcharts_phil.png', dpi=300)
plt.show()
