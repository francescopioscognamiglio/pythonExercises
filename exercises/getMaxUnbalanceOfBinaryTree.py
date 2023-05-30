#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 19:16:35 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Node:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

currentMax = 0
def maxSbilanciamento(node):
    global currentMax
    if node == None: return 0
    if node.left == None and node.right == None: return 1
    countLeft = maxSbilanciamento(node.left)
    countRight = maxSbilanciamento(node.right)
    sbilanciamento = abs(countLeft - countRight)
    currentMax = max(currentMax, sbilanciamento)
    return countLeft + countRight + 1


root = Node(1)
root.left = Node(1)
root.left.left = Node(1)
root.left.right = Node(1)
root.left.right.left = Node(1)
root.left.right.left.left = Node(1)
root.left.right.left.right = Node(1)
root.left.right.right = Node(1)
root.right = Node(1)
root.right.left = Node(1)
root.right.right = Node(1)
root.right.right.right = Node(1)
maxSbilanciamento(root)
print(currentMax)
