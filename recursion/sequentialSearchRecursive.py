#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:01:48 2023

@author: scognamigliofrancescopio@gmail.com
"""

def sequentialSearchRecursive(A,x,i=0):
    n = len(A)
    
    if i == n: return None

    if x == A[i]: return i
    else: return sequentialSearchRecursive(A, x, i+1)

def sequentialSearchRecursiveWithotIndex(A,x):
    if A == []: return None
    if A[-1] == x: return len(A)-1 # check the last element A[-1]
    return sequentialSearchRecursiveWithotIndex(A[:-1], x) # A[:-1] means keep elements without the last one

print(sequentialSearchRecursive([2,1,3,8,7,4,2], 3))
print(sequentialSearchRecursive([2,1,3,8,7,4,2], 144))
print(sequentialSearchRecursiveWithotIndex([2,1,3,8,7,4,2], 3))
print(sequentialSearchRecursiveWithotIndex([2,1,3,8,7,4,2], 144))