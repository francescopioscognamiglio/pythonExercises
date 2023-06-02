#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:25:08 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def sortArray(A):
    if len(A) == 0: return
    root = NodeSBT(A[0])
    A
    i = 1
    while i < len(A):
        insertNode(root, A[i])
        i += 1
    A.clear()
    fromSBTToArray(A, root)
    return A

def fromSBTToArray(A, node):
    if node == None: return
    fromSBTToArray(A, node.left)
    A.append(node.key)
    fromSBTToArray(A, node.right)

def insertNode(node, key):
    if node == None: return
    if node.key < key:
        # the new node will go into the right subtree
        if not node.right: node.right = NodeSBT(key)
        else: insertNode(node.right, key)
    else:
        # the new node will go into the left subtree
        if not node.left: node.left = NodeSBT(key)
        else: insertNode(node.left, key)


A = [10, 3, 2, 5, 6, 7, 4]
assert sortArray(A) == [2, 3, 4, 5, 6, 7, 10]
print(sortArray(A))
