#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 11:32:27 2023

@author: scognamigliofrancescopio@gmail.com
"""

def rearrange(A):
    i, j = 0, len(A)-1
    while i < j:
        if A[i]%2 == 0: i += 1
        if A[j]%2 == 1: j -= 1
        if A[i]%2 == 1 and A[j]%2 == 0:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    i, j = 1, len(A)-2
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 2
        j -= 2

def rearrangeCompact(A):
    e, o = 0, 1 # even and odd
    while e < len(A) and o < len(A):
        if A[e]%2 == 0: e += 2
        if A[o]%2 == 1: o += 2
        if A[e]%2 == 1 and A[o]%2 == 0:
            A[e], A[o] = A[o], A[e]
            e += 2
            o += 2


A = [7, 3, 1, 8, 8, 2, 1, 4]
print(A)
rearrange(A)
assert A == [4, 1, 8, 1, 8, 3, 2, 7]
print(A)
print()
A = [7, 3, 1, 8, 8, 2, 1, 4]
print(A)
rearrangeCompact(A)
assert A == [8, 3, 2, 7, 8, 1, 4, 1]
print(A)
