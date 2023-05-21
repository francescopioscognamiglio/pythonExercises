#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 18:02:08 2023

@author: scognamigliofrancescopio@gmail.com
"""

class List:
    def __init__(self, val, next = None, prec = None):
        self.val = val
        self.next = next
        self.prec = prec

def getTail(node):
    while node.next != None:
        node = node.next
    return node

def isPalindrome(node):
    if node == None: return False
    nodeTail = getTail(node)
    while node != nodeTail:
        if node.val != nodeTail.val:
            return False
        node = node.next
        nodeTail = nodeTail.prec
    return True


head = List(0)
head.next = List(1)
head.next.prec = head
head.next.next = List(0)
head.next.next.prec = head.next
head.next.next.next = List(1)
head.next.next.next.prec = head.next.next
head.next.next.next.next = List(1)
head.next.next.next.next.prec = head.next.next.next
head.next.next.next.next.next = List(0)
head.next.next.next.next.next.prec = head.next.next.next.next
print(isPalindrome(head))

head = List(1)
head.next = List(1)
head.next.prec = head
head.next.next = List(0)
head.next.next.prec = head.next
head.next.next.next = List(1)
head.next.next.next.prec = head.next.next
head.next.next.next.next = List(1)
head.next.next.next.next.prec = head.next.next.next
print(isPalindrome(head))
