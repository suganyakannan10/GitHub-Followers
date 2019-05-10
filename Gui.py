
# coding: utf-8

# In[7]:


import tkinter as tk
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv


# In[ ]:


Height=400
Width=500

def get_csv(userlink):  
      
        df = pd.read_csv('./ALLUser.csv',header=0)
        df.columns=['Name','Repository','Project','Stars','Followers','Following','Link']
        df.to_string(justify='left')
        df['Percent']=0
        df['Percent']=df['Followers']/len(df.Name)*100
        df['Percent']=round(df['Percent'],0)        
        m=df.Link.isin([userlink])
        
        m2=df[m].Percent
        v=m2.values[0]
        m3=' is in the top\n '
        m5='% of the Melbourne Github users based on followers'
        m4=userlink+ m3+str(v)+m5
        
       
        label['text']=m4
        
top = tk.Tk()

canvas = tk.Canvas(top,height=Height, width=Width)
canvas.pack()

frame=tk.Frame(top, bg='#008fb3', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1,anchor='n')

entry = tk.Entry(frame, font=30)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Run",font=40, command=lambda:get_csv(entry.get()))
button.place(relx=0.7,relwidth=0.3, relheight=1)

lower_frame = tk.Frame(top,bg='#008fb3',bd=5)
lower_frame.place(relx=0.5, rely=0.26,relwidth=0.75,relheight=0.6,anchor='n')


label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)


top.mainloop()

