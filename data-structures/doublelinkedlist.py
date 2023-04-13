#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:43:57 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Node:
    # initialization function
    def __init__(self, key = None, prev = None, next = None):
        self.key = key
        self.prev = prev
        self.next = next

def createList(A):
    head = Node(A[0])
    node = head
    for i in range(1, len(A)-1):
        node.next = Node(A[i], node)
        node = node.next
    return head

def printList(node):
    while node != None:
        print(node.key, end=' ')
        node = node.next
    print()

def printListReversed(node):
    while node.next != None:
        node = node.next
    while node != None:
        print(node.key, end=' ')
        node = node.prev
    print()

def addHead(p, q):
    """
    Take a list p
    and add a node q at the start of the list.
    """
    q.next = p
    p.prev = q
    return q

def addAfter(p, q, d):
    """
    Take a list p
    and add a node q after the node d.
    """
    q.prev = d
    q.next = d.next
    q.next.prev = q
    d.next = q

def addBefore(p, q, d):
    """
    Take a list p
    and add a node q before the node d.
    """
    # limit case: the head and the d node before which we have to add the q node are equal
    if p == d:
        return addHead(p, q)
    q.prev = d.prev
    q.prev.next = q
    q.next = d
    d.prev = q
    return p


printList(createList([1, 3, 4, 2, 5, 7]))

l = addHead(createList([1, 3, 4, 2, 5, 7]), Node(11))
printList(l)
printListReversed(l)

addAfter(l, Node(111), l.next.next)
printList(l)
printListReversed(l)

l = addBefore(l, Node(222), l.next.next)
printList(l)
printListReversed(l)
l = addBefore(l, Node(222), l)
printList(l)
printListReversed(l)
