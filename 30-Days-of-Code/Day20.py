import re

phrase = raw_input()
mat = re.split(r"[ '!,?.\\_\[\]'@+]+", phrase)
mat = filter(None, mat)
print len(mat)
for i in mat:
    print i
