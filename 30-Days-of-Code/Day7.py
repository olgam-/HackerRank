n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for i in range(n):
    print arr[n-i-1],
