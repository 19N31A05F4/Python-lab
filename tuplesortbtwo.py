tup_1=(('anji',7),('rakesh',5),('tarun',3),('naveen',4),('vamsi',8))
print(tup_1)
list_1=list(tup_1)
def Sort_List(list_1):
    list_1.sort(key=lambda x:x[1])
    return list_1
tup_1=tuple(Sort_List(list_1))
print(tup_1)
