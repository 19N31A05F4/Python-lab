#tuple operations
x=(1,2,3,4,5,6)
print(x)
print(type(x))
print(x[2]) #accessing
print(x[-5])
print(x[0:3])
t=list(x)
t.append(7) #adding using list
x=tuple(t)
print(x)
y=len(x) #length of tuple
print(y)
print(any(x))
if 7 in x:  #check for an element
    print("is present in tuple")
else:
     print("not present")

for name in ('anji','rakesh'):
    print("hello",name)