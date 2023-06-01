#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:02:17 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Node:
    def __init__(self, key, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

def deleteNode(node):
    if node == None: return
    newnode = node
    if node.parent and node.parent.left and node.parent.right:
        # the parent has two children
        isNodeLeft = node.parent.left == node
        if (node.left == None and node.right) or (node.left and node.right == None):
            # the node has only one child
            isChildLeft = node.left != None
            if isChildLeft:
                if node.left.right and node.left.left:
                    # the child has two children - remove the node
                    newnode = node.left
                    node.left.parent = node.parent
                    if isNodeLeft: node.parent.left = node.left
                    else: node.parent.right = node.left
            else:
                if node.right.right and node.right.left:
                    # the child has two children - remove the node
                    newnode = node.right
                    node.right.parent = node.parent
                    if isNodeLeft: node.parent.left = node.right
                    else: node.parent.right = node.right
    deleteNode(newnode.left)
    deleteNode(newnode.right)

def printTree(node, h = 0):
    if node == None: return
    print(h*'-', node.key)
    printTree(node.left, h+1)
    printTree(node.right, h+1)


root = Node('a')
root.left = Node('b', root)
root.left.left = Node('d', root.left)
root.left.right = Node('e', root.left)
root.left.right.left = Node('h', root.left.right)
root.left.right.left.left = Node('m', root.left.right.left)
root.left.right.left.right = Node('n', root.left.right.left)
root.left.right.left.right.right = Node('r', root.left.right.left.right)
root.right = Node('c', root)
root.right.left = Node('f', root.right)
root.right.left.right = Node('i', root.right.left)
root.right.left.right.left = Node('o', root.right.left.right)
root.right.left.right.right = Node('p', root.right.left.right)
root.right.right = Node('g', root.right)
root.right.right.left = Node('l', root.right.right)
root.right.right.left.right = Node('q', root.right.right.left)
root.right.right.left.right.left = Node('s', root.right.right.left.right)
root.right.right.left.right.right = Node('t', root.right.right.left.right)
printTree(root)
deleteNode(root)
print()
printTree(root)
