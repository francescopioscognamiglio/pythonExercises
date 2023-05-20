#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:14:34 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def numberOfBalancedNodesOld(node):
    if node == None: return 0
    left = numberOfBalancedNodesOld(node.left)
    right = numberOfBalancedNodesOld(node.right)
    number = left + right
    if left == right: return number + 1
    return number

def numberOfBalancedNodes(node):
    if node == None: return 0, 0
    balancedLeft, totalLeft = numberOfBalancedNodes(node.left)
    balancedRight, totalRight = numberOfBalancedNodes(node.right)
    balanced = balancedLeft + balancedRight
    if totalLeft == totalRight: balanced += 1
    return balanced, totalLeft + totalRight + 1


root = NodeBT(10)
print(numberOfBalancedNodesOld(root), '==', numberOfBalancedNodes(root)[0])
root.left = NodeBT(14)
print(numberOfBalancedNodesOld(root), '==', numberOfBalancedNodes(root)[0])
root.right = NodeBT(3)
print(numberOfBalancedNodesOld(root), '==', numberOfBalancedNodes(root)[0])
root.left.left = NodeBT(4)
root.left.right = NodeBT(44)
print(numberOfBalancedNodesOld(root), '==', numberOfBalancedNodes(root)[0])
root.left.left.left = NodeBT(11)
root.right.right = NodeBT(45)
print(numberOfBalancedNodesOld(root), '==', numberOfBalancedNodes(root)[0])
