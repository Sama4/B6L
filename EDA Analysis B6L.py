#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[51]:


df = pd.read_csv('Mobilephone_prices.csv')


# In[52]:


df.head()


# In[53]:


df.info


# In[54]:


df.describe()


# In[55]:


df.value_counts()


# In[56]:


df.columns


# In[57]:


sns.jointplot(x='Y_Caala_sales', y='Phone_price_kz', data=df)


# In[58]:


sns.pairplot(df)


# In[59]:


df.corr()


# In[60]:


crr= df.corr()


# In[61]:


sns.heatmap(crr)


# In[62]:


sns.lmplot(x='Y_Caala_sales', y= 'Y_Shopping_sales', data=df, hue='Phone_brand')


# In[72]:


sns.lmplot(x='Y_Caala_sales', y= 'Phone_price_kz', data=df, hue='Phone_brand')


# In[70]:


sns.lmplot(x='Y_Caala_sales', y= 'Y_Shopping_sales', data=df, hue='Phone_price_kz')


# In[63]:


pd.value_counts(df['Y_Caala_sales'])


# In[64]:


pd.value_counts(df['Y_Shopping_sales'])


# In[65]:


df['Phone_brand']. unique()


# In[66]:


df['Phone_category']. unique()


# In[76]:


Caala= df['Y_Caala_sales'].sum()
print(Caala_tot)


# In[77]:


Shop= df['Y_Shopping_sales'].sum()
print(Shop_tot)


# In[78]:


df.Phone_name.str.split(expand=True).stack().value_counts()


# In[74]:


df.Phone_brand.str.split(expand=True).stack().value_counts()


# In[75]:


total_sales_sum= df['Y_Caala_sales'].sum() + df['Y_Shopping_sales'].sum()
print(total_sales_sum)


# In[79]:


df.Phone_category.str.split(expand=True).stack().value_counts()


# In[80]:


df.Phone_price_kz.hist()


# In[81]:


df.Y_Caala_sales.hist()


# In[82]:


df.Y_Shopping_sales.hist()


# In[89]:


sns.barplot(x='Phone_brand', y='Y_Caala_sales', data=df)


# In[88]:


sns.barplot(x='Phone_brand', y='Y_Shopping_sales', data=df)


# In[95]:


pd.pivot_table(df, index=['Y_Shopping_sales', 'Phone_category', 'Phone_brand'], values= 'Phone_price_kz')


# In[96]:


pd.pivot_table(df, index=['Y_Caala_sales', 'Phone_category', 'Phone_brand'], values= 'Phone_price_kz')


# In[ ]:




