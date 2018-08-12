#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:02:03 2018

@author: yanglinxuan
"""

#leetcode 771. Jewels and Stones

# Strings J = types of stones that are jewels
# String S = stones you have
# Input
# J = "aA", S = "aAAbbbb"
# Output
# 3
# create a dictionary where the key is the char and the value is 
#the number of occurrences

def jewels(S,J):
    jewelss={x:0 for x in J}
    for i in S:
        for j in jewelss.keys():
            if i==j:
                jewelss[j]=jewelss[j]+1
                
    return jewelss
  


J = "aZAb"
S = "aAAizbbbbc"
j=jewels(S,J)


# or if we just need the sum of jewels we have 

def findj(S,J):
    count=0
    for i in S:
        for j in J:
            if i==j:
                count+=1
    return count

print('we have sum=',findj(S,J))


# FOR FUN
sum=0
for i in J:
    print('i are:',i)
    
    sum=sum+j[i]
    print(sum)

print('sum is=',sum)
  