#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 13:47:48 2018

@author: yanglinxuan
"""
#leetcode 359 logger rate limiter 
"""
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.
"""


dic={}
def shouldprint(timestamp,msg):
    """
    timestamp type: int
    msg type: str
    r type: boolean
    """
    if msg in dic.keys():
        print(timestamp,'-',dic[msg])
        if timestamp-dic[msg]>=10:
            dic[msg]=timestamp
            return True 
        else: #less than 10
            return False
    else:
        dic[msg]=timestamp
        return True
        


print(shouldprint(1,'foo'))
print(shouldprint(2,'bar'))
print(shouldprint(3,'foo'))
print(shouldprint(8,'bar'))
print(shouldprint(10,'foo'))
print(shouldprint(11,'foo'))
        
    




