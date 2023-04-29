#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:46:34 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def countNodesOnLevel(node, k, currentLevel = 0):
    if node == None: return 0
    if currentLevel == k: return 1
    return countNodesOnLevel(node.left, k, currentLevel+1) + countNodesOnLevel(node.right, k, currentLevel+1)

def countNodesOnLevelImproved(node, k):
    if node == None: return 0
    if k == 0: return 1
    return countNodesOnLevelImproved(node.left, k-1) + countNodesOnLevelImproved(node.right, k-1)


root = NodeBT(5)
root.left = NodeBT(5)
root.left.right = NodeBT(5)
root.left.right.left = NodeBT(5)
root.left.right.left.left = NodeBT(5)
root.left.right.right = NodeBT(5)
root.right = NodeBT(5)
root.right.left = NodeBT(5)
root.right.right = NodeBT(5)
root.right.right.left = NodeBT(5)
root.right.right.left.right = NodeBT(5)
root.right.right.right = NodeBT(5)
print(countNodesOnLevel(root, 3))
print(countNodesOnLevel(root, 4))
print(countNodesOnLevel(root, 5))
print(countNodesOnLevelImproved(root, 3))
print(countNodesOnLevelImproved(root, 4))
print(countNodesOnLevelImproved(root, 5))
