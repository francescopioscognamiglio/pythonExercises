#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:02:13 2023

@author: scognamigliofrancescopio@gmail.com
"""

def symmetricDifference(A, B, n, m):
    C = []
    i, j = 0, 0
    while i < n and j < m:
        if A[i] == B[j]:
            i += 1
            j += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
    while i < n:
        C.append(A[i])
        i += 1
    while j < m:
        C.append(B[j])
        j += 1
    return C


A = [5, 28, 100, 120]
B = [34, 100, 150]
print(symmetricDifference(A, B, len(A), len(B)))
