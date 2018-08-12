#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 00:48:43 2018

@author: yanglinxuan
"""

#flipping an image 
#frist reverse each row,then invert the image

def fct(A):
    newmatrix=[]
    for i in A:
        test=[]
        for j in range (len(i)-1,-1,-1):
            if i[j]==0:
                i[j]=1
                test.append(i[j])
            else:
                i[j]=0
                test.append(i[j])
            
        newmatrix.append(test)
    return newmatrix
            


A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(fct(A))
    

