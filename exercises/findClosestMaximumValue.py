#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:28:48 2023

@author: scognamigliofrancescopio@gmail.com
"""

def findClosestMax(A, x):
    i, j = 0, len(A)-1
    while True:
        if i == j:
            if A[i] > x: return i
            else: return -1
        m = (i+j)//2
        if A[m] > x: j = m
        else: i = m+1


A = [1, 2, 8, 10, 11, 12, 19]
print(findClosestMax(A, 7))
print(findClosestMax(A, 30))
