
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv


# In[2]:


#user_link=['https://github.com/MelbourneDeveloper','https://github.com/JacksonBates']
links=[]
for num in range(59,60):
    
    print(num) 
    
    time.sleep(3)
    url2='https://github.com/search?l=&p='+str(num)+'&q=melbourne+location%3Amelbourne+location%3Amelbourne&ref=advsearch&type=Users&utf8=%E2%9C%93'    
    page = requests.get(url2)
    soup = BeautifulSoup(page.text,'html.parser')
    results = soup.findAll('a', class_='d-table')
    #links=[]
    
    
    for i in results:        
        user_name = i.get('href').split('/')[1]
        user_link ='https://github.com' + '/'+user_name
        links.append(user_link)
        
        data=[]
        for i in links:    
            time.sleep(3)
            page = requests.get(i)
            soup = BeautifulSoup(page.text, 'lxml')
            result1=soup('title')
            result2=soup('span', class_='Counter')
            
            if len(result2)<4:
                Name = result1[0].text.strip('· GitHub')
                Repository=result2[0].text.strip()
                Projects=0
                Stars=0
                Followers=0          
                Following=0
                data.append([Name,Repository,Projects,Stars,Followers,Following,i])

            else:
                Name = result1[0].text.strip('· GitHub')
                Repository=result2[0].text.strip()
                Projects=result2[1].text.strip()
                Stars=result2[2].text.strip()
                Followers=result2[3].text.strip()          
                Following=result2[4].text.strip()
                data.append([Name,Repository,Projects,Stars,Followers,Following,i])

        df=pd.DataFrame(data)

        df.to_csv('Github_User.csv',index=None,encoding='utf-8',header=True)
            
           


# In[3]:


#print(data)


# In[4]:


print(links)


# In[5]:


df


# In[6]:


#print(data)

