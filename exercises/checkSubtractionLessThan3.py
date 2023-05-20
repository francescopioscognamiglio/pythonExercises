#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:58:24 2023

@author: scognamigliofrancescopio@gmail.com
"""

def checkSubtractionLessThan3(A, B):
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if abs(A[i] - B[j]) <= 3: return True
        if A[i] > B[j]: j += 1
        else: i += 1
    return False


A = [1, 2, 20, 30]
B = [6, 7, 10]
print(checkSubtractionLessThan3(A, B))
A = [1, 2, 9, 10, 12]
B = [6, 14, 16, 20]
print(checkSubtractionLessThan3(A, B))
