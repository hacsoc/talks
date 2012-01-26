#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tim Henderson
# Email: tim.tadh@hackthology.com
# This file is in the Public Domain

import functools

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

def Acc(init, step):
    acc = [init]
    def Acc(op):
        acc[0] = op(acc[0], step)
        return acc[0]
    return Acc

acc = Acc(5, 3)
registry = dict()
def Curry1(f, a, name):
    print "registered '%s'" % name
    def wrapper():
        # make a database call to find out a
        return f(a)
    registry[name] = wrapper 
    return wrapper

addacc = Curry1(acc, add, 'add')
subacc = functools.partial(acc, sub) # no boilerplate

print acc(mul)
print addacc()
print addacc()
print addacc()
print acc(div)
print subacc()

print registry['add']()

