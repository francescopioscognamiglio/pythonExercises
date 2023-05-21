#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:17:16 2023

@author: scognamigliofrancescopio@gmail.com
"""

def getSubArray(A, s):
    sum = 0
    i = 0
    start = 0
    while i < len(A):
        sum += A[i]
        if sum == s: return start, i
        elif sum > s:
            start = i
            sum = A[i]
        i += 1
    return None


A = [1, 3, 5, 2, 9, 3, 3, 1, 6]
assert getSubArray(A, 7) == (2, 3)
print(getSubArray(A, 7))
assert getSubArray(A, 21) == None
print(getSubArray(A, 21))
