#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:58:13 2023

@author: scognamigliofrancescopio@gmail.com
"""

## remove the maximux (it is the first element: A[i])
def extractMax(A, size):
    # move the last element into the first
    size -= 1
    A[0] = A[size]
    A.pop(size)
    # fix the heap to satisfy this rule: each node is greater than or equal to its children
    heapify(v, 0, len(v))

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


v = [18, 16, 17, 12, 15, 10, 1, 8, 4, 14, 11, 3]
print(v)
extractMax(v, len(v))
print(v)
