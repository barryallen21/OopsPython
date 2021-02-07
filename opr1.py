class comp:


    def __init__(self,r,y):
        self.r=r
        self.y=y

    def __add__(self, other):

        self.r=self.r+other.r
        self.y=self.y+other.y
        return comp(self.r,self.y)

    def __str__(self):                      #__str__ function converts python objects into strings
        return("({0},{1})".format(self.r,self.y))

    def disp(self):
        print("x=",self.r)
        print("y=",self.y)

c=comp(12,3)
#print(c)
d=comp(5,6)
n=c+d
n.disp()
print(n)
