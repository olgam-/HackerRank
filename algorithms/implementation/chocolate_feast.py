#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    chocolates = n/c
    wrappers = chocolates

    while wrappers >= m:
        fresh = wrappers/m
        chocolates += fresh
        wrappers = (wrappers % m) + fresh

    print chocolates
