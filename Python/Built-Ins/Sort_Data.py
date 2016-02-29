N, M = map(int, raw_input().strip().split(" "))
a = []
for i in range(N):
    a.append(map(int, raw_input().strip().split(" ")))
k = input()

a.sort(key=lambda x: x[k])

for i in range(N):
    print " ".join(str(j) for j in a[i])
