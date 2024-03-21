#!/usr/bin/env python
# coding: utf-8

# #  T20 World Cup

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[14]:


url = 'https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450'
page = requests.get(url)


# In[15]:


soup = BeautifulSoup(page.text,'html')


# In[16]:


print(soup)


# In[17]:


soup.find('table')


# In[22]:


table = soup.find('table')


# In[23]:


print(table)


# In[31]:


table_title = table.find_all('tr')[0]


# In[35]:


t_title = table_title.find_all('td')


# In[36]:


print(t_title)


# In[37]:


match_result_title = [title.text.strip() for title in t_title]

print(match_result_title)


# In[38]:


import pandas as pd


# In[39]:


df = pd.DataFrame(columns = match_result_title )
df


# In[45]:


column_data = table.find_all('tr')[1:]


# In[46]:


print(column_data)


# In[47]:


for Row in column_data:
    row_data = Row.find_all('td')
    individual_row_data = [rdata.text.strip() for rdata in row_data ]
    print(individual_row_data)


# In[48]:


for Row in column_data[1:]:
    row_data = Row.find_all('td')
    individual_row_data = [rdata.text.strip() for rdata in row_data ]
    
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[49]:


df


# In[51]:


df.to_csv(r'C:\sem4\Data anylist\Cricket project\Matchresult.csv',index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




