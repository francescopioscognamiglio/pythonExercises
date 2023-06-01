#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:57:34 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Node:
    def __init__(self, key, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

def deleteBrother(node):
    if node == None or node.parent == None: return
    if node.parent.left and node.parent.right:
        isLeftNode = node.parent.left == node
        if isLeftNode:
            node.parent.right = None
        else:
            node.parent.left = None

def printTree(node, h = 0):
    if node == None: return
    print(h*'-', node.key)
    printTree(node.left, h+1)
    printTree(node.right, h+1)


root = Node(10)
root.left = Node(7, root)
root.left.left = Node(4, root.left)
root.left.right = Node(8, root.left)
root.right = Node(12, root)
root.right.left = Node(11, root.right)
root.right.right = Node(15, root.right)
printTree(root)
deleteBrother(root.right)
print()
printTree(root)
