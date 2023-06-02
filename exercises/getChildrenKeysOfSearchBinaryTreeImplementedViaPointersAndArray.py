#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:47:06 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def getChildrenKeys(node, key):
    if not node: return None, None
    if node.key == key:
        if node.left and node.right: return node.left.key, node.right.key
        elif node.left: return node.left.key, None
        else: return None, node.right.key
    if key > node.key: return getChildrenKeys(node.right, key)
    return getChildrenKeys(node.left, key)

def getChildrenKeysIterative(node, key):
    while node:
        if node.key == key:
            if node.left and node.right: return node.left.key, node.right.key
            elif node.left: return node.left.key, None
            elif node.right: return None, node.right.key
            else: return None, None
        if key > node.key: node = node.right
        else: node = node.left
    return None, None # no key found

def getChildrenKeysViaArray(A, key, i = 0):
    if i >= len(A): return None, None
    if A[i] == key:
        if 2*i+1 < len(A) and 2*i+2 < len(A): return A[2*i+1], A[2*i+2]
        elif 2*i+1 < len(A): return A[2*i+1], None
        elif 2*i+2 < len(A): return None, A[2*i+2]
        else: return None, None
    if key > A[i]: return getChildrenKeysViaArray(A, key, 2*i+2)
    return getChildrenKeysViaArray(A, key, 2*i+1)

def getChildrenKeysViaArrayIterative(A, key):
    i = 0
    while i < len(A):
        if A[i] == key:
            if 2*i+1 < len(A) and 2*i+2 < len(A): return A[2*i+1], A[2*i+2]
            elif 2*i+1 < len(A): return A[2*i+1], None
            elif 2*i+2 < len(A): return None, A[2*i+2]
            else: return None, None
        if key > A[i]: i = 2*i+2
        else: i = 2*i+1
    return None, None # no key found


root = NodeSBT(15)
root.left = NodeSBT(10)
root.left.left = NodeSBT(5)
root.left.right = NodeSBT(12)
root.right = NodeSBT(20)
root.right.left = NodeSBT(16)
root.right.right = NodeSBT(25)
root.right.right.left = NodeSBT(22)
assert getChildrenKeys(root, 15) == (10, 20)
assert getChildrenKeysIterative(root, 15) == (10, 20)
print(getChildrenKeys(root, 15))

A = [15, 10, 20, 5, 12, 16, 25, None, None, None, None, None, None, 22]
assert getChildrenKeysViaArray(A, 15) == (10, 20)
assert getChildrenKeysViaArrayIterative(A, 15) == (10, 20)
print(getChildrenKeysViaArray(A, 15))
