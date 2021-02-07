p=open("D:\python\ex1.txt","x")
print(p)
if p:
    print("file created successfully")

m=open("D:\python\ex1.txt","w")
m.write("""
hi
Prathamesh
""")

