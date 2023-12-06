#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
pd.set_option('display.max_rows', 50000)
pd.set_option('display.max_columns', 50000)
pd.set_option('display.width', 100000)
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# In[9]:


df = pd.read_csv(r"C:\Users\dchit\OneDrive\Documents\LeaguesOnly.csv")
df


# In[10]:


del df['ID']


# In[11]:


df = pd.read_csv(r"C:\Users\dchit\OneDrive\Documents\LeagueTotals.csv")
df


# In[12]:


df.corr()


# In[13]:


Seasons = df.groupby(['LastName', 'Year'])

Seasons.sum().sort_values(by='Points', ascending=False)


# In[14]:


Age = df.groupby('Age')


# In[15]:


Age.describe()


# In[16]:


Age.sum()


# In[19]:


Age.mean().sort_values(by="Points", ascending=False)


# In[18]:


Age.mean().sort_values(by="Goals", ascending=False)


# In[20]:


Age.mean().sort_values(by="PPG", ascending=False)


# In[22]:


Age.mean()['Points'].plot()


# In[23]:


Age.mean()['Goals'].plot()


# In[24]:


Age.mean()['PPG'].plot()


# In[25]:


pd.pivot_table(df.reset_index(),
              index='Year',columns='Age',values='Goals'
              ).plot(subplots=True,sharex=False, figsize=(10,50))


# In[26]:


pd.pivot_table(df.reset_index(),
              index='Year',columns='Age',values='PPG'
              ).plot(subplots=True,sharex=False, figsize=(10,50))


# In[ ]:




