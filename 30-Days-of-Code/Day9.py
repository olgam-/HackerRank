def find_gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


a, b = [int(x) for x in raw_input().strip().split(" ")]
gcd = find_gcd(a, b)
print gcd
