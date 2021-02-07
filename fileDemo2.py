p=open("d:\python\stud.txt","w")
p.write("""hello
hi
bye""")
p.close()

l=['red','\ngreen','\nblue']
m=open('d:\python\clr2.txt','w')
m.writelines(l)

"""li = ['nfakfa','jakhf']
with open('d:\python\clr1.txt','w') as p:
    for i in li:
        print(p,i)"""