#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:17:09 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def getNumberOfValidNodes(node, sum = 0):
    if node == None: return 0
    count = 0
    if node.key == sum: count += 1
    sum += node.key
    return count + getNumberOfValidNodes(node.left, sum) + getNumberOfValidNodes(node.right, sum)


root = NodeBT(0)
root.left = NodeBT(2)
root.left.left = NodeBT(1)
root.left.right = NodeBT(7)
root.left.right.left = NodeBT(9)
root.right = NodeBT(5)
root.right.left = NodeBT(6)
root.right.right = NodeBT(-40)
root.right.right.left = NodeBT(-35)
assert getNumberOfValidNodes(root) == 3
print(getNumberOfValidNodes(root))
