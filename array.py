from array import *

a1=array('i',[23,56,11,22,40,90])

print(type(a1))

print(a1)

for x in a1:
    print(x)

for i in range(5):
    print(a1[i],end='')

print("\n")
a1.append(90)
print(a1)

c=a1.count(90)
print(c)

print(a1.fromlist([90]))

print(sorted(a1))