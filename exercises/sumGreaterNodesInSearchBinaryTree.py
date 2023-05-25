#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:10:34 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def sumGreaterNodes(node, x = 0):
    if node == None: return 0
    if node.left == None and node.right == None:
        val = node.key
        node.key = x
        return val
    valparent = node.key
    valright = sumGreaterNodes(node.right, x)
    valleft = sumGreaterNodes(node.left, x + valparent + valright)
    node.key = valright + x
    return valparent + valright + valleft

def printTree(node, h = 0):
    if node == None: return
    print(h*'-', node.key)
    printTree(node.left, h+1)
    printTree(node.right, h+1)


root = NodeSBT(10)
root.left = NodeSBT(7)
root.left.left = NodeSBT(3)
root.left.right = NodeSBT(9)
root.right = NodeSBT(15)
root.right.left = NodeSBT(12)
root.right.right = NodeSBT(20)
root.right.left.right = NodeSBT(14)
printTree(root)
sumGreaterNodes(root)
print()
printTree(root)
