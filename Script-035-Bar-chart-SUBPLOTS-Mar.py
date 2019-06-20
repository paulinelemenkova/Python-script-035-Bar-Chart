#!/usr/bin/env python
# coding: utf-8
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.artist as martist
from matplotlib.offsetbox import AnchoredText
import seaborn as sns

sns.set_style('whitegrid')
sns.set_context('paper')

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
depths = df['Min']

fig = plt.figure(figsize=(10.0, 4.0), dpi=300)
fig.suptitle('Bar chart for the bathymetry of the Mariana Trench',
             fontsize=10, fontweight='bold', x=0.5, y=0.99)

def add_at(ax, t, loc=2):
    fp = dict(size=11)
    _at = AnchoredText(t, loc=loc, prop=fp)
    ax.add_artist(_at)
    return _at

# subplot 1
ax = fig.add_subplot(121)
ax = depths.plot(kind ='bar', color=sns.color_palette('tab20c'))
plt.title('Distribution of depths by 25 profiles (unsorted)')
plt.xlabel('Profiles, nr. 1-25, unsorted', fontsize=10, fontfamily='sans-serif')
plt.ylabel('Depths, m', fontsize=10, fontfamily='sans-serif')
plt.xticks(rotation=15, size=8)
plt.yticks(rotation=0, size=8)
add_at(ax, "A", loc=4)

# subplot 2
ax = fig.add_subplot(122)
ax = depths.sort_values().plot(kind ='bar', color=sns.color_palette('tab20c'))
plt.title('Distribution of depths by 25 profiles (sorted)')
plt.xlabel('Profiles, nr. 1-25, sorted', fontsize=10, fontfamily='sans-serif')
plt.ylabel('Depths, m', fontsize=10, fontfamily='sans-serif')
plt.xticks(rotation=15, size=8)
plt.yticks(rotation=0, size=8)
add_at(ax, "B", loc=4)

# visualizing and saving
plt.tight_layout()
plt.subplots_adjust(top=0.90, bottom=0.08,
                    left=0.10, right=0.95,
                    hspace=0.25, wspace=0.35
                    )
plt.savefig('plot_BarCharM.png', dpi=300)
plt.show()
