#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:23:32 2023

@author: scognamigliofrancescopio@gmail.com
"""

def quickSort(A, i, j):
    if i < j:
        m = partition(A, i, j)
        quickSort(A, i, m-1)
        quickSort(A, m+1, j)

def partition(A, i, j):
    p = i # the position of the pivot
    while i < j:
        while i < j and A[j] > A[p]: # in the right side we have all elements greater than the pivot
            j -= 1
        while i < j and A[i] <= A[p]: # in the left side we have all elements less or equal than the pivot
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i] # switch elements
            i += 1
            j -= 1
    A[i], A[p] = A[p], A[i] # set the pivot in its final position


