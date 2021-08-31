#dictionary operations
d={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F'}
print(d)
print(type(d))
print(d.keys())
print(d.values())
print(d.pop(4))
x=d[1]
print(x)
y=d.get(5)
print(y)
d[6]='G'
print(d)
print(len(d))
d.clear()
print(d)