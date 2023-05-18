#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:34:41 2023

@author: scognamigliofrancescopio@gmail.com
"""

class BinaryNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def maxPath(BT, k = 0):
    if BT == None: return k-1
    left = maxPath(BT.left, k+1)
    right = maxPath(BT.right, k+1)
    return max(left, right)


root = BinaryNode(10)
print(maxPath(root))
root.left = BinaryNode(15)
root.right = BinaryNode(110)
print(maxPath(root))
root.left.left = BinaryNode(22)
root.left.left.left = BinaryNode(55)
print(maxPath(root))
