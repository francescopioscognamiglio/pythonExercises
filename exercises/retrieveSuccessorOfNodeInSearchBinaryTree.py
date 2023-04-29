#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:13:55 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def search(node, key):
    if node == None: return None
    if node.key == key: return node
    elif node.key > key:
        return search(node.left, key)
    else:
        return search(node.right, key)

def retrieveMin(node):
    if node.left == None: return node
    return retrieveMin(node.left)

def getSuccessor(node, key):
    n = search(node, key)
    if n == None or n.right == None: return None
    return retrieveMin(n.right)


root = NodeSBT(5)
root.left = NodeSBT(3)
root.left.right = NodeSBT(4)
root.left.left = NodeSBT(2)
root.right = NodeSBT(100)
root.right.left = NodeSBT(90)
root.right.right = NodeSBT(110)
print(getSuccessor(root, 5).key)
print(getSuccessor(root, 3).key)
