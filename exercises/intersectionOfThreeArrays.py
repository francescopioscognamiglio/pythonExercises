#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 12:22:02 2023

@author: scognamigliofrancescopio@gmail.com
"""

def intersection3Arrays(A, B, C):
    i = j = k = 0
    while i < len(A) and j < len(B) and k < len(C):
        if A[i] == B[j] and B[j] == C[k]:
            print(A[i])
            i += 1
            j += 1
            k += 1
            continue
        if A[i] < B[j] or A[i] < C[k]:
            i += 1
        elif B[j] < A[i] or B[j] < C[k]:
            j += 1
        elif C[k] < A[i] or C[k] < B[j]:
            k += 1

def intersection3ArraysNew(A, B, C):
    a = b = c = 0
    while a < len(A) and b < len(B) and c < len(C):
        if A[a] == B[b] and B[b] == C[c]:
            print(A[a])
        m = min(A[a], B[b], C[c])
        if m == A[a]: a += 1
        if m == B[b]: b += 1
        if m == C[c]: c += 1


A = [1, 2, 3, 4, 5, 6]
B = [1, 4, 5, 6, 8, 9]
C = [2, 4, 6, 7, 8, 9]
intersection3Arrays(A, B, C)
intersection3ArraysNew(A, B, C)
