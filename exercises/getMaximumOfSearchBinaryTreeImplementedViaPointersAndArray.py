#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:06:35 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def getMax(node):
    if node == None: return None
    if node.right == None: return node.key
    return getMax(node.right)

def getMaxIterative(node):
    if node == None: return None
    while node.right != None: node = node.right
    return node.key

def getMaxViaArray(A, i = 0):
    if i >= len(A): return None
    if 2*i+2 >= len(A) or A[2*i+2] == None: return A[i]
    return getMaxViaArray(A, 2*i+2)

def getMaxViaArrayIterative(A):
    if len(A) == 0: return None
    i = 0
    while 2*i+2 < len(A) and A[2*i+2] != None: i = 2*i+2
    return A[i]


root = NodeSBT(15)
root.left = NodeSBT(10)
root.left.left = NodeSBT(5)
root.left.right = NodeSBT(12)
root.right = NodeSBT(20)
root.right.left = NodeSBT(16)
root.right.right = NodeSBT(25)
root.right.right.left = NodeSBT(22)
assert getMax(root) == 25
assert getMaxIterative(root) == 25
print(getMax(root))

A = [15, 10, 20, 5, 12, 16, 25, None, None, None, None, None, None, 22]
assert getMaxViaArray(A) == 25
assert getMaxViaArrayIterative(A) == 25
print(getMaxViaArray(A))
