#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:03:37 2023

@author: scognamigliofrancescopio@gmail.com
"""

def deleteBrother(A, i):
    if i <= 0: return
    isRightNode = (i-1)//2 == (i-2)//2
    p = (i-1)//2
    if isRightNode:
        removeTree(A, 2*p+1)
    else:
        removeTree(A, 2*p+2)

def removeTree(A, i):
    if i >= len(A): return
    removeTree(A, 2*i+1)
    removeTree(A, 2*i+2)
    A[i] = None


A = [10, 7, 12, 4, 8, 11, 15]
print(A)
deleteBrother(A, 2)
assert A == [10, None, 12, None, None, 11, 15]
print(A)
