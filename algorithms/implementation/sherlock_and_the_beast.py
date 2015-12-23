#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    my5div = n / 3
    my5mod = n % 3

    if my5div < 1:
        print "-1"
    elif my5mod == 0:
        print n * "5"
    elif my5mod == 1 and n >= 10:
        print (n - 10) * "5" + 10 * "3"
    elif my5mod == 2:
        print (n - 5) * "5" + 5 * "3"
    else:
        print "-1"
