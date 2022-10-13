#!/usr/bin/env python
# coding: utf-8

# # Calling Dataset]

# In[1]:


import pandas as pd
df=pd.read_csv("supermarket_sales - Sheet1.csv")
df.head()


# In[2]:


df['Hour']=df['Time'].str[0:2]


# In[3]:


df.head(2)


# In[4]:


df.shape


# In[5]:


df.describe()


# # Cities

# In[6]:


df['City'].unique()


# # Customer Count

# In[7]:


df['City'].value_counts()


# # Total Sales

# In[8]:


total_sales=df.groupby('City').sum()
total_sales['Total'].sort_values(ascending=False)


# # Quantity Sales

# In[9]:


total_quantity=df.groupby('City').sum()
total_quantity['Quantity'].sort_values(ascending=False)


# # Customer type

# In[10]:


df['Customer type'].unique()


# In[11]:


df.groupby('Customer type').size()


# # Gender of Customer 

# In[12]:


df.groupby('Gender').size()


# # Payment Method

# In[13]:


df['Payment'].unique()


# In[14]:


df.groupby('Payment').size()


# # Each Product Line

# In[15]:


df['Product line'].unique()


# ## Total Sell

# In[16]:


product=df.groupby('Product line').sum()
product['Total'].sort_values(ascending=False)


# # Amount of Selling Quantity

# In[17]:


product['Quantity'].sort_values(ascending=False)


# # Gross Income

# In[18]:


product['gross income'].sort_values(ascending=False)


# In[19]:


df['gross margin percentage'].unique()


# ### Gross margin Parcentage is fixed for every product line.

# # Peak Hour-Off Peak Hour

# In[20]:


df['Hour']=df['Time'].str[0:2]


# In[21]:


df.head()


# In[22]:


copy_df=df.copy()


# In[23]:


copy_df


# In[24]:


df['Hour'].unique()


# In[25]:


df['Hour'].dtype


# In[26]:


df['Hour']=pd.to_numeric(df['Hour'])
df['Hour'].dtype


# In[27]:


hours=df.groupby('Hour').sum()
hours['Total']


# In[28]:


hours=df.groupby('Hour').sum()
hours['Quantity']


# In[29]:


df['Rating'].unique()


# In[30]:


#converting 'Rating' from float to int
df['Rating']=df['Rating'].astype('int')
df['Rating'].dtype


# In[75]:


df['Rating'].unique()


# In[32]:


df['Rating'].value_counts()


# # Rating on each product line

# In[33]:


df['Rating'].groupby(df['Product line']).median().sort_values(ascending=False)


# #  Analyze Each Branch

# In[34]:


gb=df.groupby('City')
Yangon_df=gb.get_group('Yangon')
Naypyitaw_df=gb.get_group('Naypyitaw')
Mandalay_df=gb.get_group('Mandalay')


# # Yangon Zone

# In[35]:


Yangon_df.groupby('Customer type').size()


# In[36]:


Yangon_df.groupby('Gender').size()


# In[37]:


Yangon_df.groupby(['Customer type', 'Gender']).size()


# In[38]:


Yangon_df.groupby('Payment').size().sort_values(ascending=False)


# In[39]:


Yangon_df['Total'].groupby(Yangon_df['Product line']).sum().sort_values(ascending=False)


# In[40]:


Yangon_df['Total'].groupby(Yangon_df['Hour']).sum().sort_values(ascending=False)


# In[41]:


Yangon_df['Quantity'].groupby(Yangon_df['Hour']).sum().sort_values(ascending=False)


# In[42]:


Yangon_df.groupby(['Gender', 'Customer type', 'Product line']).size().sort_values(ascending=False)


# In[43]:


Yangon_df['Quantity'].groupby(Yangon_df['Product line']).sum().sort_values(ascending=False)


# In[44]:


Yangon_df['Rating'].value_counts()


# In[73]:


Yangon_df['Rating'].groupby(Yangon_df['Product line']).median().sort_values(ascending=False)


# In[74]:


Yangon_df['Rating'].dtype


# # Naypyitaw Zone

# In[46]:


Naypyitaw_df.groupby('Customer type').size()


# In[47]:


Naypyitaw_df.groupby('Gender').size()


# In[48]:


Naypyitaw_df.groupby(['Customer type', 'Gender']).size()


# In[49]:


Naypyitaw_df.groupby('Payment').size().sort_values(ascending=False)


# In[50]:


Naypyitaw_df['Total'].groupby(Naypyitaw_df['Product line']).sum().sort_values(ascending=False)


# In[51]:


Naypyitaw_df['Quantity'].groupby(Naypyitaw_df['Product line']).sum().sort_values(ascending=False)


# In[52]:


Naypyitaw_df.groupby(['Gender', 'Customer type', 'Product line']).size().sort_values(ascending=False)


# In[53]:


Naypyitaw_df['Total'].groupby(Naypyitaw_df['Hour']).sum().sort_values(ascending=False)


# In[54]:


Naypyitaw_df['Quantity'].groupby(Naypyitaw_df['Hour']).sum().sort_values(ascending=False)


# In[55]:


Naypyitaw_df['Rating'].value_counts()


# In[56]:


Naypyitaw_df['Rating'].groupby(Naypyitaw_df['Product line']).median().sort_values(ascending=False)


# # Mandalay Zone

# In[57]:


df.head(10)


# In[58]:


Mandalay_df.groupby('Customer type').size()


# In[59]:


Mandalay_df.groupby('Gender').size()


# In[60]:


Mandalay_df.groupby(['Customer type', 'Gender']).size()


# In[61]:


Mandalay_df.groupby('Payment').size().sort_values(ascending=False)


# In[62]:


Mandalay_df['Total'].groupby(Mandalay_df['Product line']).sum().sort_values(ascending=False)


# In[63]:


Mandalay_df['Quantity'].groupby(Mandalay_df['Product line']).sum().sort_values(ascending=False)


# In[64]:


Mandalay_df.groupby(['Gender', 'Customer type', 'Product line']).size().sort_values(ascending=False)


# In[65]:


Mandalay_df['Total'].groupby(Mandalay_df['Hour']).sum().sort_values(ascending=False)


# In[66]:


Mandalay_df['Quantity'].groupby(Mandalay_df['Hour']).sum().sort_values(ascending=False)


# In[67]:


Mandalay_df['Rating'].value_counts()


# In[68]:


Mandalay_df['Rating'].groupby(Mandalay_df['Product line']).median().sort_values(ascending=False)

