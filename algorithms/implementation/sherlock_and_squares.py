#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = raw_input()
    k = n.split()
    a = int(k[0]) ** 0.5
    b = int(k[1]) ** 0.5

    if a - int(a) == 0:
        sum = 1
    else:
        sum = 0
    a = int(a)
    b = int(b)
    sum += (b - a)
    print sum
