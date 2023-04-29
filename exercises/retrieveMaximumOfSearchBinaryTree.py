#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:13:45 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def insert(root, key):
    q = NodeSBT(key)
    if root == None: return q
    p = root
    while p: # p is not None
        if p.key > key and p.left:
            p = p.left
        elif p.key < key and p.right:
            p = p.right
        else: break

    # p points to the last element
    if p.key > key:
        p.left = q
    elif p.key < key:
        p.right = q
    return root

def retrieveMax(node):
    if node.right == None: return node
    return retrieveMax(node.right)


root = insert(None, 8)
insert(root, 4)
insert(root, 12)
insert(root, 2)
insert(root, 6)
insert(root, 10)
insert(root, 14)
insert(root, 9)
print(retrieveMax(root).key)
