#!/usr/bin/py
def lonelyinteger(a):
    answer = 0
    for i in b:
        answer = answer ^ i
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
