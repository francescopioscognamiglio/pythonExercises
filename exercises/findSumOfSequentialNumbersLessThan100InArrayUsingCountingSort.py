#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:59:55 2023

@author: scognamigliofrancescopio@gmail.com
"""

def findSumOfSequentialNumbersLessThan100(A):
    C = [False]*100
    for x in A:
        if x < 100: C[x] = True
    i = len(C)-1
    count, sum = 0, 0
    while i >= 0:
        if C[i] == False or sum+i >= 100:
            # stop the counter when we found a missing element or the new element is too big
            if count >= 3: return i + count//2 + 1
            else: count, sum = 0, 0 # no numbers found, re-init the variables
        elif C[i] == True and sum+i < 100:
            count += 1
            sum += i
        i -= 1
    return -1


A = [101, 5, 9, 31, 33, 10, 100, 4, 8, 32, 500, 11, 99]
assert findSumOfSequentialNumbersLessThan100(A) == 32
print(findSumOfSequentialNumbersLessThan100(A))

A = [101, 5, 9, 31, 33, 10, 100, 4, 8, 32, 500, 34, 11, 99]
assert findSumOfSequentialNumbersLessThan100(A) == 33
print(findSumOfSequentialNumbersLessThan100(A))
