class Student:
    def __init__(self, firstName, lastName, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone

    def display(self):
        print "First Name:", self.firstName
        print "Last Name:", self.lastName
        print "Phone:", self.phone


class Grade(Student):
    def __init__(self, firstName, lastName, phone, score):
        Student.__init__(self, firstName, lastName, phone)

    def calculate(self):
        if score < 40:
            return "D"
        elif score < 60:
            return "B"
        elif score < 75:
            return "A"
        elif score < 90:
            return "E"
        elif score <= 100:
            return "O"


firstName = raw_input().strip()
lastName = raw_input().strip()
phone = int(raw_input())
score = int(raw_input())
stu = Grade(firstName, lastName, phone, score)
stu.display()
print "Grade:", stu.calculate()
