#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 16:35:03 2023

Given an ordered array and an input k
Retrieve the number of pairs that their sum gets k.
The complexity must be O(n).

@author: scognamigliofrancescopio@gmail.com
"""

def countPairsGetK(A, k):
    count = 0
    i, j = 0, len(A)-1
    while i < j:
        if A[i] + A[j] > k:
            j -= 1
        elif A[i] + A[j] < k:
            i += 1
        elif A[i] + A[j] == k:
            # count the duplicate values
            countdi, countdj = 1, 1
            while i+1 < j and A[i] == A[i+1]:
                countdi += 1
                i += 1
            while j-1 > i and A[j] == A[j-1]:
                countdj += 1
                j -= 1
            if A[i] == A[j]:
                count += (countdi+countdj)*(countdi+countdj-1)//2
            else:
                count += countdi * countdj
            i += 1
            j -= 1
    return count


t1 = countPairsGetK([1, 2, 5, 6, 6, 7], 12)
t2 = countPairsGetK([0, 4, 4, 7, 8], 12)
t3 = countPairsGetK([0, 3, 6, 9, 12], 15)
t4 = countPairsGetK([2, 2, 2, 2], 4)
t5 = countPairsGetK([1, 2, 2, 3, 4, 5, 5, 5, 8, 9, 9], 7)
t6 = countPairsGetK([1, 5, 5, 5, 9], 10)
assert t1 == 2
print(t1)
assert t2 == 2
print(t2)
assert t3 == 2
print(t3)
assert t4 == 6
print(t4)
assert t5 == 7
print(t5)
assert t6 == 4
print(t6)
