#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:44:50 2023

@author: scognamigliofrancescopio@gmail.com
"""

def findSumOfSequentialThreeNumbersLessThan100(A):
    C = [False]*100
    for x in A:
        if x < 100: C[x] = True
    i = len(C)-1
    while i >= 0:
        if i-2 >= 0 and C[i] and C[i-1] and C[i-2]:
            if i+(i-1)+(i-2) < 100: return i-1
        i -= 1
    return -1


A = [101, 5, 9, 31, 33, 10, 100, 4, 8, 32, 500, 11, 99]
assert findSumOfSequentialThreeNumbersLessThan100(A) == 32
print(findSumOfSequentialThreeNumbersLessThan100(A))

A = [101, 5, 9, 31, 33, 10, 100, 4, 8, 32, 500, 34, 11, 99]
assert findSumOfSequentialThreeNumbersLessThan100(A) == 33
print(findSumOfSequentialThreeNumbersLessThan100(A))
