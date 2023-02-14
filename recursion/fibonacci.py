#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:08:16 2023

@author: scognamigliofrancescopio@gmail.com
"""

def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(30))