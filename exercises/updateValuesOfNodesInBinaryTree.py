#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:56:25 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def updateValues(node):
    if node == None: return
    if node.left and node.right:
        node.val += node.left.val + node.right.val
    elif node.left:
        node.val += node.left.val
    elif node.right:
        node.val += node.right.val
    updateValues(node.left)
    updateValues(node.right)

def printTree(node, h = 0):
    if node == None: return
    print(h*'-', node.val)
    printTree(node.left, h+1)
    printTree(node.right, h+1)


root = NodeBT(5)
root.left = NodeBT(6)
root.right = NodeBT(2)
root.right.left = NodeBT(4)
root.right.right = NodeBT(3)
root.right.left.left = NodeBT(5)
root.right.right.left = NodeBT(1)
root.right.right.right = NodeBT(4)
printTree(root)
updateValues(root)
printTree(root)
