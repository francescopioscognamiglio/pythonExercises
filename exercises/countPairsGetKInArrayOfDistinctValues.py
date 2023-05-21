#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:39:41 2023

Given an ordered array with distinct values and an input k
Retrieve the number of pairs that their sum gets k.
The complexity must be O(n).

@author: scognamigliofrancescopio@gmail.com
"""

def countPairsGetK(A, k):
    count = 0
    i, j = 0, len(A)-1
    while i < j:
        if A[i] + A[j] == k:
            count += 1
            i += 1
        elif A[i] + A[j] < k:
            i += 1
        else:
            j -= 1
    return count


t1 = countPairsGetK([1, 2, 5, 6, 6, 7], 12)
t2 = countPairsGetK([0, 4, 4, 7, 8], 12)
t3 = countPairsGetK([0, 3, 6, 9, 12], 15)
assert t1 == 2
print(t1)
assert t2 == 2
print(t2)
assert t3 == 2
print(t3)
