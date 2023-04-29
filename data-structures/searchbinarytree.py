#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:46:19 2023

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
    if node.key < key:
        return search(node.right, key)
    else:
        return search(node.left, key)

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


root = insert(None, 8)
insert(root, 4)
insert(root, 12)
insert(root, 2)
insert(root, 6)
insert(root, 10)
insert(root, 14)
insert(root, 9)
print(search(root, 9))
print(search(root, 1))
