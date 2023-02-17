#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:08:16 2023

@author: scognamigliofrancescopio@gmail.com
"""

def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-2) + fibonacci(n-1)

def fibonacciIterative(n):
    A = [0,1]
    if n<=1: return A[n]
    for i in range (2, n+1):
        A.append(A[-1]+A[-2]) # A[-1] take last element
                              # A[-2] take second to last element
    return A[-1]

def fibonacciIterativeOptimized(n):
    f1 = 0
    f2 = 1
    if n<=1: return n
    for i in range (2, n+1):
        f1, f2 = f2, f1+f2
    return f2

#print(fibonacci(30))
print(fibonacciIterative(50))
print(fibonacciIterativeOptimized(50))