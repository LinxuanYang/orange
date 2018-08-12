#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:10:55 2018

@author: yanglinxuan
"""

# leetcode 344 reverse string

s='hello'
def reverse(s):
    l=''
    for i in range (len(s)):
        print(s[i])
        l+=(s[len(s)-1-i])
    return l

print(reverse(s))


        