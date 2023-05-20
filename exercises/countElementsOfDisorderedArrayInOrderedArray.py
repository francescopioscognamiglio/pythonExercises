#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 18:28:54 2023

@author: scognamigliofrancescopio@gmail.com
"""

def binarySearch(B, x, i, j):
    if i > j: return False
    m = (i+j)//2
    if B[m] == x: return True
    if B[m] > x: return binarySearch(B, x, i, m-1)
    else: return binarySearch(B, x, m+1, j)

def countElementsOfAInB(A, B):
    counter = 0
    for x in A:
        if binarySearch(B, x, 0, len(B)-1) == False: counter += 1
    return counter


A = [8, 1, 2, 12, 10, 11, 20, 2]
B = [3, 3, 4, 8, 10, 10, 13, 20, 21, 22]
print(countElementsOfAInB(A, B))
