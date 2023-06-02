#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:23:57 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Node:
    def __init__(self, val, sx = None, dx = None):
        self.val = val
        self.sx = sx
        self.dx = dx

areNodeEqual = True
def checkNodes(node):
    global areNodeEqual
    if node == None: return areNodeEqual
    if node.sx and node.val != node.sx.val: areNodeEqual = False
    if node.dx and node.val != node.dx.val: areNodeEqual = False
    checkNodes(node.sx)
    checkNodes(node.dx)
    return areNodeEqual

def checkNodes2(node):
    if node == None: return True
    if node.sx and node.val != node.sx.val: return False
    if node.dx and node.val != node.dx.val: return False
    return checkNodes(node.sx) and checkNodes(node.dx)


root = Node(10)
root.sx = Node(10)
root.sx.sx = Node(10)
root.sx.sx.sx = Node(10)
root.sx.sx.sx.sx = Node(10)
root.sx.dx = Node(10)
root.sx.dx.sx = Node(10)
root.sx.dx.dx = Node(10)
root.dx = Node(10)
root.dx.sx = Node(10)
root.dx.dx = Node(10)
root.dx.dx.sx = Node(10)
root.dx.dx.dx = Node(10)
root.dx.dx.dx.sx = Node(10)
root.dx.dx.dx.dx = Node(10)
assert checkNodes(root) == True
print(checkNodes(root))
assert checkNodes2(root) == True
print(checkNodes2(root))

root.dx.dx.dx.dx.sx = Node(15)
assert checkNodes(root) == False
print(checkNodes(root))
assert checkNodes2(root) == False
print(checkNodes2(root))
