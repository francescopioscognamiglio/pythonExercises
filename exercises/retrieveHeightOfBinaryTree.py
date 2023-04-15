#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 10:21:59 2023

Given a binary tree, retrieve the height.

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def retrieveHeight(node):
    if node == None: return -1
    hleft = retrieveHeight(node.left)
    hright = retrieveHeight(node.right)
    return max(hleft, hright) + 1


root = NodeBT(5)
root.left = NodeBT(19)
root.right = NodeBT(9)
root.left.left = NodeBT(3)
root.left.right = NodeBT(5)
root.right.left = NodeBT(11)
assert retrieveHeight(root) == 2
print(retrieveHeight(root))

root = NodeBT(5)
root.left = NodeBT(19)
root.right = NodeBT(9)
root.left.left = NodeBT(3)
root.left.right = NodeBT(5)
root.right.left = NodeBT(11)
root.right.right = NodeBT(12)
root.right.right.right = NodeBT(3)
root.right.right.right.right = NodeBT(4)
assert retrieveHeight(root) == 4
print(retrieveHeight(root))
