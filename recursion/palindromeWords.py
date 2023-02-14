#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:36:18 2023

@author: scognamigliofrancescopio@gmail.com
"""

def isPalindrome(A,i,j):
    if i >= j: return True
    if A[i] != A[j]: return False
    return isPalindrome(A,i+1,j-1)

def isPalindromeWithoutIndexes(A):
    if len(A) <= 1: return True
    if A[0] != A[-1]: return False # A[-1] take the last element
    return isPalindromeWithoutIndexes(A[1:-1]) # take elements without the first and the last

# Madam I'm Adam
A0 = []
print(isPalindrome(A0, 0, len(A0)-1))
A1 = ['m','a','d','a','m','i','m','a','d','a','m']
print(isPalindrome(A1,0,len(A1)-1))
A2 = ['r','a','d','a','r']
print(isPalindrome(A2,0,len(A2)-1))
A3 = ['c','a','r','e']
print(isPalindrome(A3,0,len(A3)-1))