#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())

number_words = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    21 : "twenty one",
    22 : "twenty two",
    23 : "twenty three",
    24 : "twenty four",
    25 : "twenty five",
    26 : "twenty six",
    27 : "twenty seven",
    28 : "twenty eight",
    29 : "twenty nine"
}

hour = number_words[h]

if (m == 1) or (m ==59):
    min_string = "minute"
else:
    min_string = "minutes"

if m == 0:
    my_string = "%s o' clock" % hour
elif m == 15:
    my_string = "quarter past %s" % hour
elif m < 30:
    minutes = number_words[m]
    my_string = "%s %s past %s" % (minutes, min_string, hour)
elif m == 30:
    my_string = "half past %s" % hour
elif m == 45:
    hour = number_words[h + 1]
    my_string = "quarter to %s" % hour
else:
    minutes = number_words[60 - m]
    hour = number_words[h + 1]
    my_string = "%s %s to %s" % (minutes, min_string, hour)

print my_string
