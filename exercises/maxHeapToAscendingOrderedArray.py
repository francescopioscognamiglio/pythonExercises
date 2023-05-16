#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:55:34 2023

@author: scognamigliofrancescopio@gmail.com
"""

def extract(MH):
    maximum = MH[0]
    MH[0] = MH[-1]
    MH.pop()
    heapify(MH)
    return maximum

def heapify(MH, i = 0):
    c, l, r = i, i*2+1, i*2+2
    if l < len(MH) and MH[c] < MH[l]:
        c = l
    if r < len(MH) and MH[c] < MH[r]:
        c = r
    if c == i: return
    MH[c], MH[i] = MH[i], MH[c]
    heapify(MH, c)

def maxHeapToAscendingOrderedArray(MH):
    A = []
    while len(MH) > 0:
        A.append(extract(MH))
    B = []
    for i in range(len(A)-1, -1, -1):
        B.append(A[i])
    return B


print(maxHeapToAscendingOrderedArray([100, 80, 65, 40, 34, 55]))
