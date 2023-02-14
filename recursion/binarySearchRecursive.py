#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:14:52 2023

@author: scognamigliofrancescopio@gmail.com
"""

import math
import random

def binarySearchRecursive(A,x):
    n = len(A)
    c = math.floor(n/2)

    if (A[c] == x): return True # element found
    if (n == 1): return False # no element found

    if (A[c] > x): return binarySearchRecursive(A[0:c], x) # search into the n/2 left part of the array
    return binarySearchRecursive(A[c+1:n], x) # search into the n/2 right part of the array


n = 10000
foundCounter = 0
# prepare a list of n sequential elements (ordered)
list = [x for x in range(n)]
for i in range (n):
    x = random.randint(0, n*2)
    print('searching ' + str(x) + ' ...')
    v = binarySearchRecursive(list, x)
    if (v == True): foundCounter+=1

print('the search average is: ' + str(foundCounter/n))