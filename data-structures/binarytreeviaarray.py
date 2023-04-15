#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 19:40:21 2023

The old way to build a binary tree is using an array, without the pointers.
Given a node i:
    - the left child is in 2*i+1
    - the right child is in 2*i+2

Example:
Given the following binary tree: [1, 2, 3, 2, 5, 6, 2, 3]
The children of the root (position 0 with value 1) are in 2*0+1=1 and 2*0+2=2 positions
The children of the node at position 1 (with value 2) are in 2*1+1=3 and 2*1+2=4

@author: scognamigliofrancescopio@gmail.com
"""

def printChildren(tree, i):
    leftChild = i*2+1
    rightChild = i*2+2
    if leftChild < len(tree): print(tree[leftChild])
    if rightChild < len(tree): print(tree[rightChild])

def printParent(tree, i):
    parent = (i-1)//2
    if parent >= 0 and parent < len(tree): print(tree[parent])

def printTree(tree, i = 0, h = 0):
    if i >= len(tree): return
    print(h*'|', tree[i])
    printTree(tree, i*2+1, h+1)
    printTree(tree, i*2+2, h+1)


tree = [1, 2, 3, 2, 5, 6, 2, 3]
printTree(tree)
print()
printChildren(tree, 0)
printChildren(tree, 1)
printChildren(tree, 2)
printChildren(tree, 100)
print()
printParent(tree, 0)
printParent(tree, 1)
printParent(tree, 2)
printParent(tree, 3)
printParent(tree, 4)
printParent(tree, 5)
printParent(tree, 30)
