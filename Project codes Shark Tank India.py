#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


# Loaded the Shark Tank dataset
file_path = "C:/Users/nikhi/OneDrive/Desktop/Shark Tank India.csv"
df = pd.read_csv(file_path)


# In[9]:


# Display basic information and first few rows
df.info(), df.head()


# In[10]:


#to get a quick statistical summary
df.describe()


# In[11]:


# to replace all missing (NaN) values in the DataFrame with 0
df.fillna(0, inplace=True)


# In[12]:


# to view Headings
df.head(10)


# In[13]:


#To remove Duplicates
df.duplicated()


# In[14]:


print(df['Season End'].unique())


# In[15]:


# Convert to datetime
df['Season Start'] = pd.to_datetime(df['Season Start'], errors='coerce')
df['Season End'] = pd.to_datetime(df['Season End'], errors='coerce')
df['Original Air Date'] = pd.to_datetime(df['Original Air Date'], errors='coerce')

# Convert to string in desired format
df['Season Start'] = df['Season Start'].dt.strftime('%d-%m-%Y')
df['Season End'] = df['Season End'].dt.strftime('%d-%m-%Y')
df['Original Air Date'] = df['Original Air Date'].dt.strftime('%d-%m-%Y')


# In[16]:


df.head(10)


# In[18]:


df.groupby('Industry')['Total Deal Amount'
].sum().reset_index()


# In[17]:


# Organizing data by domain and funding amount
df_domain = df[['Industry', 'Total Deal Amount']].dropna()
df_domain['Total Deal Amount'] = pd.to_numeric(df_domain['Total Deal Amount'], errors='coerce')
industry_funding = df_domain.groupby('Industry')['Total Deal Amount'].sum().reset_index()
industry_funding = industry_funding.sort_values(by='Total Deal Amount', ascending=False)

print(industry_funding)


# In[44]:


#To sort the values
df_domain.sort_values(by='Total Deal Amount', ascending=False)


# In[25]:


df['Pitchers Average Age'] = pd.to_numeric(df['Pitchers Average Age'], errors='coerce')
df['Pitchers Average Age'].fillna(df['Pitchers Average Age'].median(), inplace=True)

# Continue Analysis
founder_profiles = df.groupby('Industry').agg({
    'Number of Presenters': ['mean', 'max'],
    'Pitchers Average Age': ['mean']
}).reset_index()

print(founder_profiles)


# In[27]:


# **Funding Stage Success Analysis**
funding_success = df_filtered.groupby('Bootstrapped').agg({
    'Original Ask Amount': ['mean', 'sum'],
    'Total Deal Amount': ['mean', 'sum']
}).reset_index()


# In[30]:


print(founder_profiles.columns)
print(funding_success.columns)


# In[32]:


print(founder_profiles.shape)  # Check number of columns
print(funding_success.shape)


# In[34]:


founder_profiles.columns = ['Industry', 'Avg Presenters', 'Max Presenters', 'Avg Age']


# In[37]:


funding_success.columns = ['Bootstrapped', 'Avg Ask Amount', 'Total Ask Amount', 'Avg Deal Amount', 'Total Deal Amount']


# In[39]:


print(founder_profiles.columns)
print(funding_success.columns)


# In[41]:


# Display results
print("\nFounder Profiles by Industry:")
print(founder_profiles)

print("\nFunding Stage Success:")
print(funding_success)


# In[43]:


# Export to CSV
output_path = "C:/Users/nikhi/Downloads/Shark Tank US.csv"
df.to_csv(output_path, index=False)

output_path

