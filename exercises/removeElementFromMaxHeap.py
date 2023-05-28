#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 18:34:50 2023

@author: scognamigliofrancescopio@gmail.com
"""

def removeElementFromMaxHeap(A, i):
    if i == len(A)-1:
        A.pop()
        return
    A[i] = A.pop()
    while i < len(A):
        new = i
        l, r = 2*i+1, 2*i+2
        if l < len(A) and A[new] < A[l]: new = l
        if r < len(A) and A[new] < A[r]: new = r
        if new == i: return
        A[new], A[i] = A[i], A[new]
        i = new


A = [18, 16, 10, 12, 15, 3, 1, 8, 4, 14, 11]
removeElementFromMaxHeap(A, 0) # remove the root
print(A)
assert A == [16, 15, 10, 12, 14, 3, 1, 8, 4, 11]
B = [18, 16, 10, 12, 15, 3, 1, 8, 4, 14, 11]
removeElementFromMaxHeap(B, len(B)-1) # remove the last
print(B)
assert B == [18, 16, 10, 12, 15, 3, 1, 8, 4, 14]
C = [18, 16, 10, 12, 15, 3, 1, 8, 4, 14, 11]
removeElementFromMaxHeap(C, 4)
print(C)
assert C == [18, 16, 10, 12, 14, 3, 1, 8, 4, 11]
