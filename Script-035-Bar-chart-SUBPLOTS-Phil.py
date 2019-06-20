#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.artist as martist
from matplotlib.offsetbox import AnchoredText
import seaborn as sns

sns.set_style('whitegrid')
sns.set_context('paper')

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-GeomorphPhil.csv")
sunda = df.plate_sunda
phil = df.plate_phil
sa = df.tan_angle
sth = df.sedim_thick

fig = plt.figure(figsize=(10.0, 8.0), dpi=300)
fig.suptitle('Bar charts for the bathymetry of the Philippine Trench',
             fontsize=10, fontweight='bold', x=0.5, y=0.95)

# define annotations
def add_at(ax, t, loc=2):
    fp = dict(size=11)
    _at = AnchoredText(t, loc=loc, prop=fp)
    ax.add_artist(_at)
    return _at

# Generate a loop for 25 profiles
names = range(1, 26)

# subplot 1
ax = fig.add_subplot(221)
sunda.plot(kind ='bar', color=sns.color_palette('rainbow'))
plt.title('Sample points across Sunda Plate')
plt.xlabel('Cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), (names), rotation=45, fontsize=8)
plt.ylabel('Number of observation ponts', fontsize=10, fontfamily='sans-serif')
add_at(ax, "A", loc=2)

# subplot 2
ax = fig.add_subplot(222)
phil.plot(kind ='bar', color=sns.color_palette('plasma'))
plt.title('Sample points across Philippine Plate')
plt.xlabel('Cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), (names), rotation=45, fontsize=8)
plt.ylabel('Number of observation ponts', fontsize=10, fontfamily='sans-serif')
add_at(ax, "B", loc=2)


# subplot 3
ax = fig.add_subplot(223)
sa.plot(kind ='bar', color=sns.color_palette('gist_heat'))
plt.title('Slope steepness (tangent angles °)')
plt.xlabel('Cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), (names), rotation=45, fontsize=8)
plt.ylabel('Slope angles, tangent °', fontsize=10, fontfamily='sans-serif')
add_at(ax, "C", loc=2)

# subplot 4
ax = fig.add_subplot(224)
sth.plot(kind ='bar', color=sns.color_palette('cool'))
plt.title('Sediment thickness')
plt.xlabel('Cross-section profiles', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(25), (names), rotation=45, fontsize=8)
plt.ylabel('Sediment thickness, m', fontsize=10, fontfamily='sans-serif')
add_at(ax, "D", loc=1)

# visualizing and saving
plt.tight_layout()
plt.subplots_adjust(top=0.90, bottom=0.08,
                    left=0.10, right=0.95,
                    hspace=0.25, wspace=0.35
                    )
plt.savefig('plot_BarCharP.png', dpi=300)
plt.show()
