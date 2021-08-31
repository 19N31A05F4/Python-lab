#largest of three numbers
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if a>b and a>c:
    print("a is greater")
elif b>c and b>a:
    print("b is greater")
else:
    print("c is greater")