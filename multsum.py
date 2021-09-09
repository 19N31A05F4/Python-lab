num=int(input("enter a number to  multiply:"))
n=int(input("enter the size of the list:"))
list_1=[]
for i in range(n):
  val=int(input("enter:"))
  list_1.append(num*val)
print(list_1)
print(sum(list_1),":Sum")