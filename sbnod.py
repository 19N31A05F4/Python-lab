#python program which sorts the tuples by the total numbers or digits
tuple_1=((3,4,6),(1,2,3,4),(6,7,8,9,2,3),(4,3))
def count_digits(ele):
    return len(ele)
list_1=list(tuple_1)
print(list_1)
list_1.sort(key=count_digits)
tuple_1=tuple(list_1)
print('sorted tuple is :',tuple_1)