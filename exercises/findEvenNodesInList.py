#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:26:01 2023

@author: scognamigliofrancescopio@gmail.com
"""

class List:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def countEven(node):
    if node == None: return 0
    even = 0
    if node.val % 2 == 0: even = 1
    return countEven(node.next) + even


head = List(3)
head.next = List(5)
head.next.next = List(2)
head.next.next.next = List(4)
head.next.next.next.next = List(4)
head.next.next.next.next.next = List(8)
head.next.next.next.next.next.next = List(7)
head.next.next.next.next.next.next.next = List(7)
head.next.next.next.next.next.next.next.next = List(1)
head.next.next.next.next.next.next.next.next.next = List(9)
head.next.next.next.next.next.next.next.next.next.next = List(2)
head.next.next.next.next.next.next.next.next.next.next.next = List(2)
print(countEven(head))
