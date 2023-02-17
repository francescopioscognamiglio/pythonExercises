#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:58:18 2023

@author: scognamigliofrancescopio@gmail.com
"""

import math

def binarySearchMod(A,x):
    n = len(A)
    i,j = 0,n-1
    m = math.floor((i+j)/2)
    while A[m] != x: # array A with distinct values
        if A[m] > x:
            j=m-1 # search into the n/2 left part of the array
        else:
            i = m+1 # search into the n/2 right part of the array
        if i > j:
            break
        m = math.floor((i+j)/2)
    return m

def countRangeValues(A,a,b):
    posa = binarySearchMod(A, a)
    if A[posa] < a: posa += 1 # check if consider the next element (because we are in the middle)
    posb = binarySearchMod(A, b)
    if A[posb] > b: posb -= 1 # check if consider the previous element (because we are in the middle)
    return posb - posa + 1

print(countRangeValues([1,3,7,10,20,32], 0, 59)) #6
print(countRangeValues([1,3,7,10,20,32], 3, 59)) #5
print(countRangeValues([1,3,7,10,20,32], 4, 31)) #3
print(countRangeValues([1,3,7,10,20,32], 0, 20)) #5
print(countRangeValues([1,3,7,10,20,32], 0, 19)) #4
print(countRangeValues([1,3,7,10,20,32], 0, 1)) #1