#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 00:08:32 2018

@author: yanglinxuan
"""

# leetcode 476 number complement
"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
"""

def numcom(num):
    s1=bin(num)
    s=s1[2:]
    newstring=''
    for i in range(len(s)):
        if int(s[i]) == 1:
            newstring+='0'
        else:
            newstring+='1'
    
    return int(newstring,2)


print(numcom(5))
    
