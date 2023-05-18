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

def minPath(BT, k = 0):
    if BT == None: return k-1
    left = minPath(BT.left, k+1)
    right = minPath(BT.right, k+1)
    return min(left, right)


root = BinaryNode(10)
print(minPath(root))
root.left = BinaryNode(15)
root.right = BinaryNode(110)
print(minPath(root))
root.left.left = BinaryNode(22)
root.left.left.left = BinaryNode(55)
print(minPath(root))
root.left.right = BinaryNode(25)
root.left.left.right = BinaryNode(223)
root.right.left = BinaryNode(45)
root.right.right = BinaryNode(12)
print(minPath(root))
root.left.right.left = BinaryNode(77)
root.left.right.right = BinaryNode(45)
root.right.left.left = BinaryNode(47)
root.right.left.right = BinaryNode(56)
root.right.right.left = BinaryNode(32)
root.right.right.right = BinaryNode(89)
print(minPath(root))
