#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:01:01 2023

@author: scognamigliofrancescopio@gmail.com
"""

def sortKOrderedArray(A, k):
    i = 0
    while i < len(A):
        ki = k
        while ki > 0:
            if ki+i < len(A) and A[ki+i] < A[i]:
                A[i], A[ki+i] = A[ki+i], A[i]
                break
            ki //= 2
        i += 1


A = [10, 9, 8, 7, 4, 70, 60, 50]
sortKOrderedArray(A, 4)
print(A)
assert A == [4, 7, 8, 9, 10, 50, 60, 70]
B = [6, 5, 3, 2, 8, 10, 9]
sortKOrderedArray(B, 3)
print(B)
assert B == [2, 3, 5, 6, 8, 9, 10]
