from collections import deque


class Palindrome:
    def __init__(self):
        self.my_queue = deque([])
        self.my_stack = []

    def pushCharacter(self, character):
        self.my_stack.append(character)

    def enqueueCharacter(self, character):
        self.my_queue.append(character)

    def popCharacter(self):
        return self.my_stack.pop()

    def dequeueCharacter(self):
        return self.my_queue.popleft()


# read the string s
s = raw_input()
# Create the Palindrome class object
p = Palindrome()

l = len(s)
# push all the characters of string s to stack
for i in range(l):
    p.pushCharacter(s[i])
# enqueue all the characters of string s to queue
for i in range(l):
    p.enqueueCharacter(s[i])
f = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l):
    if p.popCharacter() != p.dequeueCharacter():
        f = False
        break
# finally print whether string s is palindrome or not.
if f:
    sys.stdout.write("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write("The word, "+s+", is not a palindrome.")
