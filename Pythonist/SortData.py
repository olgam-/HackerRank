numbers = []
first = raw_input()
inp = raw_input()
while inp.__contains__(" "):
    numbers.append(inp.split(" "))
    inp = raw_input()

numbers = [[int(j) for j in i] for i in numbers]

numbers.sort(key=lambda x: x[int(inp)])

for element in numbers:
    print " ".join(map(str, element))
