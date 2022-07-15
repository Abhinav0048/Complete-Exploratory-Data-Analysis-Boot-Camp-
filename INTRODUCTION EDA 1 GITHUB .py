#!/usr/bin/env python
# coding: utf-8

# # EXPLORATORY DATA ANALYSIS 

# # What is EDA 
# *EDA is anlaytics process to understand the data in depth and learn different data characterstics with visual means.

# In[2]:


# Some Important libraries which we have to import as module to work::


# In[3]:


import numpy as np 
import pandas as pd
import scipy 
from scipy import stats
import seaborn as sns


# # End To End Process which needs to be followed for Data Analysis
# *Univariate Analaysis
# 
# *Bivariate Analysis
# 
# *Treating the Missing Values in the data 
# 
# *Outliers Analysis and Removal from the data 
# 
# *Feauture Engineering(Extracting new Features from existing one)
# 
# * Data Transformation,Scalling & Encoding(Also known as preprocesing Stage)
# 

# In[ ]:


# Pulling the data from Analyticsvidya.com 
# The data is about Big Mart Sales 
# The want anyalysis on the sale so they make decisons  for their buisness


# In[4]:


sales=pd.read_csv('https://datahack-prod.s3.amazonaws.com/train_file/train_v9rqX0R.csv')


# In[5]:


sales


# # There are few steps that we need to follow before starting the Analysis
# * Check the shape of the data 
# 
# * check the Info the data 
# 
# * check the descriptive Statistics of the value 
# 
# * Decide the Target Variable in your data 
# 
# 

# In[6]:


sales.shape


# In[7]:


sales.info()


# In[8]:


sales.describe()


# In[9]:


sales.head() # Checking the head of the data/preview of the data


# In[10]:


# Checking the Target Variable 
# The Target Variable is sales as we have to predict the sales for future 


# In[11]:


sales.Item_Outlet_Sales


# In[ ]:




