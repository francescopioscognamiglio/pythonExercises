#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:41:03 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def height(node):
    if node == None: return -1
    return max(height(node.left), height(node.right)) + 1

def buildArrayFromBinaryTree(node, A, i = 0):
    if node == None: return
    A[i] = node.key
    buildArrayFromBinaryTree(node.left, A, 2*i+1)
    buildArrayFromBinaryTree(node.right, A, 2*i+2)
    return A

def printEachLevel(node):
    A = [None]*(pow(2, height(node)+1)-1) # 2^(h+1)-1
    A = buildArrayFromBinaryTree(node, A)
    for x in A: print(x)


root = NodeBT(10)
root.left = NodeBT(12)
root.left.left = NodeBT(3)
root.left.right = NodeBT(55)
root.right = NodeBT(6)
root.right.left = NodeBT(82)
root.right.left.left = NodeBT(44)
print(printEachLevel(root))
