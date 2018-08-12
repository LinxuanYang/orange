#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 00:28:49 2018

@author: yanglinxuan
"""



# leetcode 811 subdomain visit count
"""
A website domain like “discuss.leetcode.com” consists of various subdomains. 
At the top level, we have “com”, at the next level, we have “leetcode.com”, 
and at the lowest level, “discuss.leetcode.com”. 
When we visit a domain like “discuss.leetcode.com”, 
we will also visit the parent domains “leetcode.com” and “com” implicitly.

Now, call a “count-paired domain” to be a count 
(representing the number of visits this domain received), 
followed by a space, followed by the address. 
An example of a count-paired domain might be “9001 discuss.leetcode.com”.
We are given a list cpdomains of count-paired domains. 
We would like a list of count-paired domains, 
(in the same format as the input, and in any order), 
that explicitly counts the number of visits to each subdomain.
"""
s=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]


def countsubdomains(s):
    dic={}
    for i in s:
        print('now we test:',i)
        times,domains=i.split(sep=None,maxsplit=-1)
        times=int(times)
        dic[domains]=times
        
        b=domains.split(sep='.',maxsplit=-1)
        print(b)
        for j in range(0,len(b)):
            if j!=len(b)-1:
                s=b[j]+'.'+b[len(b)-1]
                if s in dic:
                    dic[s]+=times
                else:
                    dic[s]=times
            else:
                if b[len(b)-1] in dic:
                    dic[b[len(b)-1]]+=times
                else:
                    dic[b[len(b)-1]]=times
    l=[]
    for key,val in dic.items():
        s=str(val)+' '+key
        l.append(s)
    return l
 
print(countsubdomains(s))
    
def subdomainvisit(s):
    dic={}
    for i in s:
        times,domains=i.split(sep=None,maxsplit=-1)
        times=int(times)
        if domains in dic:
            dic[domains]+=times
        else:
            dic[domains]=times
        while '.' in domains:
            domains=domains[domains.index('.')+1:]
            if domains in dic:
                dic[domains]+=times
            else:
                dic[domains]=times
    return[str(v)+' '+d for d,v in dic.items()]
    
print(subdomainvisit(s))
        
        




