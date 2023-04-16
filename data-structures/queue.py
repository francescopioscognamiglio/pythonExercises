#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:03:34 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Queue:
   def __init__(self, key = None, next = None):
       self.key = key
       self.next = next

def enqueue(head, tail, node):
    """
    Insert a new node at the end of the queue.

    Parameters
    ----------
    head : Queue
        The head.
    tail : Queue
        The tail.
    node : Queue
        The new node to insert.

    Returns
    -------
    head : Queue
        The updated head.
    node : Queue
        The updated tail.

    """
    if head == None:
        head = node
        tail = node
    else:
        tail.next = node
    return head, node # the node become the new tail

def dequeue(head, tail):
    """
    Extract the node from the start of the queue.

    Parameters
    ----------
    head : Queue
        The head.
    tail : Queue
        The tail.

    Returns
    -------
    head : Queue
        The updated head.
    tail : Queue
        The updated tail.
    node : Queue
        The extracted node.

    """
    if head == None: return None, None, None # empty queue
    node = head
    head = node.next
    node.next = None
    if head == None: tail = None # empty queue
    return head, tail, node


head, tail = enqueue(None, None, Queue(5))
head, tail = enqueue(head, tail, Queue(15))
head, tail = enqueue(head, tail, Queue(2))
head, tail = enqueue(head, tail, Queue(7))
head, tail = enqueue(head, tail, Queue(11))
head, tail, node = dequeue(head, tail)
assert node.key == 5
print(node.key)
head, tail, node = dequeue(head, tail)
assert node.key == 15
print(node.key)
head, tail, node = dequeue(head, tail)
assert node.key == 2
print(node.key)
head, tail, node = dequeue(head, tail)
assert node.key == 7
print(node.key)
