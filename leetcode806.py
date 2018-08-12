#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 00:06:44 2018

@author: yanglinxuan
"""

#leetcode 806 number of lines to write string

widths=[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
#the width of each letter 

s="bbbcccdddaaa"


print(ord('a'))
print(ord('c'))
print(ord('b'))
def lines(widths,s):
    """
    type widths: list[int]
    type s: str
    rtype: list[int]
    """
    
    line=1
    widcount=0
    for i in s:
        wid=widths[ord(i)-ord('a')]
        widcount=widcount+wid
        if widcount>100:
            line=line+1
            widcount=wid
            
    return (line,widcount)

print(lines(widths,s))
    

        
