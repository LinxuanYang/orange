#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:29:08 2018

@author: yanglinxuan
"""
# 657. Judge Route Circle

def judgecircle(moves):
    # type moves:str
    # rtype: bool
    return moves.count('U')==moves.count('D') and moves.count('L')== moves.count('R')


m='UDLR'
print(judgecircle(m))


