#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:53:40 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Node:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def findMinUsingPointers(node):
    if node == None: return None
    if node.left == None and node.right == None:
        return node
    left = findMinUsingPointers(node.left)
    right = findMinUsingPointers(node.right)
    if left == None: return right
    if right == None: return left
    if left.key <= right.key: return left
    return right

def findMinUsingArray(A):
    i = len(A)//2
    m = A[i]
    i += 1
    while i < len(A):
        m = min(m, A[i])
        i += 1
    return m


root = Node(18)
root.left = Node(16)
root.left.left = Node(12)
root.left.left.left = Node(8)
root.left.left.right = Node(4)
root.left.right = Node(15)
root.left.right.left = Node(14)
root.left.right.right = Node(11)
root.right = Node(17)
root.right.left = Node(10)
root.right.left.left = Node(3)
root.right.right = Node(1)
assert findMinUsingPointers(root).key == 1
print(findMinUsingPointers(root).key)

A = [18, 16, 17, 12, 15, 10, 1, 8, 4, 14, 11, 3]
assert findMinUsingArray(A) == 1
print(findMinUsingArray(A))
