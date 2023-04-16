#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:40:09 2023

@author: scognamigliofrancescopio@gmail.com
"""

class Stack:
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next

def push(top, node):
    node.next = top
    return node

def pop(top):
    if top == None: return None, None # empty stack
    newtop = top.next
    top.next = None
    return top, newtop


top = Stack(5)
top = push(top, Stack(11))
top = push(top, Stack(3))
top = push(top, Stack(63))
node, top = pop(top)
assert node.key == 63
print(node.key)
node, top = pop(top)
assert node.key == 3
print(node.key)
node, top = pop(top)
assert node.key == 11
print(node.key)
node, top = pop(top)
assert node.key == 5
print(node.key)
