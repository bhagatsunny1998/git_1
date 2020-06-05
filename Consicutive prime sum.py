# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:19:33 2020

@author: Sunnykumar Bhagat
"""


val = int(input("Enter number: "))  
 
count = 0  

a = []
for num in range(2,val+1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:
           
           
           a.append(num)
           
           
  

for i in range(1, len(a)):
    
    sum =0
    for j in a:
        sum = sum +j
        if sum == a[i]:
            print(sum)
            count = count + 1
            
        if sum >a[i]:
            break
         
print("Consicutive prime sum are :",count)


