
# coding: utf-8

# In[2]:

import requests
url = 'https://info.xsede.org/wh1/rdr-db/v1/rdr/'
response = requests.get(url)
data = response.json()
data
raw = response.text


# In[4]:

import pandas as pd

df = pd.read_json(raw)
df.to_csv('xsede-resources.csv')
df


# In[51]:

a = df[df['current_statuses']=='production']
b = a[a['provider_level']=='XSEDE Level 1']
b[['resource_descriptive_name','rdr_type','recommended_use','resource_description','other_attributes','updated_at','rdr_resource_id']].sort_values(['rdr_type','resource_descriptive_name'])


# In[ ]:



