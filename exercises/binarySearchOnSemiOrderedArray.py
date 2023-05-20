#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 10:31:54 2023

@author: scognamigliofrancescopio@gmail.com
"""

def binarySearchMod(A, i, j):
    if i == j: return A[i]
    m = (i+j)//2
    if m+1 < len(A) and A[i] < A[m+1]: return binarySearchMod(A, m+1, j)
    elif m-1 >= 0 and A[i] < A[m-1]: return binarySearchMod(A, i, m-1)
    else: return A[m]


A = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]
print(binarySearchMod(A, 0, len(A)))
