#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:29:21 2023

@author: scognamigliofrancescopio@gmail.com
"""

class SBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def maximumDistance(node):
    copy = node
    minimum = node.key
    while node != None:
        if node.key < minimum: minimum = node.key
        node = node.left
    node = copy
    maximum = node.key
    while node != None:
        if node.key > maximum: maximum = node.key
        node = node.right
    return maximum - minimum

root = SBT(100)
root.left = SBT(50)
root.left.left = SBT(25)
root.left.right = SBT(75)
root.right = SBT(150)
root.right.left = SBT(110)
root.right.right = SBT(200)
assert maximumDistance(root) == 175
print(maximumDistance(root))
