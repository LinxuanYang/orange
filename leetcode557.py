#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:16:46 2018

@author: yanglinxuan
"""
"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

"""

s="Let's take LeetCode contest"

def reservewords(s):
   l=s.split(sep=None,maxsplit=-1)
   ll=[]
   for i in l:
       ll.append((i[::-1]))
       #[::-1] 的意思是从前面这个i的范围里，起始位置是0，结束是最后一个，然后
       # 每次下一个的间距是－1，所以这个从最后一个开始往前走，i[::-1]结果是一个新的东西
       #如果i='abc'那么i[::－1]=‘cba'
   
   ll[::]=[' '.join(ll[::])]
   # 如果 list=['a','b','c','d','e','f'],那么首先list[1:3]=['b'，'c'],然后我们想把这两个合起来然后还用‘ ’分开
   # 所以join后面的范围和前面的要一致。当我们合起来以后再看list[1:3]=['b c','d']
   return ll[0]
      
       
       
ll=reservewords(s)

print(type(ll))

       
# for list, join elements in list: ll[::]=[' '.join(ll[::])]