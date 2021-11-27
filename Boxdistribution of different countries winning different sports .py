#!/usr/bin/env python
# coding: utf-8

# In[2]:


#The objective of this project is to see the boxplot distribution for the different countries winning the medal. 
#The following data is from the website https://www.kaggle.com/arjunprasadsarkhel/2021-olympics-in-tokyo


# In[97]:


import pandas as pd
import os
print(os.getcwd())


# In[98]:


import matplotlib.pyplot as plt
import seaborn as sns #Uses matplotlib but works as an upgrade of matplotlib. 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[99]:


os.chdir('C:\\Users\\spark\\Desktop\\Data Science Projects\\Olympics in Tokyo 2021') #This is changing the working directory
Athletes = pd.read_csv('Athletes.csv')


# In[100]:


Athletes.drop(columns= ["Name"],axis=1,inplace=False) # "Name" Column from the data frame is not necessary so dropped it.


# In[101]:


Athletes.head()


# In[102]:


sns.catplot(x='NOC',
             kind="count", 
             height=15, 
             aspect=5, 
             data=Athletes)

#In this case, since there are so many bars, I only want to see few bars from here. 


# In[103]:


sns.catplot(x='Discipline',
             kind="count", 
             height=15, 
             aspect=5, 
             data=Athletes)


# In[155]:


#Looking at the graph above, we realize that Athletics is not part of the types of sports. 

#to start, for the Discipline, we want to make sure to drop the following. 
#Cycling Road, Artistic Gymnatstics, Rowing, Basketball, 

indexNames = Athletes[Athletes['Discipline'] == 'Sport Climbing'].index
indexNames2 = Athletes[Athletes['Discipline'] == 'Cycling BMX Freestyle'].index
indexNames3 = Athletes[Athletes['Discipline'] == '3x3 Basketball'].index
indexNames4 = Athletes[Athletes['Discipline'] == 'Cycling Mountain Bike'].index
indexNames5 = Athletes[Athletes['Discipline'] == 'Modern Pentathlon'].index
indexNames6 = Athletes[Athletes['Discipline'] == 'Skateboarding'].index
indexNames7 = Athletes[Athletes['Discipline'] == 'Golf'].index
indexNames8 = Athletes[Athletes['Discipline'] == 'Cycling Track'].index
indexNames9 = Athletes[Athletes['Discipline'] == 'Tennis'].index
indexNames10 = Athletes[Athletes['Discipline'] == 'Equestrian'].index
indexNames11 = Athletes[Athletes['Discipline'] == 'Volleyball'].index
indexNames12 = Athletes[Athletes['Discipline'] == 'Rugby Sevens'].index
indexNames13 = Athletes[Athletes['Discipline'] == 'Equ'].index
indexNames14 = Athletes[Athletes['Discipline'] == 'PromoRepublic'].index
indexNames15 = Athletes[Athletes['Discipline'] == 'Buffer'].index
indexNames16 = Athletes[Athletes['Discipline'] == 'Twitter for Ipad'].index
indexNames17 = Athletes[Athletes['Discipline'] == 'Taekwondo'].index
indexNames18 = Athletes[Athletes['Discipline'] == 'Artistic Swimming'].index 
indexNames19 = Athletes[Athletes['Discipline'] == 'Cycling Road'].index 
indexNames20 = Athletes[Athletes['Discipline'] == 'Artistic Gymnastics'].index 
indexNames21 = Athletes[Athletes['Discipline'] == 'Karate'].index
indexNames22 = Athletes[Athletes['Discipline'] == 'Swimming'].index
indexNames23 = Athletes[Athletes['Discipline'] == 'Handball'].index
indexNames24 = Athletes[Athletes['Discipline'] == 'Rowing'].index
indexNames25 = Athletes[Athletes['Discipline'] == 'Basketball'].index
indexNames26 = Athletes[Athletes['Discipline'] == 'Wrestling'].index
indexNames27 = Athletes[Athletes['Discipline'] == 'Rhythmic Gymnastics'].index
indexNames28 = Athletes[Athletes['Discipline'] == 'Baseball/Softball'].index
indexNames29 = Athletes[Athletes['Discipline'] == 'Judo'].index
indexNames30 = Athletes[Athletes['Discipline'] == 'Shooting'].index
indexNames31 = Athletes[Athletes['Discipline'] == 'Judo'].index
indexNames32 = Athletes[Athletes['Discipline'] == 'Table Tennis'].index
indexNames33 = Athletes[Athletes['Discipline'] == 'Fencing'].index
indexNames34 = Athletes[Athletes['Discipline'] == 'Badminton'].index
indexNames35 = Athletes[Athletes['Discipline'] == 'Trampoline Gymnastics'].index
indexNames36 = Athletes[Athletes['Discipline'] == 'Marathon Swimming'].index
indexNames37 = Athletes[Athletes['Discipline'] == 'Triathlon'].index
indexNames38 = Athletes[Athletes['Discipline'] == 'Canoe Slalom'].index
indexNames39 = Athletes[Athletes['Discipline'] == 'Surfing'].index
indexNames40 = Athletes[Athletes['Discipline'] == 'Cycling BMX Racing'].index
indexNames41 = Athletes[Athletes['Discipline'] == 'Beach Volleyball'].index
indexNames42 = Athletes[Athletes['Discipline'] == 'Cycling BMX Racing'].index
indexNames43 = Athletes[Athletes['Discipline'] == 'Cycling Mountain Bike'].index
indexNames44 = Athletes[Athletes['Discipline'] == 'Archery'].index
indexNames45 = Athletes[Athletes['Discipline'] == 'Athletics'].index


# In[156]:


Athletes.drop(indexNames, inplace=True)
Athletes.drop(indexNames2, inplace=True)
Athletes.drop(indexNames3, inplace=True)
Athletes.drop(indexNames5, inplace=True)
Athletes.drop(indexNames6, inplace=True)
Athletes.drop(indexNames7, inplace=True)
Athletes.drop(indexNames8, inplace=True)
Athletes.drop(indexNames9, inplace=True)
Athletes.drop(indexNames10, inplace=True)
Athletes.drop(indexNames11, inplace=True)
Athletes.drop(indexNames12, inplace=True)
Athletes.drop(indexNames13, inplace=True)
Athletes.drop(indexNames14, inplace=True)
Athletes.drop(indexNames15, inplace=True)
Athletes.drop(indexNames16, inplace=True)
Athletes.drop(indexNames17, inplace=True)
Athletes.drop(indexNames18, inplace=True)
Athletes.drop(indexNames19, inplace=True)
Athletes.drop(indexNames20, inplace=True)
Athletes.drop(indexNames21, inplace=True)
Athletes.drop(indexNames22, inplace=True)
Athletes.drop(indexNames23, inplace=True)
Athletes.drop(indexNames24, inplace=True)
Athletes.drop(indexNames25, inplace=True)
Athletes.drop(indexNames26, inplace=True)
Athletes.drop(indexNames27, inplace=True)
Athletes.drop(indexNames28, inplace=True)
Athletes.drop(indexNames29, inplace=True)
Athletes.drop(indexNames30, inplace=True)
Athletes.drop(indexNames31, inplace=True)
Athletes.drop(indexNames32, inplace=True)
Athletes.drop(indexNames33, inplace=True)
Athletes.drop(indexNames34, inplace=True)
Athletes.drop(indexNames35, inplace=True)
Athletes.drop(indexNames36, inplace=True)
Athletes.drop(indexNames37, inplace=True)
Athletes.drop(indexNames38, inplace=True)
Athletes.drop(indexNames39, inplace=True)
Athletes.drop(indexNames40, inplace=True)
Athletes.drop(indexNames41, inplace=True)
Athletes.drop(indexNames42, inplace=True)
Athletes.drop(indexNames43, inplace=True)
Athletes.drop(indexNames44, inplace=True)
Athletes.drop(indexNames45, inplace=True)


# In[169]:


sns.catplot( x='Discipline',
             kind="count", 
             height=15, 
             aspect=5, 
             data=Athletes)
plt.xlabel("Discipline", size=20,color='white')
plt.ylabel("Count", size=20)
plt.title("Toyko Olympics Medal numbers",size = 40)
plt.tight_layout()
plt.savefig("TokoOlympicsMedalnumber.png")


# In[168]:



#The result indicates that from the 11,000 atheltes with 47 disciplines, participants received the most medals in disciplines of
#Football, Boxing, Weightlifting, Diving, Sailing, Hockey, Water Polo, Canoe Sprint. 
#The common feature of these disciplines is that these require group works. For example, soccer can always be done with a team of 11. 

