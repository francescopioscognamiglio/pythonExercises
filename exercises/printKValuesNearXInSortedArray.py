#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 12:46:57 2023

@author: scognamigliofrancescopio@gmail.com
"""

def binarySearchNearest(A, x):
    i, j = 0, len(A)-1
    posx = -1
    while i <= j:
        m = (i+j)//2
        if A[m] == x:
            posx = m
            break
        sx = abs(A[m-1]-x)
        dx = abs(A[m]-x)
        if dx < sx:
            i = m+1
            posx = m
        else:
            j = m-2
            posx = m-1
    return posx

def printKValuesNearX(A, x, k):
    posx = binarySearchNearest(A, x)
    if A[posx] != x:
        print(A[posx])
        k -= 1
    i, j = 1, 1
    while k > 0 and posx-i >= 0 and posx+j < len(A):
        sx = abs(A[posx-i]-x)
        dx = abs(A[posx+j]-x)
        if dx < sx:
            print(A[posx+j])
            j += 1
        else:
            print(A[posx-i])
            i += 1
        k -= 1
    while k > 0 and posx-i >= 0:
        print(A[posx-i])
        i += 1
        k -= 1
    while k > 0 and posx+j < len(A):
        print(A[posx+j])
        j += 1
        k -=1


A = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
x, k = 35, 4
assert binarySearchNearest(A, x) == 4
printKValuesNearX(A, x, k)
print()
B = [12, 16, 22, 30, 36, 39, 42, 45, 48, 50, 53, 55, 56]
assert binarySearchNearest(B, x) == 4
printKValuesNearX(B, x, k)
print()
C = [12, 16, 22, 30, 34, 39, 42, 45, 48, 50, 53, 55, 56]
assert binarySearchNearest(C, x) == 4
printKValuesNearX(C, x, k)
print()
printKValuesNearX(A, x, len(A)-1)
