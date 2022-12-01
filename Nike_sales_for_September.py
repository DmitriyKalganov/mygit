#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd 
import sqlite3


# In[38]:


df = pd.read_csv('nike_data_2022_09.csv')


# In[39]:


df.head()


# In[40]:


con = sqlite3.connect('db')


# In[41]:


df.to_sql('nike_data',con,index=False,if_exists='replace')


# In[42]:


sql = '''select * from nike_data'''


# In[43]:


def select(sql):
    return pd.read_sql(sql,con)


# In[44]:


select(sql)


# In[45]:


df.info()


# In[46]:


df['scraped_at'] = pd.to_datetime(df['scraped_at'],format="%d/%m/%Y %H:%M:%S")


# In[47]:


len(df)


# In[48]:


df[df['availability'].isna()]


# In[49]:


sql = '''select sub_title,price,count(sub_title) as cnt from nike_data
group by sub_title,price
order by cnt DESC
'''


# In[50]:


select(sql)


# In[51]:


df['month'] = df['scraped_at'].dt.month


# In[52]:


df.sample(10)


# In[18]:


df['scraped_at'].value_counts()


# In[23]:


df['scraped_at'] = pd.to_datetime(df['scraped_at']).dt.date

