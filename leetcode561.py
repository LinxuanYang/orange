#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 23:39:25 2018

@author: yanglinxuan
"""

#561 array partition 1

#Given an array of 2n integers, your task is to group these 
#integers into n pairs of integer, say (a1, b1), (a2, b2), ..., 
#(an, bn) which makes sum of min(ai, bi) for all i 
#from 1 to n as large as possible.
    
a=[2,5,4,1,6,5]
a.sort()
print(a)


b=a[0::2]
print(b)
c=0
for i in b:
    c+=i
print(c)



