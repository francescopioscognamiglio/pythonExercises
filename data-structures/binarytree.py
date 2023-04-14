#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:41:14 2023

@author: scognamigliofrancescopio@gmail.com
"""

import random

class NodeBT:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def createTree(n, m):
    """
    Creates a random tree.
    
    Parameters
    ----------
    n : number
        The number of nodes.
    m : number
        The range [1, m] used to generate the node key.
    Returns
    -------
    The root of the tree.
    """
    if n == 0: return None
    node = NodeBT(random.randint(1, m))
    x = random.randint(0, n-1)
    node.left = createTree(x, m) # x nodes in the left side
    node.right = createTree(n-1-x, m) # n-1-x nodes in the right side
    return node

def printTree(node):
    """
    Prints out the entire tree.
    
    Parameters
    ----------
    node : NodeBT
        The root of the tree.
    Returns
    -------
    None.
    """
    if node == None: return
    print(node.key)
    printTree(node.left)
    printTree(node.right)


# build manually
r = NodeBT(5)
r.left = NodeBT(3)
r.right = NodeBT(2)
r.left.left = NodeBT(8)
r.left.right = NodeBT(6)

# build dinamically
r = createTree(5, 100)
printTree(r)
