N = input()
x = map(int,raw_input().strip().split(' '))

maximum = float('-inf')
second = float('-inf')
for i in x:
    if i > maximum:
        second = maximum
        maximum = i
    elif i > second and i != maximum:
        second = i
    
print second
