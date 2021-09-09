#python program to print 
dict_1={'A':1,'B':2,'F':7,'Z':5,'Y':6,'I':4}
print(dict_1)
for k,v in list(dict_1.items()): 
    if dict_1[k]>5:
        del(dict_1[k])
print(dict_1)
