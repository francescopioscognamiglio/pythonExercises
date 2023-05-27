#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 11:51:02 2023

@author: scognamigliofrancescopio@gmail.com
"""

class CircularList:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

def findMin(node):
    if node == None: return None
    rootk = node.key
    min = node.key
    node = node.next
    while node != None and node.key != rootk:
        if node.key < min:
            min = node.key
        node = node.next
    return min

def printCircularList(node):
    rootk = node.key
    print(node.key)
    node = node.next
    while node != None and node.key != rootk:
        print(node.key)
        node = node.next


head = CircularList(31)
head.next = CircularList(10)
head.next.next = CircularList(15)
head.next.next.next = CircularList(12)
head.next.next.next.next = CircularList(14)
head.next.next.next.next.next = CircularList(3)
head.next.next.next.next.next.next = CircularList(9)
head.next.next.next.next.next.next.next = CircularList(7)
head.next.next.next.next.next.next.next.next = head
printCircularList(head)
assert findMin(head) == 3
print('the minimum is:', findMin(head))
