class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)

        # self.maximumDifference = 0
        # for i in range(len(self.__elements)):
        #     for j in range(i+1, len(self.__elements)):
        #         diff = abs(i - j)
        #         if diff > self.maximumDifference:
        #             self.maximumDifference = diff


_ = raw_input()
a = [int(e) for e in raw_input().split(" ")]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
