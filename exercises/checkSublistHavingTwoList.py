#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:04:13 2023

@author: scognamigliofrancescopio@gmail.com
"""

class List:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

def checkSublist(p, q):
    while p != None and q != None:
        if p.key == q.key:
            p = p.next
        q = q.next
    return p == None


p = List(1)
p.next = List(2)
p.next.next = List(3)
p.next.next.next = List(4)
q = List(5)
q.next = List(1)
q.next.next = List(2)
q.next.next.next = List(1)
q.next.next.next.next = List(2)
q.next.next.next.next.next = List(3)
q.next.next.next.next.next.next = List(5)
q.next.next.next.next.next.next.next = List(6)
q.next.next.next.next.next.next.next.next = List(4)
assert checkSublist(p, q) == True
print(checkSublist(p, q))

p = List(1)
p.next = List(2)
p.next.next = List(3)
p.next.next.next = List(4)
q = List(1)
q.next = List(2)
q.next.next = List(2)
q.next.next.next = List(1)
q.next.next.next.next = List(4)
q.next.next.next.next.next = List(5)
q.next.next.next.next.next.next = List(6)
q.next.next.next.next.next.next.next = List(3)
q.next.next.next.next.next.next.next.next = List(2)
assert checkSublist(p, q) == False
print(checkSublist(p, q))
