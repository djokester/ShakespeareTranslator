import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

count = 0
path="/home/anubhav10/Desktop/lbs"
total_pages=128
total_pages=int((total_pages/2))+1
for i in range(1,total_pages):
    temp=2*i
    url="http://nfs.sparknotes.com/errors/page_"+str(temp)+".html"
    file_name=path+str(temp)+".txt"
    r  =  requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,"lxml")
    stats = soup.find_all("div" ,{"class" : "original-line"})
    for stat in stats:
        data = stat.text
        file1 = open(file_name,'a+')
        file1.write(data)
    file1.write("#LBSFORGOLD")
    print("done")
    gender = soup.find_all("div" ,{"class" : "modern-line"})
    for gender_data in gender:
        data1 = gender_data.text          
        file1.write(data1)         
    count = count+1
    if(count%20==0):
        time.sleep(50)