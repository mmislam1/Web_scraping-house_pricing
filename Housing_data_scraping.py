#!/usr/bin/env python
# coding: utf-8

# In[14]:


from bs4 import BeautifulSoup
import requests
import xlsxwriter

def getter(s):
    url = s

    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

    soup = BeautifulSoup(html_content, 'lxml')
    
    return soup

#print(soup)


# In[2]:


def extractor(a):
    l=[]
    for i in a:
        l.append(i.text)
        
    return l


# In[3]:


def finder(soup,element,class_):    
    x=soup.find_all(element,class_=class_)
    return x



# In[4]:


def linker(a):
    l=[]
    for i in a:
        l.append("https://www.newhomeco.com"+(i.find('a')['href']))
        
    return l


# In[8]:


def filer(a):
    workbook = xlsxwriter.Workbook('House pricing.xlsx')
 
    worksheet = workbook.add_worksheet("Pricing Sheet")
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            
            worksheet.write(i+1,j,a[i][j])
            
            
    
    workbook.close()
    
    
    


# In[15]:


base="https://www.newhomeco.com/promotions/"

pages=['colorado','northern-california','arizona','houston','southern-california']

element='div'

prices_class="field field--name-field-neighborhood-title-line-on field--type-string field--label-hidden field__item"

location_class='field field--name-field-neighborhood-title-line-tw field--type-string field--label-hidden field__item'

results=[]

for i in pages:
    soup=getter(base+i)
    
    prices_raw=finder(soup,element,prices_class)
    prices=extractor(prices_raw)
    
    links=linker(prices_raw)
    
    locations_raw=finder(soup,element,location_class)
    locations=extractor(locations_raw)
    
    
    for j in range(len(prices)):
        
        result=[i,locations[j],prices[j],links[j]]
        results.append(result)
    
filer(results)


# In[ ]:




