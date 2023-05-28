#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 11:23:06 2023

@author: scognamigliofrancescopio@gmail.com
"""

def reorganizeNegativeAndPositive(A):
    i, j = 0, len(A)-1
    while i < j:
        if A[i] < 0: i += 1
        if A[j] > 0: j -= 1
        if i < j and A[i] > 0 and A[j] < 0:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1


A = [3, -1, 5, -2, 4]
print(A)
reorganizeNegativeAndPositive(A)
assert A == [-2, -1, 5, 3, 4]
print(A)
