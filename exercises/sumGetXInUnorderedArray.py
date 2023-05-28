#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 10:26:33 2023

@author: scognamigliofrancescopio@gmail.com
"""

def sumGetX(A, x):
    #mergeSort(A, 0, len(A)-1)
    A.sort()
    i, j = 0, len(A)-1
    while i < j:
        if A[i]+A[j] == x: return True
        if A[i]+A[j] > x: j -= 1
        if A[i]+A[j] < x: i += 1
    return False


A = [0, -1, 2, -3, 1]
assert sumGetX(A, -2) == True
print(sumGetX(A, -2))
assert sumGetX(A, 20) == False
print(sumGetX(A, 20))
