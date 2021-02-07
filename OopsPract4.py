class base():
    def get(self):
        self.a = 34
        self.b = 45

class der(base):
    def add(self):
        self.c= (self.a+self.b)
        print(self.c)

class der1(der):
    def sub(self):
        self.d = self.c - self.b
        print(self.d)

class der2(der1):
    def mul(self):
        self.e = self.c*self.d
        print(self.e)

print(issubclass(der,base))
print(super(der))

ob1 = der2()
ob1.get()
ob1.add()
ob1.sub()
ob1.mul()