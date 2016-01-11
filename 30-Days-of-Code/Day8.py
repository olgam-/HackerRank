n = input()
phonebook = {}
for i in range(n):
    name = raw_input()
    value = input()
    phonebook.update({name: value})

for i in range(n):
    name = raw_input()
    if name in phonebook:
        print "%s=%d" % (name, phonebook[name])
    else:
        print "Not found"
