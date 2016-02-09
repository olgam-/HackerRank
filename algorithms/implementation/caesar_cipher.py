#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

k = k % 26
caesar = ""
for i in s:
    if i.isalpha():
        letter = ord(i) + k
        if i.isupper():
            if letter > ord("Z"):
                letter -= 26
        elif i.islower():
            if letter > ord("z"):
                letter -= 26
        caesar += chr(letter)
    else:
        caesar += i

print caesar
