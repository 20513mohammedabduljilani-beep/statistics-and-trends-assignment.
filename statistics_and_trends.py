#!/usr/bin/env python
# coding: utf-8

# In[76]:


"""
Title: Global Unemployment Trends (2014–2024)
Author: Mohammed Abdul Jilani
Student ID Number: 24168848
Module: Applied Data Science 1 – Statistics and Trends
Dataset: Kaggle – Global Unemployment Data
"""


# In[76]:


"""
Title: Global Unemployment Trends (2014–2024)
Author: Mohammed Abdul Jilani
Student ID Number: 24168848
Module: Applied Data Science 1 – Statistics and Trends
Dataset: Kaggle – Global Unemployment Data
"""


# In[109]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from scipy.stats import skew, kurtosis


# In[110]:


df = pd.read_csv("global_unemployment_data.csv")
df.head()


# In[111]:


print(df.columns)


# In[112]:


years = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']


# In[113]:


usa = df[df['country_name']=='United States']
india = df[df['country_name']=='India']
china = df[df['country_name']=='China']
brazil = df[df['country_name']=='Brazil']


# In[114]:


def plot_yearly_unemployment(df_unemp):
    """
    Plots unemployment trends for 4 countries (2014–2024)
    """
    plt.figure(dpi=144)
    for country in ['United States', 'India', 'China', 'Brazil']:
        data = df_unemp[df_unemp['country_name'] == country]
        plt.plot(years, data[years].values[0], label=country)
    plt.xlabel('Year')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend()
    plt.title('Global Unemployment Trends (2014–2024)')
    plt.show()

plot_yearly_unemployment(df)


# In[115]:


def plot_subplotted_unemployment(df):
    """
    Plots 4 histograms (US, India, China, Brazil) as subplots
    """
    fig, axs = plt.subplots(2, 2, dpi=144)
    axs = axs.flatten()

    usa = df[df['country_name']=='United States'][years].values[0]
    india = df[df['country_name']=='India'][years].values[0]
    china = df[df['country_name']=='China'][years].values[0]
    brazil = df[df['country_name']=='Brazil'][years].values[0]

    axs[0].hist(usa)
    axs[1].hist(india)
    axs[2].hist(china)
    axs[3].hist(brazil)

    for i, ax in enumerate(axs):
        ax.set_ylabel('N')
        ax.set_title(['United States','India','China','Brazil'][i])

    fig.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()

plot_subplotted_unemployment(df)


# In[116]:


def plot_overplotted_unemployment(*dfs, labels=('United States', 'India', 'China', 'Brazil')):
    """
    Plots 4 unemployment histograms on top of each other (2014–2024)
    """
    plt.figure(dpi=144)
    for i, df in enumerate(dfs):
        plt.hist(df[years].values[0], label=labels[i], bins=10, range=(0, 20), alpha=0.75)
    plt.ylabel('N')
    plt.xlabel('Unemployment Rate (%)')
    plt.title('Overplotted Unemployment Distributions (2014–2024)')
    plt.legend()
    plt.show()

plot_overplotted_unemployment(usa, india, china, brazil)


# In[117]:


def unemployment_boxplot(df):
    """
    Creates a box plot of unemployment rates for selected countries.
    Parameters:
        dataframe : pandas DataFrame containing unemployment data
    """
    plt.figure(dpi=144)

    data_to_plot = []

    for country in countries:
        subset = df[df['country_name'] == country]
        values = subset[years].values.flatten()
        data_to_plot.append(values)

    plt.boxplot(data_to_plot, labels=countries)
    plt.xlabel("Country")
    plt.ylabel("Unemployment Rate (%)")
    plt.title("Box Plot of Unemployment Rates (2014–2024)")
    plt.show()


# In[118]:


unemployment_boxplot(df)


# In[121]:


# Calculate and print the 4 main statistical moments
for i, country in enumerate(countries):
    values = data_to_plot[i]
    mean_val = values.mean()
    var_val = values.var()
    skew_val = skew(values)
    kurt_val = kurtosis(values)
    
    print(country)
    print(" Mean:", round(mean_val, 2))
    print(" Variance:", round(var_val, 2))
    print(" Skewness:", round(skew_val, 2))
    print(" Kurtosis:", round(kurt_val, 2))
    print()


# In[ ]:




