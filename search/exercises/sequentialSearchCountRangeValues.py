#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:21:17 2023

@author: scognamigliofrancescopio@gmail.com
"""

def sequentialSearchCountRangeValues(A,a,b):
    c = 0
    for i in range(len(A)):
        if A[i] >= a and A[i] <= b:
            c += 1
    return c

print(sequentialSearchCountRangeValues([1,3,6,9,12,15], 2, 10))