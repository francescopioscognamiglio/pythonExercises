#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:03:27 2023

Given a tree, count the number of nodes.

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def countNodes(node):
    if node == None: return 0
    return countNodes(node.left) + countNodes(node.right) + 1


root = NodeBT(10)
root.left = NodeBT(12)
root.right = NodeBT(74)
root.left.left = NodeBT(44)
root.left.left.left = NodeBT(52)
root.left.left.right = NodeBT(3)
root.left.right = NodeBT(15)
root.left.right.left = NodeBT(33)
root.left.right.right = NodeBT(13)
root.right.right = NodeBT(55)
root.right.right.right = NodeBT(0)
root.right.right.right.right = NodeBT(1)
print(countNodes(root))
