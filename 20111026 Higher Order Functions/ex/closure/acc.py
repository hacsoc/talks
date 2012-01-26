#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tim Henderson
# Email: tim.tadh@hackthology.com
# This file is in the Public Domain

# var Acc = func(init, step) {
#     acc = init
#     return func(op) {
#         acc = op(acc, step)
#         return acc
#     }
# }

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
print acc(mul)
print acc(add)
print acc(add)
print acc(add)
print acc(div)

