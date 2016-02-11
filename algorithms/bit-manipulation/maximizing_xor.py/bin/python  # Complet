#!/bin/python

# Complete the function below.


def maxXor( l,  r):
    res = -1
    for i in range(l, r+1):
        for j in range(l, r+1):
            tmp = i ^ j
            if tmp > res:
                res = tmp
    return res


_l = int(raw_input());
_r = int(raw_input());

res = maxXor(_l, _r)
print(res)
