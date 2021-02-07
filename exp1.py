"""
try:
   print(x)
except Exception as e:
    print(e)

print("hi")

try:
    a=12
    b='a'
    c=a+b
except TypeError:
    print("addtiton of integer and string is not possible")
print("hello")
"""

try:
    a = 12
    b ='r'
    c=a/b
    print("div=",c)
except TypeError:
    print("divisin of integer and string is not possible")
except ZeroDivisionError:
    print("zero devision error")
finally:
    print("file successfully printed")
print("hello")

