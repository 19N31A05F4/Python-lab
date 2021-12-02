import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr)
print(np.shape(arr))
newarr = arr.reshape(2, 2, 3) 
print ("\nReshaped array:\n", newarr) 
print(np.shape(newarr))

arr1=np.arange(0,30,5)
print(arr1)

arr2= np.array([[2,3], [4,5]])
arr2.flatten()

arr3= np.full((2,2),4+1j,dtype=np.complex64)
print(arr3)

