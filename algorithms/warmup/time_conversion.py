#!/bin/python

import sys


time = raw_input().strip()

if time[8] == "P":
    new = (int(time[:2]) + 12)

    if new != 24:
        print str(new) + time[2:8]
    else:
        print "12" + time[2:8]

elif time[8] == "A":
    if time[0:2] == "12":
        print "00" + time[2:8]
    else:
        print time[:8]
