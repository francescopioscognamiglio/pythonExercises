#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:21:37 2023

@author: scognamigliofrancescopio@gmail.com
"""

def countingSort(A):
    k = max(A) # retrieve the maximum value of the array
    C = [0] * (k+1) # create an array 
    for x in A:
        C[x] += 1

    p = 0
    for i in range(len(C)):
        for j in range(C[i]):
            A[p] = i
            p += 1


v1 = [1, 2, 2, 1, 3, 2, 1]
countingSort(v1)
print(v1)
assert v1 == [1, 1, 1, 2, 2, 2, 3]

v2 = [1, 1, 1, 1]
countingSort(v2)
print(v2)
assert v2 == [1, 1, 1, 1]
