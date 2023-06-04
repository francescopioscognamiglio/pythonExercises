#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:04:55 2023

@author: scognamigliofrancescopio@gmail.com
"""

def elementWithMoreOccurrences(A):
    C = [0]*10*len(A)
    maxOccurrences = 0
    for x in A:
        C[x] += 1
        if maxOccurrences < C[x]: maxOccurrences = C[x]
    i = 0
    while i < len(C) and C[i] != maxOccurrences: i += 1
    return i


A = [2, 6, 8, 5, 2, 3, 6, 8, 9, 5, 8, 1, 2]
assert elementWithMoreOccurrences(A) == 2
print(elementWithMoreOccurrences(A))
