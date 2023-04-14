#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:58:43 2023

Print out the linked list in reversed order.
You will do it:
    - in recursive way
    - in iterative way
    - in iterative way with workspace O(1) - no other structures can be used

@author: scognamigliofrancescopio@gmail.com
"""

class Node:
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next

def createList(A):
    head = Node(A[0])
    node = head
    for i in range(1, len(A)):
        node.next = Node(A[i])
        node = node.next
    return head

def printReversedViaRecursion(node):
    if (node == None): return
    printReversedViaRecursion(node.next)
    print(node.key)

def printReversedViaIteration(node):
    A = []
    while node != None:
        A.append(node.key)
        node = node.next
    for i in range(len(A)-1, -1, -1):
        print(A[i])

def printNode(node):
    while node != None:
        print(node.key)
        node = node.next

def printReversedViaIterationWithoutAdditionalSpace(node):
    if node == None: return
    prev = node
    node = node.next
    prev.next = None
    while node != None:
        prevnode = node
        nextnode = node.next
        node.next = prev
        prev = prevnode
        node = nextnode
    printNode(prev)


head = createList([1, 3, 4, 2, 5, 3, 6])
printReversedViaRecursion(head)
print()
printReversedViaIteration(head)
print()
printReversedViaIterationWithoutAdditionalSpace(head)
print()
