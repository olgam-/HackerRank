M = input()
T = input()
X = input()

tip = T * M / float(100)
tax = X * M / float(100)
price = round(M + tip + tax)

print "The final price of the meal is $%d." % price
