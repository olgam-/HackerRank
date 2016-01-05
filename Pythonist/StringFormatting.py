N = input()
padding = len(bin(N)[2:])

for i in range(1, N+1):
    print str(i).rjust(padding) + " " + oct(i)[1:].rjust(padding) + " " + hex(i)[2:].upper().rjust(padding) + " " + bin(i)[2:].rjust(padding)
