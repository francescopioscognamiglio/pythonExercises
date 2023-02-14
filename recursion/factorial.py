#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:38:54 2023

@author: scognamigliofrancescopio@gmail.com
"""

def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

print(factorial(5))