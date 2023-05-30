#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:08:56 2023

@author: scognamigliofrancescopio@gmail.com
"""

def fromPosToParentArray(A):
    C, P, i = [], [], 0
    while i < len(A):
        if A[i] != None:
            C.append(A[i])
            ppos = (i-1)//2
            if ppos >= 0:
                P.append(ppos)
            else:
                P.append(None) # manage the root
        i += 1
    return C, P


A = [1, 3, 10, 4, 2]
C, P = fromPosToParentArray(A)
print(C)
print(P)
assert C == [1, 3, 10, 4, 2]
assert P == [None, 0, 0, 1, 1]
