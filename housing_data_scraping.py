#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests

url = "https://www.newhomeco.com/promotions/colorado"

response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

soup = BeautifulSoup(html_content, 'lxml')

print(soup)


# In[1]:





# In[5]:


x=soup.find_all('div',class_="field field--name-field-strike-through-price field--type-string field--label-hidden field__item")

print(x)


# In[ ]:




