#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 14:46:47 2018

@author: yanglinxuan
"""

#leetcode 346. Moving Average from Data Stream

import queue
a=3
l=queue.Queue(maxsize=a)
#insert element
l.put(1)


#get and remove element 
l.get()



size=10
summ = 0
l1=queue.Queue()
def nextone(val):
    global summ
    if l1.qsize()<size:
        print('before we add,we have size:',l1.qsize(),'it is less than window size',size)
        summ = summ + val
        print('we have sum',summ)
        l1.put(val)
        print('after add this int we have size:',l1.qsize())
        print('we have avg:',summ/l1.qsize())
        return summ/l1.qsize()
    else:
        print('so far we already reach zise 10 before adding',val)
        summ=summ-l1.get()
        print('minus the very first one',summ)
        l1.put(val)
        summ=summ+val
        return summ/size



r=[]
for i in range(13):
    print(end='\n')
    print('we want to add ingeter:',i)
    r.append(nextone(i))
    
    
print(r)
        
    