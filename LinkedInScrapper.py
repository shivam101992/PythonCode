from time import sleep
import random as ra
import regex as re
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome("/Users/shreyaankaushal/Downloads/chromedriver")
import h5py
import numpy as np



a = read_hdf('final.h5', 'LI')
array = np.array(a)
master=array[100:300] # yahan split specify karde (try running 1000 each ke chaar VMs)
print master
data =[]
useragent=["Mozilla/5.0"]
def pullData(profile_link):
    #opener = urllib2.build_opener()
    #opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #response = opener.open(profile_link)
    #page = response.read()
    #You have to insert User agent randomization and IP rotation here 
    driver.get(profile_link) #gets the page for that particular link
    html=driver.page_source
    soup=BeautifulSoup(html) 
    temp =[]
    person =[]
    name = soup.find('h1',{"id":"name"})
    print name.getText() #name
    location = soup.find('span',{"class":"locality"})
    print location.getText() #location
    #list of designation
    designation = soup.find_all('li',{"class":"position"})
    tempdesig=[]
    for d in designation:
        for pos in d.find_all('h4',{"class":"item-title"}):
            if pos.find('a') == True:
                tempdesig.append(pos.find('a').getText())
            else:
                tempdesig.append(pos.getText())    
    print tempdesig

    #list of companies where designation held
    designation = soup.find_all('li',{"class":"position"})
    tempcomp=[]
    for d in designation:
        for company in d.find_all('h5',{"class":"item-subtitle"}):
            if company.find('a') == True:
                tempcomp.append(company.find('a').getText())
            else:
                tempcomp.append(company.getText())    
    print tempcomp


    #list of dates for which designation held
    designation = soup.find_all('li',{"class":"position"})
    tempdate=[]
    for d in designation:
        for company in d.find_all('span',{"class":"date-range"}):
            if company.find('a') == True:
                tempdate.append(company.find('a').getText())
            else:
                tempdate.append(company.getText())    
    print tempdate
    work=[]
    for i in range(len(tempcomp)):
        work.append([tempdesig[i],tempcomp[i],tempdate[i]])
       
    #List of Univeristies attended 

    education = soup.find_all('li',{"class":"school"})
    print "                                     "
    tempuni=[]
    for e in education:
        for degree in e.find_all('h4',{"class":"item-title"}):
            if degree.find('a') == True:
                tempuni.append(degree.find('a').getText())
            else:
                tempuni.append(degree.getText())    
    print tempuni

   #List of degree (time mile tho degree aur major bhi seperate kardiyo, not urgent)

    education = soup.find_all('li',{"class":"school"})
    print "                                     "
    tempmajor=[]
    for e in education:
        for degree in e.find_all('span',{"data-field-name":"Education.DegreeName"}):
            if degree.find('a') == True:
                tempmajor.append(degree.find('a').getText())
                break;
            else:
                tempmajor.append(degree.getText())
                break;
    print tempmajor
    person.append([name.getText(),location.getText(),tempdesig,tempcomp,tempdate,tempuni,tempmajor,profile_link]) 
    print "\n"
    data.append(person)

count=0;
for persons in master:
    count=count+1
    if count%10==0:
        sleep(ra.randint(1,5))
    if count%50==0:
        sleep(ra.randint(3,10))
    sleep(ra.random())
    try:
        sleep(ra.random())
        sleep(ra.random())
        pullData(persons)
    except:
        continue

    
import csv
result = open("finaljobs.csv",'wb')
wr = csv.writer(result, dialect='excel')
result2 = open("finaleducation.csv",'wb')
wr2 = csv.writer(result2, dialect='excel')
#wr.writerow([1,2,3,4])

for x in data:
    name = x[0][0].encode("utf-7")
    location = x[0][1].encode("utf-7")
    profile = x[0][7].encode("utf-7")
    for y in range(0, len(x[0][2])):
        desig = x[0][2][y].encode("utf-7")
        comp = x[0][3][y].encode("utf-7")
        date = x[0][4][y].encode("utf-7")
        #print desig
        list = []
        list.extend([profile, name, location, desig, comp, date])
        wr.writerow(list)
    for y in range(0, len(x[0][5])):
        unit = x[0][5][y].encode("utf-7")
        degree = x[0][6][y].encode("utf-7")
        list = []
        list.extend([profile, name, location, unit, degree])
        wr2.writerow(list)
     
        

result.close()
result2.close()

