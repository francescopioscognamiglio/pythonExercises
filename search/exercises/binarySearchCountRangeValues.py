#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:49:45 2023

@author: scognamigliofrancescopio@gmail.com
"""

import math

def binarySearchMin(A,x):
    n = len(A)
    i = 0
    j = n-1
    posx = -1
    while i <= j:
        m = math.floor((i+j)/2)
        if A[m] >= x:
            posx = m
            j=m-1 # search into the n/2 left part of the array
        else: i = m+1 # search into the n/2 right part of the array
    return posx

def binarySearchMax(A,x):
    n = len(A)
    i = 0
    j = n-1
    posx = -1
    while i <= j:
        m = math.floor((i+j)/2)
        if A[m] > x: j=m-1 # search into the n/2 left part of the array
        else:
            posx = m
            i = m+1 # search into the n/2 right part of the array
    return posx

def countRangeValues(A,a,b):
    posa = binarySearchMin(A, a)
    posb = binarySearchMax(A, b)
    return posb - posa + 1

print(countRangeValues([1,3,7,10,20,32], 0, 59))
print(countRangeValues([1,3,7,10,20,32], 0, 1))