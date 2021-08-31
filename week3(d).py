#check whether two lists are equal or not
def check(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    else:
        return sorted(list_1) == sorted(list_2)
list_1=[]
list_2=[]
n1=int(input("Enter number of elements in list_1:"))
n2=int(input("Enter number of elements in list_2:"))
    
for i in range(0,n1):
    ele=input()
    list_1.append(ele)
print(list_1)
for i in range(0,n2):
    elem=input()
    list_2.append(elem)
print(list_2)
if check(list_1,list_2):
    print("Two lists are equal")
else:
    print("Lists are not equal")
