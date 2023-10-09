#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


# # This Notebook shows some basic Pandas Commands/Functions and Graph Plotting with Matplotlib and Seaborn in Python
# 
# * Here you can find some practice/examples of how to load, sort, and select columns from a dataset with pandas commands
# * And additionally, one horizontal barplot 

# For this demonstration, I will be using a dataset for male and female individuals consisting of age,
# citizenship, marital status, annual household income, weight, height, and bmi

# In[2]:


# loading the csv file from my computer's file path.
# If seeking to replicate this procedure, please input the file path for a dataset as it is stored in your computer for this step.
nhanes_csv_filepath = 'C:/Users/micha/height_weight_gender.csv'
nhanes_csv_filepath


# ### Loading the nhanes dataset into a dataframe, df1

# In[3]:


df1 = pd.read_csv(nhanes_csv_filepath)
df1


# ### Selecting columns for gender, height, weight, and BMI

# In[4]:


df2 = df1[['gender', 'height', 'weight', 'bmi']]
df2


# ### Getting the height and weight of only male participants

# In[5]:


dfmale = df1[df1['gender'] == 'male']
dfmale_hw = dfmale[['height', 'weight']]
dfmale_hw


# ### Selecting the BMI of only female participants

# In[6]:


dffem = df1[df1['gender'] == 'female']
dffem_bmi = dffem[['bmi']]
dffem_bmi


# ### Selecting people heavier than 100 kg

# In[7]:


df4 = df1[df1['weight'] > 100]
df4


# ### Selecting only people with above average bmi
# 
# * Here, I find the mean for any column (say "column xyz") by using the "df['xyz'].mean()"

# In[8]:


meanbmi = df1['bmi'].mean()
print('Average BMI:', meanbmi)


# In[9]:


df5 = df1[df1['bmi'] > meanbmi]
df5


# ### Selecting male participant taller than average height and heavier than average weight

# In[10]:


meanheight = df1['height'].mean()
meanweight = df1['weight'].mean()
print('Average Height:', meanheight)
print('Average Weight:', meanweight)


# In[11]:


df6 = df1[(df1['gender'] == 'male') & (df1['height'] > meanheight) & (df1['weight'] > meanweight)]
df6


# ### Sorting the dataset by BMI

# In[12]:


df_sorted = df1.sort_values(by = 'bmi', ascending = True) # "ascending = True" sorts from smallest to largest
df_sorted


# ### Sorting the dataset by Gender and BMI (in that order)

# In[13]:


df_sorted2 = df1.sort_values(by = ['gender', 'bmi'], ascending = True)
df_sorted2


# ## Plotting the average male and female height on a horizontal barplot 
# 
# This graph was plotted with the following features:
# * 1. A 4x3 figure size 
# * 2. The xlabel being given the name "Height (cm)"
# * 3. No ylabel 
# * 4. Plotted using 'ggplot' style

# In[14]:


dfavg = df1.groupby('gender')['height'].mean()
dfavg


# In[15]:


plt.style.use('ggplot')
sns.set_style('whitegrid')
plt.figure(figsize = (4,3))
dfavg.plot(kind='barh', color=['red','blue'])
plt.xlabel('Height (cm)')
plt.ylabel('')
plt.title('Average Male and Female Heights')
plt.show()


# ## Using Seaborn & Different Colors (for Fun)

# In[16]:


plt.style.use('ggplot')
sns.set_style('whitegrid')
plt.figure(figsize = (4,3))
sns.barplot(y=dfavg.index, x=dfavg.values, palette=['orchid','turquoise'])
plt.xlabel('Height (cm)')
plt.ylabel('')
plt.title('Average Male and Female Heights')
plt.show()

