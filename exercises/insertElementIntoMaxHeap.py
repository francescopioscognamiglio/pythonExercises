#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:32:11 2023

@author: scognamigliofrancescopio@gmail.com
"""

def fixLastElement(A):
    i = len(A)-1
    while i > 0:
        p = (i-1)//2
        if A[i] > A[p]:
            A[i], A[p] = A[p], A[i]
            i = p
        else: break

def insertIntoMaxHeap(A, k):
    A.append(k)
    fixLastElement(A)


A = [18, 16, 10, 12, 15, 3, 1, 8, 4, 14, 11]
insertIntoMaxHeap(A, 17)
print(A)
assert A == [18, 16, 17, 12, 15, 10, 1, 8, 4, 14, 11, 3]
B = [18, 16, 10, 12, 15, 3, 1, 8, 4, 14, 11]
insertIntoMaxHeap(B, 22)
print(B)
assert B == [22, 16, 18, 12, 15, 10, 1, 8, 4, 14, 11, 3]
