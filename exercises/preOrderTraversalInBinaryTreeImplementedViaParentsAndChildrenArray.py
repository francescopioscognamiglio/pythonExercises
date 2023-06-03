#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:39:41 2023

@author: scognamigliofrancescopio@gmail.com
"""

def findRoot(A, P):
    i = 0
    while i < len(P):
        if P[i] == None: return i
        i += 1
    return None

def findChildren(A, P, i):
    C = [None, None]
    j, k = 0, 0
    while j < len(P):
        if P[j] == i:
            C[k] = j
            k += 1
        j += 1
    return C[0], C[1]

def preOrderTraversal(A, P):
    C = []
    i = 0
    while i < len(A):
        li, ri = findChildren(A, P, i)
        C.append([li, ri])
        i += 1
    ri = findRoot(A, P)
    preOrderPrint(A, P, C, ri)

def preOrderPrint(A, P, C, i, h = 0):
    if i == None: return
    print(h*'-', A[i])
    li, ri = C[i]
    preOrderPrint(A, P, C, li, h+1)
    preOrderPrint(A, P, C, ri, h+1)


A = [10, 5, 3]
P = [None, 0, 0]
preOrderTraversal(A, P)

A = [7, 2, 10, 5, 4, 5, 3]
P = [2, 2, None, 0, 1, 1, 0]
print()
preOrderTraversal(A, P)
