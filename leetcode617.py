#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:34:52 2018

@author: yanglinxuan
"""
# 617. Merge Two Binary Trees
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None


class Solution():
    def mergeTree(self,t1,t2):
        #type t1: TreeNode
        #type t2: TreeNode
        #rtype: TreeNode
        if t1 is not None and t2 is not None:
            t1.left=self.mergeTree(t1.left,t2.left)
            t2.right=self.mergeTree(t1.right,t2.right)
            t1.val=t2.val
            return t1
        return t1 if t2 is None else t2
    
 #tree 1   you may check...
t1=TreeNode(1)
t1.left=TreeNode(3)
t1.left.left=TreeNode(5)
t1.right=TreeNode(2)
 #tree 2
t2=TreeNode(2)
t2.left=TreeNode(1)
t2.left.right=TreeNode(4)
t2.right=TreeNode(3)
t2.right.right=TreeNode(7)


s=Solution()
print(s.mergeTree(t1,t2))
