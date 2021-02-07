class bb:
    def disp(self):
        print("base  class")

class der(bb):
    def show(self):
        print("derived class")

class der1(bb):
    def show1(self):
        print("derived class 2")

d=der()
d.disp()
d.show()
d1=der1()
d1.disp()
d1.show1()