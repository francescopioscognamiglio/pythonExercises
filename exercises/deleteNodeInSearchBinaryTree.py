#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 18:10:56 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def deleteNode(node, key):
    if not node: return
    if node.left and node.left.key == key:
        # remove left child
        if node.left.left and node.left.right:
            # left child has two children
            insertNode(node.left.right, node.left.left.key)
            node.left = node.left.right
        elif node.left.left or node.left.right:
            # left child has one child
            if node.left.left: node.left = node.left.left
            else: node.left = node.left.right
        else:
            # left child has no children
            node.left = None
        return
    elif node.right and node.right.key == key:
        # remove right child
        if node.right.left and node.right.right:
            # right child has two children
            insertNode(node.right.right, node.right.left.key)
            node.right = node.right.right
        elif node.right.left or node.right.right:
            # right child has one child
            if node.right.left: node.right = node.right.left
            else: node.right = node.right.right
        else:
            # right child has no children
            node.right = None
        return
    if key > node.key: deleteNode(node.right, key)
    deleteNode(node.left, key)

def insertNode(node, key):
    if not node: return
    if key > node.key:
        if node.right: insertNode(node.right, key)
        else: node.right = NodeSBT(key)
    else:
        if node.left: insertNode(node.left, key)
        else: node.left = NodeSBT(key)

def printTree(node, h = 0):
    if node == None: return
    print(h*'-', node.key)
    printTree(node.left, h+1)
    printTree(node.right, h+1)


root = NodeSBT(15)
root.left = NodeSBT(10)
root.left.left = NodeSBT(5)
root.left.right = NodeSBT(12)
root.right = NodeSBT(20)
root.right.left = NodeSBT(16)
root.right.right = NodeSBT(25)
root.right.right.left = NodeSBT(22)
printTree(root)
deleteNode(root, 20)
print()
printTree(root)
deleteNode(root, 16)
print()
printTree(root)
