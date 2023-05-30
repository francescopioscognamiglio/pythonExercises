#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:20:42 2023

@author: scognamigliofrancescopio@gmail.com
"""

def fromParentToPosArray(C, P, A = [], i = None):
    j = 0
    children = []
    while j < len(P):
        if P[j] == i:
            A.append(C[j])
            children.append(j)
        j += 1
    if children == []: return A
    fromParentToPosArray(C, P, A, children[0])
    if len(children) == 1: return A
    fromParentToPosArray(C, P, A, children[1])
    return A

def printParentArray(C, P, i = None):
    j = 0
    children = []
    while j < len(P):
        if P[j] == i:
            print(C[j])
            children.append(j)
        j += 1
    if children == []: return
    printParentArray(C, P, children[0])
    if len(children) == 1: return
    printParentArray(C, P, children[1])


C1, P1 = [1, 3, 10, 4, 2], [None, 0, 0, 1, 1]
#printParentArray(C1, P1)
A1 = fromParentToPosArray(C1, P1, []) # we have to pass the empty array A
                                      # otherwise it will be created a new one
                                      # shared with *every* call to this method
print(A1)
assert A1 == [1, 3, 10, 4, 2]

print()
C2, P2 = [3, 10, 1, 4, 2], [2, 2, None, 0, 0]
#printParentArray(C2, P2)
A2 = fromParentToPosArray(C2, P2, []) # we have to pass the empty array A
                                      # otherwise it will be created a new one
                                      # shared with *every* call to this method
print(A2)
assert A2 == [1, 3, 10, 4, 2]
