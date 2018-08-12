#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 17:35:10 2018

@author: yanglinxuan
"""

#Leetcode 762:Prime Number of Set Bits in Binary Representation

class Solution:
    
    def binary(n):
        s=bin(n)
        s1=s[2:]
        return s1

    def countones(n):
        count=0
        s1=binary(n) 
        for i in range(0,len(s1)):
            if int(s1[i])==1:
                count=count+1   
                return count 
    
    def isprime(n):
        if n==1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False 
            return True 

    def countPrimeSetBits(self,L,R):
        count=0
        for i in range(L,R+1):
            if isprime(countones(i)):
                count=count+1
        return count
    
solution=Solution()
print(solution.countPrimeSetBits(10,15))