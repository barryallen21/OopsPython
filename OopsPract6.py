class base():
    def fun1(self,no_1,no_2,no_3):
        print(no_1 * no_2*no_3)


class der():
    def fun1(self,no_1,no_2,no_3):
        base.fun1(self,12,3,5)
        print(no_1 + no_2 +no_3)

o1 = der()
o1.fun1(12,3,45)
