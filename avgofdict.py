#python program to print average of dictionary values
dict_1={'A':1,'N':4,'B':5,'U':3,'I':4}
print(dict_1)
res=0
for val in dict_1.values():
    res +=val
res=res/len(dict_1)
print("Average of dictionary values:",res)