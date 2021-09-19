#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


os.chdir("C:/Users/14236/Documents") 


# In[3]:


data = pd.read_csv("Realestate.csv") # read data


# In[4]:


data.head()


# In[5]:


data.dtypes # check data types


# In[6]:


houseAge = data.houseAge # create a column to be standardized 


# In[7]:


norm = (houseAge - houseAge - houseAge.mean())/houseAge.std() # standardize the data


# In[8]:


norm.head()


# In[9]:


minmax = (houseAge - houseAge.min())/(houseAge.max() - houseAge.min()) # make it so max = 1 min = 0


# In[10]:


minmax.min()


# In[11]:


data['houseAgeStandardized'] = minmax #create a new column 


# In[12]:


data.head()


# In[13]:


data.drop('numberOfConvenienceStores', axis = 1) # drop column 


# In[14]:


data.head() 


# In[15]:


data.drop('numberOfConvenienceStores', axis = 1, inplace = True) 


# In[16]:


data.rename(columns={"transaction":"transactionDate"},inplace = True)# rename column


# In[17]:


data.loc[0:10,:] # display all rows 0:10, inclusive for loc. selects by index. 


# In[18]:


data.iloc[0:10,:] # exclusive for iloc checks by row number


# In[19]:


os.chdir("C:/Users/14236/Documents/GitHub/Data-Science/myJupyterNotebooks")


# In[ ]:




