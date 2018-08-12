#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 21:01:24 2018

@author: yanglinxuan
"""
#leetcode339
#Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

#Each element is either an integer, or a list -- whose elements may also be integers or other lists.

#Example 1:
#Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

#Example 2:
#Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)


        
            

a=[[3,[1,2]],1,2,6,8]

def getsum(dep,a):
    total=0
    print('total is',total)
    for i in a:
        print('now we test:',i)
        if isinstance(i,int):
            print('it is int')
            total=total+i*dep
            print('total=',total)
        else:
            print('it is not int')
            print('dep=',dep+1,'i:',i)
            total=total+getsum(dep+1,i)
            #the most important part, when call recur, we should 
            #always add the previous result to the next call
        
    return total
    

print(getsum(1,a))