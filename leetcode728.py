#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:26:47 2018

@author: yanglinxuan
"""

# 728. Self Dividing Numbers

def selfdivide(left,right):
    #type left,right:int
    #rtype: list[int]
    l=[]
    for i in range(left,right+1):
        a=str(i)
        l.append(i)
        for j in range(len(a)):
            if int(a[j])==0 or i%int(a[j])!=0:
                l.remove(i)
                break

    return l
                
            

print(selfdivide(11,30))

