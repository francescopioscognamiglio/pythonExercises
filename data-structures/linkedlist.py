#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:12:35 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Node:
    # initialization function
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next

def createList(A):
    node = None
    # from the end to the start
    for i in range(len(A)-1, -1, -1):
        node = Node(A[i], node)
    return node

def createList2(A):
    first = Node(A[0])
    node = first
    # from the start to the end
    for i in range(1, len(A)):
        node.next = Node(A[i])
        node = node.next
    return first

def printList(node):
    while node:
        print(node.key, end=' ')
        node = node.next
    print()

def addHead(p, q):
    """
    Take a list p
    and add a node q at the start of the list.
    """
    q.next = p
    return q

def addAfter(p, q, d):
    """
    Take a list p
    and add a node q after the node d.
    """
    q.next = d.next
    d.next = q

def addBefore(p, q, d):
    """
    Take a list p
    and add a node q before the node d.
    """
    # limit case: add the node at the start because the node d is the first node p
    if (p == d):
        return addHead(p, q)
    head = p
    # search the previous node
    while p.next != d:
        p = p.next
    q.next = d
    p.next = q
    return head


# manual setup
firstNode = Node(6)
assert firstNode.key == 6
assert firstNode.next == None
print(firstNode.key)
print(firstNode.next)
firstNode.next = Node(10)
assert firstNode.next.key == 10
assert firstNode.next.next == None
print(firstNode.next.key)
print(firstNode.next.next)
firstNode.next.next = Node(15)
assert firstNode.next.next.key == 15
assert firstNode.next.next.next == None
print(firstNode.next.next.key)
print(firstNode.next.next.next)

# using something more dynamic
printList(createList([1, 3, 4, 2, 5, 7]))

l = addHead(createList([1, 3, 4, 2, 5, 7]), Node(11))
printList(l)

addAfter(l, Node(111), l.next.next)
printList(l)

l = addBefore(l, Node(222), l.next.next)
printList(l)
l = addBefore(l, Node(222), l)
printList(l)
