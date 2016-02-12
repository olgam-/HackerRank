strings = []
queries = []
N = input()
for i in range(N):
    strings.append(raw_input())
Q = input()
for i in range(Q):
    queries.append(raw_input())

results = [0 for x in queries]
for i, q in enumerate(queries):
    for s in strings:
        if q == s:
            results[i] += 1
    print results[i]
