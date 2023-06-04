#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:25:42 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Record:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

def getFirstSum(node, sum = 0):
    if not node: return None
    if node.key == sum: return node
    return getFirstSum(node.next, node.key + sum)


head = Record(1)
head.next = Record(2)
head.next.next = Record(3)
head.next.next.next = Record(6)
assert getFirstSum(head) == head.next.next
print(getFirstSum(head).key)
