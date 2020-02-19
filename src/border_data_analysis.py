#!/usr/bin/env python
# coding: utf-8

import sys


#READING THE DATA FROM THE CSV FILE 
try:
    data=open(sys.argv[1],"r")
    k=data.readline()
    p=k.rstrip()
    field_names=p.split(',')
    table={}
except OSError as err:
    print("OS error: {0}".format(err))
    sys.exit()

for i in range(len(field_names)):
    table[field_names[i]]=[]

for i in data.readlines():
    li=i.rstrip()
    l=li.split(',')
    for n in range(len(table)):
        table[field_names[n]].append(l[n])
table['year_month']=[] 
 
    


# In[2]:


#SPLITTING THE DATE IN TO YEAR AND MONTH 
y=table['Date']
for i in y:
    d=i.split("/")
    month=d[0]
    yy=d[2].split(" ")
    year=yy[0]
    table['year_month'].append(str(year)+str(month))
    
    


# In[3]:


#IDENTIFYING THE UNIQUE VALUES FROM THE DATA
unique_table={}
unique_table={}
for i in table:
    unique_table[i]=[]
unique_table
for i in table:
    for j in table[i]:
        if j not in unique_table[i]:
            unique_table[i].append(j)


# In[4]:


#SORTING THE DATA IN TO DECREASING ORDER
unique_table['Border'].sort(reverse=True)
unique_table['Measure'].sort(reverse=True)
unique_table['year_month'].sort(reverse=True)


# In[5]:


mydata={}
mydata['Border']=[]
mydata['Date']=[]
mydata['Measure']=[]
mydata['Value']=[]


# In[6]:


#CALCULATING THE SUM OF CROSSINGS
value=[]
for i in unique_table['year_month']:
    for m in unique_table['Border']:
        for n in unique_table['Measure']:
            s=0
            for j in range(len(table['Border'])):
                 if m==table['Border'][j] and i==table['year_month'][j] and n==table['Measure'][j]:
                        try:
                            s=s+int(table['Value'][j])
                        except ValueError:
                            print("Could not convert data to an integer at value index"+str(j))
                            s=s+0
            if s!=0:
                     
                mydata['Border'].append(m)
                mydata['Date'].append(i)
                mydata['Measure'].append(n)
                mydata['Value'].append(s)
    
    
            
                
        
            
        
        
            
           


# In[7]:


#SORTING BASED ON THE DATE,VALUE ,MEASURE AND BORDER
list1=list(zip(mydata['Date'],mydata['Value'],mydata['Measure'],mydata['Border']))
k=sorted(list1,reverse=True)


# In[8]:


#CALCULATING THE AVERAGE OF THE CROSSINGS 
average=[]
for i in range(len(k)):
    count=0
    s1=0
    avg=0
    for j in range(len(k)):
        if k[i][0][:4]>=k[j][0][:4] and int(k[i][0][4:])>int(k[j][0][4:]) and k[i][2]==k[j][2] and k[i][3]==k[j][3]:
            s1=s1+int(k[j][1])
            count=count+1
    if count!=0:
                avg=s1/count
    if avg-round(avg)==0.5 and round(avg)%2==0:
        avg=round(avg)+1
        average.append(avg)
    else:
        average.append(round(avg))
    
    
    
    
    
        
        


# In[9]:


dt=list(zip(k,average))


# In[10]:


#WRITING RESULTS TO THE CSV FILE
try:
	f=open(sys.argv[2],"w")
	f.write("Border,Date,Measure,Value,Average")
	f.write("\n")
	for i in range(len(dt)):
		f.write(str(dt[i][0][3])+","+str(dt[i][0][0][4:])+"/01/"+str(dt[i][0][0][:4])+" "+"12:00:00 AM"+","+str(dt[i][0][2])+","+str(dt[i][0][1])+","+str(dt[i][1]))
		f.write("\n")
except OSError as err:
    print("OS error: {0}".format(err))
f.close()

