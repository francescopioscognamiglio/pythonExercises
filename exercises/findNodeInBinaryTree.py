#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:32:24 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def findNode(node, x):
    if node == None: return False
    if node.key == x: return True
    return findNode(node.left, x) or findNode(node.right, x)


root = NodeBT(19)
root.left = NodeBT(2)
root.left.left = NodeBT(14)
root.left.right = NodeBT(24)
root.right = NodeBT(4)
root.right.left = NodeBT(11)
root.right.right = NodeBT(13)
print(findNode(root, 11))
print(findNode(root, 444))
