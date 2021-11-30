#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Showing Gender distribution, I would like to see a chart (barplot) with different colors that indicate the distribution 
#of male and women. 


# In[10]:


import pandas as pd
import os
print(os.getcwd())


# In[45]:


import matplotlib.pyplot as plt
import seaborn as sns #Uses matplotlib but works as an upgrade of matplotlib. 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[137]:


os.chdir('C:\\Users\\spark\\Desktop\\Data Science Projects\\Sports Analysis') #This is changing the working directory
Athletes = pd.read_csv('EntriesGender.csv')
Athletes.head()
a=Athletes.Discipline
b=Athletes.Female
c=Athletes.Male


# In[138]:


a=a.iloc[0:3]
b=b.iloc[0:3]
c=c.iloc[0:3]
#https://www.shanelynn.ie/pandas-iloc-loc-select-rows-and-columns-dataframe/


# In[139]:


import numpy as np


# In[140]:


s=np.transpose(b)


# In[141]:


len(a)


# In[142]:


N= 3
ind = np.arange(N) 
width = .35


# In[146]:


plt.bar(ind, b, width, label='Female')
plt.bar(ind+width, c, width, label='Male')
plt.xticks(ind + width / 2, a)
plt.legend(loc='best')
plt.title("Medals during Toyko Olympics based on Genders")
plt.xlabel("Male or Female")
plt.ylabel("Number of medals won")
#https://benalexkeen.com/bar-charts-in-matplotlib/


# In[ ]:


#It appears that there are no gender differences in terms of winning medals during Tokyo Olympics

