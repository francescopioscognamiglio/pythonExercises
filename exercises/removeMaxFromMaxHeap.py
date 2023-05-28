#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 18:12:42 2023

@author: scognamigliofrancescopio@gmail.com
"""

def removeMaxFromMaxHeap(A):
    m = A[0]
    A[0] = A.pop()
    i = 0
    while i < len(A):
        new = i
        l, r = 2*i+1, 2*i+2
        if l < len(A) and A[new] < A[l]: new = l
        if r < len(A) and A[new] < A[r]: new = r
        if new == i: break
        A[new], A[i] = A[i], A[new]
        i = new
    return m


A = [18, 16, 10, 12, 15, 3, 1, 8, 4, 14, 11]
print(removeMaxFromMaxHeap(A))
print(A)
assert A == [16, 15, 10, 12, 14, 3, 1, 8, 4, 11]
B = [22, 16, 10, 12, 15, 3, 1, 8, 4, 14, 13]
print(removeMaxFromMaxHeap(B))
print(B)
assert B == [16, 15, 10, 12, 14, 3, 1, 8, 4, 13]
C = [22, 16, 10, 12, 15, 3, 1, 8, 4, 14, 15]
print(removeMaxFromMaxHeap(C))
print(C)
assert C == [16, 15, 10, 12, 15, 3, 1, 8, 4, 14]
