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

def inOrderTraversal(node, A):
    if node == None: return
    if node.left == None and node.right == None:
        A.append(node.key)
        return
    inOrderTraversal(node.left, A)
    A.append(node.key)
    inOrderTraversal(node.right, A)

def checkSBTViaSorting(node):
    A = []
    inOrderTraversal(node, A)
    i = 0
    while i < len(A):
        if i+1 < len(A) and A[i] >= A[i+1]:
            return False
        i += 1
    return True


root = NodeSBT(10)
root.left = NodeSBT(7)
root.left.left = NodeSBT(3)
root.left.right = NodeSBT(9)
root.right = NodeSBT(15)
root.right.left = NodeSBT(12)
root.right.left.right = NodeSBT(14)
root.right.right = NodeSBT(20)
checkSBT(root)
assert check == True
assert checkSBTViaSorting(root) == True
print(check)
print(checkSBTViaSorting(root))

print()

root = NodeSBT(3)
root.left = NodeSBT(2)
root.left.left = NodeSBT(1)
root.left.right = NodeSBT(4)
root.right = NodeSBT(10)
root.right.left = NodeSBT(6)
root.right.left.right = NodeSBT(8)
root.right.right = NodeSBT(20)
checkSBT(root)
assert check == False
assert checkSBTViaSorting(root) == False
print(check)
print(checkSBTViaSorting(root))
