#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:49:46 2023

@author: scognamigliofrancescopio@gmail.com
"""

def extract(A, isMaxHeap = True):
    first = A[0]
    last = len(A)-1
    A[0] = A[last]
    A.pop(last)
    heapify(A, 0, last, isMaxHeap)
    return first

def insert(A, e, isMaxHeap = True):
    A.append(e)
    heapifyFromBottom(A, len(A)-1, len(A), isMaxHeap)

def heapify(A, i, size, isMaxHeap):
    P = i
    L, R = 2*i+1, 2*i+2
    if isMaxHeap:
        if L < size and A[L] > A[P]:
            P = L
        if R < size and A[R] > A[P]:
            P = R
    else:
        if L < size and A[L] < A[P]:
            P = L
        if R < size and A[R] < A[P]:
            P = R
    if P == i: return
    A[P], A[i] = A[i], A[P]
    heapify(A, P, size, isMaxHeap)

def heapifyFromBottom(A, i, size, isMaxHeap):
    C = i
    P = (i-1)//2
    if isMaxHeap:
        if P >= 0 and A[P] < A[C]:
            C = P
    else:
        if P >= 0 and A[P] > A[C]:
            C = P
    if C == i: return
    A[C], A[i] = A[i], A[C]
    heapifyFromBottom(A, C, size, isMaxHeap)

def maxHeapToMinHeap(A):
    B = []
    while len(A) > 0:
        insert(B, extract(A), False)
    return B


# testing a max heap
v = [18, 16, 17, 12, 15, 10, 1, 8, 4, 14, 11, 3]
print(v)
extract(v)
print(v)
insert(v, 100)
print(v)
print()
# testing a min heap
v = [2, 3, 10, 5, 6, 12, 14]
print(v)
extract(v, False)
print(v)
insert(v, 1, False)
print(v)
print()
# extract all nodes from a max heap and insert them into a min heap
v = [18, 16, 17, 12, 15, 10, 1, 8, 4, 14, 11, 3]
print(v)
print(maxHeapToMinHeap(v))
