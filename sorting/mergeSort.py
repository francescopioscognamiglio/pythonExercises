#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:56:37 2023

@author: scognamigliofrancescopio@gmail.com
"""

def mergeSort(A, start, end):
    if start == end: return
    m = (start+end)//2
    mergeSort(A, start, m)
    mergeSort(A, m+1, end)
    merge(A, start, m, end)

def merge(A, start, m, end):
    i,j = start,m+1
    B = []
    while i <= m and j <= end:
        if A[i] > A[j]:
            B.append(A[j]); j += 1
        else:
            B.append(A[i]); i += 1
    # in case of missing elements from the first part of the array
    while i <= m:
        B.append(A[i]); i += 1
    # in case of missing elements from the second part of the array
    while j <= end:
        B.append(A[j]); j += 1

    for k in range(len(B)):
        A[start+k] = B[k]


A = [4, 3, 6, 2, 3]
mergeSort(A, 0, len(A)-1)
print(A)
