#!/bin/python

import sys


n = int(raw_input().strip())

mystring = []

for i in range(0,n):
    mystring = n * "#"
    print '{:>{}s}'.format(mystring[0:i+1], n)
