#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


# In[18]:


df =pd.ExcelFile('neev_info.xlsx')


# In[19]:


df.sheet_names


# In[20]:


read_sheet =pd.read_excel(df, 'Sheet2')


# In[21]:


read_sheet.head()
read_sheet.shape


# In[22]:


csv_data = read_sheet.to_csv('neev_info2.csv', sep='\t', encoding='utf-8', index=False)


# In[23]:


csv_data


# In[ ]:




