num = input()
grades = {}
for n in range(num):
    x = raw_input().strip().split(" ")
    grades[x[0]] = (float(x[1]) + float(x[2]) + float(x[3])) / 3.0

name = raw_input()
print "%.2f" %grades[name]

