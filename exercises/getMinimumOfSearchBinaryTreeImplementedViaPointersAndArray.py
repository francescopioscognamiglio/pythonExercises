#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:12:09 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def getMin(node):
    if node == None: return None
    if node.left == None: return node.key
    return getMin(node.left)

def getMinIterative(node):
    if node == None: return None
    while node.left != None: node = node.left
    return node.key

def getMinViaArray(A, i = 0):
    if i >= len(A): return None
    if 2*i+1 >= len(A) or A[2*i+1] == None: return A[i]
    return getMinViaArray(A, 2*i+1)

def getMinViaArrayIterative(A):
    if len(A) == 0: return None
    i = 0
    while 2*i+1 < len(A) and A[2*i+1] != None: i = 2*i+1
    return A[i]


root = NodeSBT(15)
root.left = NodeSBT(10)
root.left.left = NodeSBT(5)
root.left.right = NodeSBT(12)
root.right = NodeSBT(20)
root.right.left = NodeSBT(16)
root.right.right = NodeSBT(25)
root.right.right.left = NodeSBT(22)
assert getMin(root) == 5
assert getMinIterative(root) == 5
print(getMin(root))

A = [15, 10, 20, 5, 12, 16, 25, None, None, None, None, None, None, 22]
assert getMinViaArray(A) == 5
assert getMinViaArrayIterative(A) == 5
print(getMinViaArray(A))
