#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tim Henderson
# Email: tim.tadh@hackthology.com
# This file is in the Public Domain

def qsort(arr, less):
    
    def partition(l, r):
        def swap(a, b):
            tmp = arr[a]
            arr[a] = arr[b]
            arr[b] = tmp

        next = l
        pivot = arr[r]
        for i in xrange(l, r+1):
            if less(arr[i], pivot):
                swap(i, next)
                next += 1
        swap(next, r)
        return next
    
    def qsort(l, r):
        if r <= l: return
        pivot = partition(l, r)
        qsort(l, pivot-1)
        qsort(pivot+1, r)
    
    qsort(0, len(arr)-1)

def less(a, b):
    return a < b

def more(a, b):
    return a > b

a = [3, 9,1, 0,5,2,0,1,5,7,12,4,5,7]
print a
qsort(a, less)
print a
qsort(a, more)
print a

