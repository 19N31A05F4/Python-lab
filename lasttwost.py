list=[]
n=int(input("enter the num"))
for i in range(n):
    x=input()
    list.append(x)

c=0
a=input("enter the string")
k=a[0]
l=a[1]
for i in range(len(list)):
    x=str(list[i])
    y=x[::-1]
    if y[0]==l and y[1]==k:
        c=c+1
print(c)