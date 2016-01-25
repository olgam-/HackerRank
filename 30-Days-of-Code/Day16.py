size = input()
array = map(int, raw_input().strip().split(' '))
array.sort()
numbers = []
min = abs(array[0] - array[1])
numbers.append(array[0])
numbers.append(array[1])
for i in range(size-1):
    if abs(array[i] - array[i+1]) < min:
        min = abs(array[i] - array[i+1])
        numbers = []
        numbers.append(array[i])
        numbers.append(array[i+1])
    elif abs(array[i] - array[i+1]) == min:
        min = abs(array[i] - array[i+1])
        numbers.append(array[i])
        numbers.append(array[i+1])
for n in numbers:
    print n,
