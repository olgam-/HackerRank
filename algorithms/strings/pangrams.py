alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
phrase = raw_input().lower()

flag = True
for i in alphabet:
    if i not in phrase:
        flag = False
        break

if flag:
    print "pangram"
else:
    print "not pangram"
