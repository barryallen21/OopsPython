class p():
    def __init__(self,n):
        self.n = n

    def __pow__(self, power, modulo=None):
        self.n = self.n**power.n
        return self.n

ob1 = p(2)
ob2 = p(3)

o = ob1**ob2
print(o)