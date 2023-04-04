#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:26:29 2023

@author: scognamigliofrancescopio@gmail.com
"""

def merge(A, B):
    C = []
    i,j = 0,0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i]); i += 1
        else:
            C.append(B[j]); j += 1
    # add missing elements from the first array
    while i < len(A):
        C.append(A[i]); i += 1
    # add missing elements from the second array
    while j < len(A):
        C.append(B[j]); j += 1
    return C

A = [3, 4, 6, 8]
B = [1, 2, 5, 10]
print(merge(A, B))
