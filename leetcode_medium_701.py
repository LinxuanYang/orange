"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed
that the new value does not exist in the original BST.
Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.
"""


class TreeNode():
    #construction to create new node
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution(object):
    def insert_into_bst(self, node, val):
        """

        :param node:  treenode
        :param val: int
        :return: treenode
        """
        #if TreeNode is false, means there is no such TreeNode
        #here root is the TreeNode we have
        if not node:
            return TreeNode(val)
        if val < node.value:
            node.left = self.insert_into_bst(node.left, val)
        else:
            node.right = self.insert_into_bst(node.right, val)
        return node

mytree = TreeNode(4)
mytree.left = TreeNode(2)
mytree.right = TreeNode(7)
mytree.left.left = TreeNode(1)
mytree.left.right = TreeNode(3)

mysol = Solution()
mysol.insert_into_bst(mytree, 5)
print(mytree.value)
print(mytree.right.value)
print("4 left ", mytree.left.value)
print("2 left", mytree.left.left.value)
print(mytree.right.left.value)





