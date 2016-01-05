T = int(raw_input())
for i in range(T):
    inp = raw_input().split()
    inp = [int(x) for x in inp]
    result = inp[0]
    for j in range(inp[2]):
        result += 2**j * inp[1]
        print result,
    print
