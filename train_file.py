#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import sqlite3 


# In[4]:


df = pd.read_csv('book.csv',sep = ';')


# In[5]:


df


# In[6]:


df['dates'] = pd.to_datetime(df['dates'],format = '%d.%m.%Y %H:%M')


# In[7]:


df.info()


# In[8]:


pf=df.groupby('dates').count().reset_index()


# In[9]:


pf.sort_values(by = 'dates',ascending=False)


# In[10]:


df.isna().mean()


# In[11]:


df.columns


# In[12]:


df.columns = ['num', 'dates']


# In[13]:


df['num'] = df['num'].str.replace(' ','')


# In[14]:


df['num'] = df['num'].astype("int64")


# In[15]:


df.groupby('num')[['dates']].agg({'dates':'count'}).reset_index().sort_values(by='dates',ascending=False)


# In[17]:


con = sqlite3.connect('db')


# In[18]:


df.to_sql('data',con,index=False,if_exists='replace')


# In[28]:


sql = '''select * from data t 
where num = 998997000000
limit 1'''


# In[29]:


pd.read_sql(sql,con)


# In[32]:


def select(sql):
    return pd.read_sql(sql,con)


# In[33]:


select(sql)


# In[34]:


sql = '''select * from data'''


# In[36]:


select(sql)


# In[39]:


df['dates'].describe()


# In[ ]:




