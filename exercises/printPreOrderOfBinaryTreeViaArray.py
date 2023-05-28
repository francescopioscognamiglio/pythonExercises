#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 18:44:33 2023

@author: scognamigliofrancescopio@gmail.com
"""

def printPreOrder(A, i = 0):
    if i >= len(A) or A[i] == None: return
    print(A[i], end = ' ')
    printPreOrder(A, 2*i+1) # left child
    printPreOrder(A, 2*i+2) # right child


A = [18, 16, 10, 12, 15, 3, 1, 8, 4, 14, 11]
printPreOrder(A)
print()
B = ['a','b','e','c','d','f','g', None, None, None, None, 'h', None, None, 'i']
printPreOrder(B)
