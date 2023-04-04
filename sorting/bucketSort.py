#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:22:30 2023

@author: scognamigliofrancescopio@gmail.com
"""

def bucketSort(A, k):
    k = max(A) # retrieve the maximum value of the array
    B = [[] for _ in range(k)] # create an array of k empty arrays
    for x in A:
        B[x*(k-1)//k].append(x)

    for i in range(k):
        B[i].sort() # this sort uses the Quick Sort so the complexity is nlogn

    R = []
    for i in range(k):
        R.extend(B[i]) # we copy the element of B[i] array into the R array

    return R


v1 = [1, 5, 2, 3, 7, 3, 4]
v1Ordered = bucketSort(v1, 5)
print(v1Ordered)
assert v1Ordered == [1, 2, 3, 3, 4, 5, 7]
