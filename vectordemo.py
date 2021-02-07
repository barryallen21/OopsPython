from numpy import array
l=[12,3,45,6,7]
v=array(l)
print(v)
l1=[[12],
   [13],
   [14]]
v1=array(l1)
print(v1)

m=[12,3,4,5]
n=[12,34,5,67]
v=array(m)
v1=array(n)
d=v.dot(v1)
print(d)

c=v+v1
print(c)
x=v-v1
print(x)
z=v*v1
print(z)
t=v/v1
print(t)

w=3
f=v*w
print(f)