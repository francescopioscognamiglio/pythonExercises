#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 12:03:08 2023

@author: scognamigliofrancescopio@gmail.com
"""

def findFirstPositive(f):
    if f(0) > 0: return 0
    x = 1
    while f(x) < 0:
        x *= 2
    i, j = x//2, x
    while i <= j:
        m = (i+j)//2
        if f(m) > 0:
            x = m
            j = m-1
        else:
            i = m+1
    return x


f = lambda x : -100+3*x
assert findFirstPositive(f)
print(findFirstPositive(f))
