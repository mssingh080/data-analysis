#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


athlete_data = pd.read_csv('Athletes.csv')
coach_data = pd.read_csv('Coaches.csv')
gender_data = pd.read_csv('EntriesGender.csv')
medal_data = pd.read_csv('Medals.csv')
team_data = pd.read_csv('Teams.csv')


# In[3]:


athlete_data.head()


# In[4]:


gender_data.head()


# In[5]:


medal_data.head()


# In[6]:


team_data.head()


# In[7]:


athlete_data.isnull().sum()


# In[8]:


gender_data.isnull().sum()


# In[9]:


medal_data.isnull().sum()


# In[10]:


coach_data.isnull().sum()


#  # Which countries do most athlete's come from?
# 

# In[11]:


athlete_data.head()


# In[12]:


athlete_data['NOC'].value_counts()


# In[13]:


y = athlete_data.NOC.value_counts().values[:30]
x = athlete_data.NOC.value_counts().index[:30]
plt.figure(figsize=(20,4))
plt.bar(x,y)
plt.xlabel("Country")
plt.ylabel("Number of athelets")
plt.xticks(rotation="vertical",size=12)
plt.yticks(size=16)
plt.show()
                                          


# # Which Discipline is most popular and which country has the highest participants in it?

# In[14]:


athlete_data.head()


# In[15]:


athlete_data["Discipline"].value_counts()[:15]


# In[19]:


y = athlete_data.Discipline.value_counts().values
x = athlete_data.Discipline.value_counts().index
plt.figure(figsize=(20,4))
for index,value in enumerate(y):
    plt.text(index,value,str(value),color = "blue",size = 12)
    
plt.bar(x,y)
plt.xlabel("Discipline")
plt.ylabel("Number of athelets")
plt.xticks(rotation="vertical",size=12)
plt.yticks(size=16)
plt.show()
                                          


# In[22]:


athlete_datas = team_data[(team_data["Discipline"]=="Athletics")]
athlete_datas["NOC"].value_counts()


# # Which country produces highest number of coaches?

# In[29]:


coach_data.isnull().sum()


# In[30]:


coach_data.NOC.value_counts()


# # Gender across disciplines.

# In[32]:


gender_data.head()


# In[33]:


gender_data.isnull().sum()


# In[45]:


Disc = gender_data.groupby("Discipline")
x = [Discipline for Discipline,df in Disc]
female = gender_data.Female
male = gender_data.Male
plt.figure(figsize=(20,8))
x_axis = np.arange(len(x))
plt.bar(x_axis-0.2,female,0.4,label = "female")
plt.bar(x_axis+0.2,male,0.4,label = "male")
plt.ylabel("Number of Participants")
plt.xticks(x_axis,x,rotation="vertical")
plt.legend()
plt.show


# # Which country received most gold medal ?	Which received most silver and most bronze and which received least for each?

# In[46]:


medal_data.info()


# In[62]:


x = []
for team in medal_data["Team/NOC"]:
     x.append(team)
y = medal_data.Gold
plt.figure(figsize=(20,10))
plt.bar(x,y)
for index,value in enumerate(y):
    plt.text(index,value,str(value),color="Red",size=10)
plt.xlabel("Country")
plt.ylabel("Gold Medals")
plt.xticks(x,rotation = "vertical")
plt.title("Gold Medals across Nations")
plt.show()


# In[63]:


x = []
for team in medal_data["Team/NOC"]:
     x.append(team)
y = medal_data.Silver
plt.figure(figsize=(20,10))
plt.bar(x,y)
for index,value in enumerate(y):
    plt.text(index,value,str(value),color="Red",size=10)
plt.xlabel("Country")
plt.ylabel("Silver Medals")
plt.xticks(x,rotation = "vertical")
plt.title("Silver Medals across Nations")
plt.show()


# In[61]:


x = []
for team in medal_data["Team/NOC"]:
     x.append(team)
y = medal_data.Bronze         
plt.figure(figsize=(20,10))
plt.bar(x,y)
for index,value in enumerate(y):
    plt.text(index,value,str(value),color="Red",size=10)
plt.xlabel("Country")
plt.ylabel("Bronze Medals")
plt.xticks(x,rotation = "vertical")
plt.title("Bronze Medals across Nations")
plt.show()


# In[64]:


x = []
for team in medal_data["Team/NOC"]:
     x.append(team)
y = medal_data.Total         
plt.figure(figsize=(20,10))
plt.bar(x,y)
for index,value in enumerate(y):
    plt.text(index,value,str(value),color="Red",size=10)
plt.xlabel("Country")
plt.ylabel("Total Medals")
plt.xticks(x,rotation = "vertical")
plt.title("Total Medals across Nations")
plt.show()


# In[ ]:




