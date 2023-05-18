#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:10:32 2023

@author: scognamigliofrancescopio@gmail.com
"""

def countingSortBoolean(A):
    zero = 0
    for i in range(0, len(A)):
        if A[i] == 0: zero += 1
    for i in range(0, len(A)):
        if zero > 0:
            A[i] = 0
            zero -= 1
        else: A[i] = 1


A = [0, 1, 1, 0, 0, 1, 0, 1, 1]
print(A)
countingSortBoolean(A)
assert A == [0, 0, 0, 0, 1, 1, 1, 1, 1]
print(A)
