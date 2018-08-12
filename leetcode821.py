#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 23:05:43 2018

@author: yanglinxuan
"""
s = 'loveleetcode'
c = 'e'


def shortdis(s,c):
    """
    Given a string S and a character C, 
    return an array of integers representing the shortest distance 
    from the character C in the string.
    
    s type: str
    c type: str
    r type: list[int]
    """
    l=[-1]*len(s)
    zeroindex=[]
    #first locate all e's and record their location as 0 in l
    for i in range (len(s)):
        
        if s[i] is c :
            l[i]=0
            zeroindex.append(i)
        
    #compare the absolute value of distance bwtween each char and every 0
    print(zeroindex)
    for i in range(len(l)):
        distance=[]
        for j in zeroindex:
            diff=abs(i-j)
            distance.append(diff)
        l[i] = min(distance)
    
    return l


print(shortdis(s,c))
        


    
    