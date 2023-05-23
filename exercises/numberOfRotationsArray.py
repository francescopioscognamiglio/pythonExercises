#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:44:09 2023

@author: scognamigliofrancescopio@gmail.com
"""

def numberOfRotations(A):
    i = 1; j = len(A)-1
    k = 1
    p = A[0]
    while i <= j:
        m = (i+j)//2
        if p > A[m]:
            if p <= A[m-1]:
                k = len(A)-m
                break
            else: j = m-1
        else: i = m+1
    return k


A = [5, 7, 9, 2, 3]
assert numberOfRotations(A) == 2
print(numberOfRotations(A))
A = [9, 2, 3, 5, 7]
assert numberOfRotations(A) == 4
print(numberOfRotations(A))
