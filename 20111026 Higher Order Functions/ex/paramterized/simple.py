#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tim Henderson
# Email: tim.tadh@hackthology.com
# This file is in the Public Domain

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

def DoOp(f, a, b): return f(a,b)

print DoOp(add, 1, 2)

