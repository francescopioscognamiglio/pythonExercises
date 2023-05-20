#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:15:39 2023

@author: scognamigliofrancescopio@gmail.com
"""

class List:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def removeDuplicate(node):
    while node != None and node.next != None:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next

def removeDuplicateRec(node):
    if node == None or node.next == None: return
    if node.val == node.next.val:
        node.next = node.next.next
    else:
        node = node.next
    removeDuplicateRec(node)

def printList(node, h = 0):
    if node == None: return
    print(h*'-', node.val)
    printList(node.next, h+1)


head = List(3)
head.next = List(3)
head.next.next = List(3)
head.next.next.next = List(4)
head.next.next.next.next = List(4)
head.next.next.next.next.next = List(7)
head.next.next.next.next.next.next = List(7)
head.next.next.next.next.next.next.next = List(7)
head.next.next.next.next.next.next.next.next = List(9)
head.next.next.next.next.next.next.next.next.next = List(9)
head.next.next.next.next.next.next.next.next.next.next = List(9)
head.next.next.next.next.next.next.next.next.next.next.next = List(9)
printList(head)
removeDuplicate(head)
printList(head)

head = List(3)
head.next = List(3)
head.next.next = List(3)
head.next.next.next = List(4)
head.next.next.next.next = List(4)
head.next.next.next.next.next = List(7)
head.next.next.next.next.next.next = List(7)
head.next.next.next.next.next.next.next = List(7)
head.next.next.next.next.next.next.next.next = List(9)
head.next.next.next.next.next.next.next.next.next = List(9)
head.next.next.next.next.next.next.next.next.next.next = List(9)
head.next.next.next.next.next.next.next.next.next.next.next = List(9)
printList(head)
removeDuplicateRec(head)
printList(head)
