#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:50:51 2023

@author: scognamigliofrancescopio@gmail.com
"""

class List:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

def limit(node):
    # find the new head
    while node != None and node.key > 10:
        node = node.next
    head = node
    while node != None and node.next != None:
        if node.next.key > 10:
            node.next = node.next.next
        else:
            node = node.next
    return head

def reverse(node, next = None, prev = None):
    if node.next == None:
        node.next = prev
        return node
    head = reverse(node.next, node.next.next, node)
    node.next.next = node
    if next == None: node.next = None
    return head

def reverseAndLimit(node):
    head = limit(node)
    printList(head)
    head = reverse(head)
    print()
    printList(head)
    return head

def printList(node):
    while node != None:
        print(node.key)
        node = node.next


head = List(11)
head.next = List(10)
head.next.next = List(3)
head.next.next.next = List(7)
head.next.next.next.next = List(11)
head.next.next.next.next.next = List(12)
head.next.next.next.next.next.next = List(4)
head.next.next.next.next.next.next.next = List(15)
printList(head)
print()
head = reverseAndLimit(head)
