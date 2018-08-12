#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:03:48 2018

@author: yanglinxuan
"""

#

    
def binary(a):
    s1=bin(a)
    s2=s1[2:]
    return s2
      
def samelenth(a,b):
    l=''
    for i in range(len(b)-len(a)):
        l=l+'0'
    a=l+a
    return a
    
def hammingDistance(x,y):
    if x>y:  #always make x<y
        c=0
        c=x
        x=y
        y=c   
        
    a=binary(x)
    b=binary(y)
    count=0
    a=samelenth(a,b)
    for i in range (len(a)):
        if a[i]!=b[i]:
            count+=1
                
    return count
        

print(hammingDistance(1,4))

#or we can a very short version.

def shortone(x,y):
    a=binary(x^y)
    count=0
    print(a,len(a),a[1])
    for i in range(len(a)):
        if int(a[i])==1:
            count+=1
            
    return count

print(shortone(1,4))