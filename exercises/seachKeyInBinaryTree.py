#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:08:37 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def searchKey(node, k):
    if node == None: return None
    if node.key == k: return node
    return searchKey(node.left, k) or searchKey(node.right, k)


root = NodeBT(10)
root.left = NodeBT(15)
root.right = NodeBT(12)
root.left.left = NodeBT(5)
root.left.right = NodeBT(11)
root.right.left = NodeBT(3)
root.right.right = NodeBT(5)
print(searchKey(root, 3))
print(searchKey(root, 222))
