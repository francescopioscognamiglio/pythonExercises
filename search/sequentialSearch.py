#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:43:53 2023

@author: scognamigliofrancescopio@gmail.com
"""

import random

def sequentialSearch(A,x):
    n = len(A)
    for i in range (n):
        if (A[i] == x): return i
    return None

n = 10000
x = 1
# prepare a list of n sequential elements
list = [x for x in range(n)]
# shuffle to have an unordered list
random.shuffle(list)
# calculate the average
m = 0
for i in range (n):
    pos = sequentialSearch(list, x)
    if (pos != None): m += pos

print('the position average is: ' + str(m/n))