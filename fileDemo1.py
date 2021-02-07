p=open("data.txt")
s=p.read()
print(s)
print(type(p))

x=open("data.txt")
print(x.read(5))

f=open("data.txt")
print(f.readline())
print(f.readline())
print(f.readline())

b=open("data.txt")
l=b.readlines()
print(l)
print(type(l))

m=open("D:\python\data.txt","r")
print(m.read())

with open("D:\python\data1.txt") as x :
 print(x.read())