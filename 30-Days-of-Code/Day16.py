size = input()
array = map(int, raw_input().strip().split(' '))

numbers = []
min = abs(array[0] - array[1])
numbers.append(array[0])
numbers.append(array[1])
for i in range(size-1):
    for j in range(i +1, size):
        if abs(array[i] - array[j]) < min:
            min = abs(array[i] - array[j])
            numbers = []
            numbers.append(array[i])
            numbers.append(array[j])
        elif abs(array[i] - array[j]) == min:
            min = abs(array[i] - array[j])
            numbers.append(array[i])
            numbers.append(array[j])
numbers.sort()
for n in numbers:
    print n,
