#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:56:35 2023

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
    elif node.key > key: return search(node.left, key)
    else: return search(node.right, key)

def getParent(node, key):
    if node == None: return None
    if node.key == key: return None
    elif node.key > key:
        if node.left.key == key: return node
        return getParent(node.left, key)
    else:
        if node.right.key == key: return node
        return getParent(node.right, key)

def retrieveMax(node):
    if node == None: return None
    if node.right == None: return node
    return retrieveMax(node.right)

def remove(node, key):
    nodeToRemove = search(node, key)
    if nodeToRemove == None: return None
    parent = getParent(node, nodeToRemove.key)
    # remove a leaf
    if nodeToRemove.left == None and nodeToRemove.right == None:
        if parent:
            if parent.left and parent.left.key == nodeToRemove.key: parent.left = None
            else: parent.right = None
        else: return None # the tree is empty
    # remove a node with two children
    elif nodeToRemove.left != None and nodeToRemove.right != None:
        maximum = retrieveMax(nodeToRemove.left)
        # the maximum is a leaf
        if maximum.left == None and maximum.right == None:
            maximum.left = nodeToRemove.left
            maximum.right = nodeToRemove.right
            if parent:
                if parent.left and parent.left.key == nodeToRemove.key: parent.left = maximum
                else: parent.right = maximum
            else: return maximum # the maximum is the new root
        # the maximum has a left child (no right child because in this case it is not the real maximum)
        else:
            parentMaximum = getParent(node, maximum.key)
            if parentMaximum: parentMaximum.right = maximum.left
            maximum.left = nodeToRemove.left
            maximum.right = nodeToRemove.right
            if parent:
                if parent.left and parent.left.key == nodeToRemove.key: parent.left = maximum
                else: parent.right = maximum
            else: return maximum # the maximum is the new root
    # remove a node with only one child
    else:
        if parent:
            if parent.left and parent.left.key == nodeToRemove.key:
                if nodeToRemove.left != None: parent.left = nodeToRemove.left
                else: parent.left = nodeToRemove.right
            else:
                if nodeToRemove.left != None: parent.right = nodeToRemove.left
                else: parent.right = nodeToRemove.right
        else:
            if nodeToRemove.left != None: return nodeToRemove.left # the left node is the new root
            else: return nodeToRemove.right # the right node is the new root


root = NodeSBT(10)
root.left = NodeSBT(5)
root.left.left = NodeSBT(3)
root.left.right = NodeSBT(7)
root.right = NodeSBT(100)
root.right.left = NodeSBT(90)
root.right.right = NodeSBT(110)
print(getParent(root, 100).key)

print(root.right.right)
remove(root, 110)
print(root.right.right)

print(root.key)
root = remove(root, 10)
print(root.key)

print(root.left.key)
remove(root, 5)
print(root.left.key)
