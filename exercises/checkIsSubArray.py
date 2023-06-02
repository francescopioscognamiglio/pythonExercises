#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:07:12 2023

@author: scognamigliofrancescopio@gmail.com
"""

def isSubarray(A, B):
    i = 0
    while i < len(A) and A[i] != B[0]: i += 1
    if i == len(A): return 'No'
    j = 0
    while i < len(A) and j < len(B):
        if A[i] != B[j]: return 'No'
        i += 1
        j += 1
    return 'Sì'


A = [5, 9, 1, 3, 4, 8, 2]
B = [3, 4, 8]
assert isSubarray(A, B) == 'Sì'
print(isSubarray(A, B))
B = [3, 8, 2]
assert isSubarray(A, B) == 'No'
print(isSubarray(A, B))
B = [9, 6, 8]
assert isSubarray(A, B) == 'No'
print(isSubarray(A, B))
