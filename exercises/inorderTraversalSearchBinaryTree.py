#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:32:55 2023

@author: scognamigliofrancescopio@gmail.com
"""

class NodeSBT:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def inorderTraversal(ABR, C = []):
    if ABR == None: return
    inorderTraversal(ABR.left, C)
    C.append(ABR.key)
    inorderTraversal(ABR.right, C)
    return C


root = NodeSBT(50)
root.left = NodeSBT(10)
root.left.left = NodeSBT(5)
root.left.right = NodeSBT(15)
root.right = NodeSBT(75)
root.right.left = NodeSBT(60)
root.right.right = NodeSBT(80)
print(inorderTraversal(root))
