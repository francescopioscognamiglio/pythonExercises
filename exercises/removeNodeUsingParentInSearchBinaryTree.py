#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:24:21 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

def search(node, key):
    if node == None: return None
    if node.key == key: return node
    elif node.key > key: return search(node.left, key)
    else: return search(node.right, key)

def retrieveMax(node):
    if node == None: return None
    if node.right == None: return node
    return retrieveMax(node.right)

def remove(node, key):
    nodeToRemove = search(node, key)
    if nodeToRemove == None: return None
    # remove a leaf
    if nodeToRemove.left == None and nodeToRemove.right == None:
        if nodeToRemove.parent:
            if nodeToRemove.parent.left and nodeToRemove.parent.left.key == nodeToRemove.key: nodeToRemove.parent.left = None
            else: nodeToRemove.parent.right = None
        else: return None # the tree is empty
    # remove a node with two children
    elif nodeToRemove.left != None and nodeToRemove.right != None:
        maximum = retrieveMax(nodeToRemove.left)
        # the maximum is a leaf
        if maximum.left == None and maximum.right == None:
            maximum.left = nodeToRemove.left
            maximum.right = nodeToRemove.right
            # update parent
            maximum.left.parent = maximum
            maximum.right.parent = maximum
            if nodeToRemove.parent:
                if nodeToRemove.parent.left and nodeToRemove.parent.left.key == nodeToRemove.key: nodeToRemove.parent.left = maximum
                else: nodeToRemove.parent.right = maximum
            else: return maximum # the maximum is the new root
        # the maximum has a left child (no right child because in this case it is not the real maximum)
        else:
            if maximum.parent: maximum.parent.right = maximum.left
            maximum.left = nodeToRemove.left
            maximum.right = nodeToRemove.right
            # update parent
            maximum.left.parent = maximum
            maximum.right.parent = maximum
            if nodeToRemove.parent:
                if nodeToRemove.parent.left and nodeToRemove.parent.left.key == nodeToRemove.key: nodeToRemove.parent.left = maximum
                else: nodeToRemove.parent.right = maximum
            else: return maximum # the maximum is the new root
    # remove a node with only one child
    else:
        if nodeToRemove.parent:
            if nodeToRemove.parent.left and nodeToRemove.parent.left.key == nodeToRemove.key:
                if nodeToRemove.left != None: nodeToRemove.parent.left = nodeToRemove.left
                else: nodeToRemove.parent.left = nodeToRemove.right
            else:
                if nodeToRemove.left != None: nodeToRemove.parent.right = nodeToRemove.left
                else: nodeToRemove.parent.right = nodeToRemove.right
        else:
            if nodeToRemove.left != None: return nodeToRemove.left # the left node is the new root
            else: return nodeToRemove.right # the right node is the new root


root = NodeSBT(10)
root.left = NodeSBT(5, root)
root.left.left = NodeSBT(3, root.left)
root.left.right = NodeSBT(7, root.left)
root.right = NodeSBT(100, root)
root.right.left = NodeSBT(90, root.right)
root.right.right = NodeSBT(110, root.right)

print(root.right.right)
remove(root, 110)
print(root.right.right)

print(root.key)
root = remove(root, 10)
print(root.key)

print(root.left.key)
remove(root, 5)
print(root.left.key)
