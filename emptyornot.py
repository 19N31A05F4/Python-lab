#check whether the list is empty or not
list=[]
n=eval(input("Enter the size of list:"))
for x in range(n):
    ele=input()
    list.append(ele)
if len(list)!=0:
    print("There are elements in the list")
else:
    print("List is empty")
