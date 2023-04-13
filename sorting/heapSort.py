#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:06:22 2023

@author: scognamigliofrancescopio@gmail.com
"""

def heapify(A, i, size):
    # retrieve the node position
    N = i
    # retrieve the children positions
    L, R = 2*i+1, 2*i+2
    # check the maximum between current node and its children
    if L < size and A[L] > A[N]:
        N = L
    if R < size and A[R] > A[N]:
        N = R
    if N == i: return
    # switch the maximum with the current node
    A[i], A[N] = A[N], A[i]

    # call the procedure on the sub heap
    heapify(A, N, size)

def buildHeap(A):
    # iterate on each parent node
    size = len(A)
    for i in range((size-2)//2, -1, -1): # reverse for
        heapify(A, i, size)

def heapSort(A):
    # build the heap
    buildHeap(A)
    # sort the heap
    for i in range(len(A)-1, 0, -1):
        A[i],A[0] = A[0],A[i]
        heapify(A, 0, i)


v = [18, 16, 17, 12, 15, 10, 1, 8, 4, 14, 11, 3]
print(v)
heapSort(v)
print(v)