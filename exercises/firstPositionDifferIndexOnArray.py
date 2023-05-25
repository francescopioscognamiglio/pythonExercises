#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:54:30 2023

@author: scognamigliofrancescopio@gmail.com
"""

def firstPositionDifferIndex(A):
    if A[0] < 0: return 0
    i, j = 0, len(A)-1
    p = -1
    while i <= j:
        m = (i+j)//2
        if A[m] == m:
            i = m+1
        else:
            p = m
            j = m-1
    return p

A = [0, 1, 2, 3, 4]
assert firstPositionDifferIndex(A) ==  -1
print(firstPositionDifferIndex(A))
A = [0, 5, 6, 20, 30]
assert firstPositionDifferIndex(A) ==  1
print(firstPositionDifferIndex(A))
A = [-3, 1, 2, 3, 6]
assert firstPositionDifferIndex(A) ==  0
print(firstPositionDifferIndex(A))
