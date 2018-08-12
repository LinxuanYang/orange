#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 00:33:27 2018

@author: yanglinxuan
"""

#804 unique morse code words

def transfer(word):
    
    dict_map = { "a":".-","b":"-...", "c":"-.-.", "d": "-..",
         "e":".", "f":"..-.","g":"--.", "h":"....", "i":"..",
         "j":".---","k":"-.-","l":".-..","m":"--","n":"-.",
         "o":"---","p":".--.","q":"--.-","r":".-.","s":"...",
         "t":"-","u":"..-","v":"...-","w":".--","x":"-..-",
         "y":"-.--","z":"--.."}
    trans=''
    for i in word:
        transchar=dict_map[i]
        trans=trans+transchar
    
    return trans
        
listofword=[]

def unique(trans):
    if trans not in listofword:
        listofword.append(trans)
        
    return len(listofword)
    
    

wordslist=["gin", "zen", "gig", "msg"]

a=[]
for i in wordslist:
    a.append(unique(transfer(i)))
    
print(a[len(a)-1])
    
