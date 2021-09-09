#python program to print only even numers from the given input list
list_1=[]
n=int(input("Enter the size of the list:"))
for i in range(n):
  val=int(input("Enter:"))
  if val%2==0:
    list_1.append(val)
print(list_1)