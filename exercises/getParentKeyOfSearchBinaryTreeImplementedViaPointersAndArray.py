#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:44:45 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def getParentKey(node, key):
    if not node: return None
    if (node.left and node.left.key == key) or (node.right and node.right.key == key):
        return node.key
    if key > node.key: return getParentKey(node.right, key)
    return getParentKey(node.left, key)

def getParentKeyIterative(node, key):
    if not node: return None
    while node.left or node.right:
        if node.left and node.left.key == key: return node.key
        if node.right and node.right.key == key: return node.key
        if key > node.key: node = node.right
        else: node = node.left
    return None # no key found

def getParentKeyViaArray(A, key, i = 0):
    if i >= len(A): return None
    if (2*i+1 < len(A) and A[2*i+1] == key) or (2*i+2 < len(A) and A[2*i+2] == key):
        return A[i]
    if key > A[i]: return getParentKeyViaArray(A, key, 2*i+2)
    return getParentKeyViaArray(A, key, 2*i+1)

def getParentKeyViaArrayIterative(A, key):
    i = 0
    while (2*i+1 < len(A) and A[2*i+1] != None) or (2*i+2 < len(A) and A[2*i+2] != None):
        if 2*i+1 < len(A) and A[2*i+1] == key: return A[i]
        if 2*i+2 < len(A) and A[2*i+2] == key: return A[i]
        if key > A[i]: i = 2*i+2
        else: i = 2*i+1
    return None # no key found


root = NodeSBT(15)
root.left = NodeSBT(10)
root.left.left = NodeSBT(5)
root.left.right = NodeSBT(12)
root.right = NodeSBT(20)
root.right.left = NodeSBT(16)
root.right.right = NodeSBT(25)
root.right.right.left = NodeSBT(22)
assert getParentKey(root, 12) == 10
assert getParentKeyIterative(root, 12) == 10
print(getParentKey(root, 12))

A = [15, 10, 20, 5, 12, 16, 25, None, None, None, None, None, None, 22]
assert getParentKeyViaArray(A, 12) == 10
assert getParentKeyViaArrayIterative(A, 12) == 10
print(getParentKeyViaArray(A, 12))
