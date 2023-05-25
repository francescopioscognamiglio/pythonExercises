#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 19:23:26 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

check = True
def checkSBT(node, left = False):
    global check
    if node == None: return None
    if node.left == None and node.right == None: return node.key
    maxl = checkSBT(node.left, True)
    minr = checkSBT(node.right, False)
    if (maxl and minr) and (minr <= maxl or maxl >= node.key or minr <= node.key):
        check = False
    if left: return minr
    return maxl


root = NodeSBT(10)
root.left = NodeSBT(7)
root.left.left = NodeSBT(3)
root.left.right = NodeSBT(9)
root.right = NodeSBT(15)
root.right.left = NodeSBT(12)
root.right.left.right = NodeSBT(14)
root.right.right = NodeSBT(20)
print(check)
checkSBT(root)
print(check)

root = NodeSBT(3)
root.left = NodeSBT(2)
root.left.left = NodeSBT(1)
root.left.right = NodeSBT(4)
root.right = NodeSBT(10)
root.right.left = NodeSBT(6)
root.right.left.right = NodeSBT(8)
root.right.right = NodeSBT(20)
print(check)
checkSBT(root)
print(check)
