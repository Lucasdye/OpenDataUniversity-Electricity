#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as panda
import numpy as nump
import geopandas as gpanda
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as mticker


# In[8]:


# Defining array from .csv file
df = panda.read_csv('parc-region-annuel-production-filiere.csv', sep =';')

# Deleting the last two columns [start from last column, and go back 2 columns]
df = df.iloc[:, :-2]

# Replacing 'Nan' by 0 (replace Nan by 0)
df = df.fillna(0)

# Creating a new column 'Total' that sums all the values of the row
df['Total'] = df.iloc[:, 3:].sum(axis=1)

# Asking panda to diplay full dataframes (all rows, all))
panda.set_option('display.max_rows', None)

# Splitting the dataframe into multiple dataframes based on the year
df_2008 = df[df['annee'] == 2008].copy()
df_2009 = df[df['annee'] == 2009].copy()
df_2010 = df[df['annee'] == 2010].copy()
df_2011 = df[df['annee'] == 2011].copy()
df_2012 = df[df['annee'] == 2012].copy()
df_2013 = df[df['annee'] == 2013].copy()
df_2014 = df[df['annee'] == 2014].copy()
df_2015 = df[df['annee'] == 2015].copy()
df_2016 = df[df['annee'] == 2016].copy()
df_2017 = df[df['annee'] == 2017].copy()
df_2018 = df[df['annee'] == 2018].copy()
df_2019 = df[df['annee'] == 2019].copy()
df_2020 = df[df['annee'] == 2020].copy()
df_2021 = df[df['annee'] == 2021].copy()
df_2022 = df[df['annee'] == 2022].copy()
df_2023 = df[df['annee'] == 2023].copy()


# In[9]:


# Load GeoJSON file
map = gpanda.read_file('region_francais.geojson')

# Converting to same data type to allow joining (int64) !
map['code'] = map['code'].astype('int64')

# Merging two dataframes at the'code' and 'code insee region' of def
mergedDfs = map.set_index('code').join(df_2008.set_index('code_insee_region'))

# Create a new figure
fig, ax = plt.subplots(1, figsize=(10, 10))

# Set the aspect of the plot to be equal
ax.set_aspect('equal')

# Plot the GeoDataFrame with color according to 'Total'
mergedDfs.plot(column='Total', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Show the plot
plt.show()

# Show tab of the dataframe
#print(df_2008)


# 
