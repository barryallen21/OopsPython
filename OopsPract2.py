class add:
    a = 67
    b = 23

    @classmethod
    def sum(cls,d):
        c = cls.a + cls.b + d
        return c

    @staticmethod
    def barry(a,b,c):
        return a+b+c


ob1 = add()
ob2 = add()
s = ob1.sum(23)
print(s)
print(ob2.barry(23,67,67))
