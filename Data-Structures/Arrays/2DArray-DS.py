arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

max = -9 * 7
for i in range(4):
    for j in range(4):
        sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if sum > max:
            max = sum

print max