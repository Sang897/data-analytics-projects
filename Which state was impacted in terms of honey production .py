#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Based on the kaggle information, we are givne that 12 years ago, there was a rapid decline in honeybee population due to 
#Colony Collapse Disorder. For this reason, many industries are stil recovering. As a data analyst, the goal is to find out which
#state is struggling the most using facet grid. 


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns #Uses matplotlib but works as an upgrade of matplotlib. 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns #Uses matplotlib but works as an upgrade of matplotlib. 
get_ipython().run_line_magic('matplotlib', 'inline')
os.chdir('C:\\Users\\spark\\Desktop\\Data Science Projects\\Honey Production in  USA') #This is changing the working directory
Honeyproduction = pd.read_csv('honeyproduction.csv')


# In[5]:


Honeyproduction


# In[6]:


sns.set_style("dark", {"axes.facecolor":"black"})
sns.relplot(x="year", y="stocks", data=Honeyproduction)
#This general data seemingly show that the stocks are generally decreasing. But is this happening all over the states? 
#To find out, we need to use facet function. 


# In[7]:


#we want to first see the general trend. 
#Then, 
#By just looking at the scatter plot of a whole, we don't know which state was causing the influence. 
#So we use FacetFGrid to find out regional factors like states that could be driviing he change.  
#Working on this: Honeyproduction = sns.load_dataset("Honeyproduction")


# In[8]:


sns.set_style("ticks", {"axes.facecolor":"black"})
g= sns.FacetGrid(Honeyproduction, col = 'state')
g.map_dataframe(sns.scatterplot, x= 'year', y='stocks')
g.set_axis_labels('year','stocks')
#states are selected since the diesase or disorder of bees can be impacted by state distance. 


# In[9]:


#From the data, we see that states CA, MI, SD, WI have been struggling the most since these are the particular states with a decreasing stock price.


# In[ ]:




