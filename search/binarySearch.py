#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:09:40 2023

@author: scognamigliofrancescopio@gmail.com
"""

import math
import random

def binarySearch(A,x):
    n = len(A)
    i = 0
    j = n-1
    while i <= j:
        m = math.floor((i+j)/2)
        if x == A[m]: return m
        if x < A[m]: j = m-1 # search into the n/2 left part of the array
        else: i = m+1 # search into the n/2 right part of the array
    return None

n = 10000
foundCounter = 0
pos = 0
# prepare a list of n sequential elements (ordered)
list = [x for x in range(n)]
for i in range (n):
    x = random.randint(0, n*2)
    print('searching ' + str(x) + ' ...')
    v = binarySearch(list, x)
    if (v != None):
        pos += v
        foundCounter += 1

print('the position average is: ' + str(int(pos/n)))
print('the search average is: ' + str(foundCounter/n))