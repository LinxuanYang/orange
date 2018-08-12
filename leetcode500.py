#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:45:55 2018

@author: yanglinxuan
"""

#leetcode 500 keyboard row


s=["Hello", "Alaska", "Dad", "Peace"]

def findwords(s):
    """
    type s: list[str]
    rtype: list[str]
    """
    z=[]
    set1='qwertyuiop'
    set2='asdfghjkl'
    set3='zxcvbnm'
    
    for i in s:
        lower=i.lower()
        #这里要赋值，不然i还是本来的i，不会变lower
        if all(j in set1 for j in lower) or all(j in set2 for j in lower) or all(j in set3 for j in lower) :
            z.append(i) 
    return z


print(findwords(s))
            
        
        



        