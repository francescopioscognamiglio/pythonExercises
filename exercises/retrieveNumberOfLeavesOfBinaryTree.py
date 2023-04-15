#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 10:23:25 2023

Given a binary tree, retrieve the number of leaves.

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def countLeaves(node):
    if node == None: return 0
    if node.left == None and node.right == None: return 1
    return countLeaves(node.left) + countLeaves(node.right)


root = NodeBT(5)
root.left = NodeBT(19)
root.right = NodeBT(9)
root.left.left = NodeBT(3)
root.left.right = NodeBT(5)
root.right.left = NodeBT(11)
assert countLeaves(root) == 3
print(countLeaves(root))

root = NodeBT(5)
root.left = NodeBT(19)
root.right = NodeBT(9)
root.left.left = NodeBT(3)
root.left.right = NodeBT(5)
root.right.left = NodeBT(11)
root.right.right = NodeBT(12)
root.right.right.right = NodeBT(3)
root.right.right.right.right = NodeBT(4)
assert countLeaves(root) == 4
print(countLeaves(root))
