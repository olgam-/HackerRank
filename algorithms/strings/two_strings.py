times = input()

for n in range(times):
    a = raw_input()
    b = raw_input()
    res = "NO"
    for c in a:
        for i in b:
            if c == i:
                res = "YES"
                break
    print res
