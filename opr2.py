class opr1():

    def __init__(self, no):
        self.no = no

    def __lt__(self, other):
        if (self.no < other.no):
            return ("second no is greater")
        else:
            return ("first no is greater")


ob1 = opr1(234)
ob2 = opr1(12)
print(ob1 < ob2)
