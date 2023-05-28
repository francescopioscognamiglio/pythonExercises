#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 10:50:16 2023

@author: scognamigliofrancescopio@gmail.com
"""

def printUnion(A, B):
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            print(B[j])
            j += 1
        elif A[i] < B[j]:
            print(A[i])
            i += 1
        else:
            print(A[i])
            i += 1
            j += 1
    while i < len(A):
        print(A[i])
        i += 1
    while j < len(B):
        print(B[j])
        j += 1


A = [1, 3, 4, 6]
B = [2, 3, 4, 7]
print(A)
print(B)
printUnion(A, B)
