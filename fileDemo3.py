x = open("d:\python\std1.txt","a")

a = int(input("enter id"))
b = input("enter name")
c = int(input("enter mo no"))

x.write(str(a))
x.write(b)
x.write(str(c))
x.close()



