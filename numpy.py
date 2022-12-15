#Numpy :---Numerical Python:
#Numpy supports heavy mathematical operations:
#Based on Array:
#import numpy as np
#
#l1 = [33,44,66,88,33,11]
#
#arr1 = np.array(l1)
#
#print(arr1)
#
#print(type(arr1))
#print(arr1[2:5])
# main functions in array:
#ones --- will create array where all items are 1
#zeros -- will create array where all itemsa are 0
#arange
#linspace
#random.randint
#reshape
import numpy as np
#arr1 = np.zeros((4,5,3),dtype = int)
#print(arr1)
#
#print(arr1.dtype)
#
#print(type(arr1))
#
#print(arr1.size)#total no of items in ur array
#
#print(arr1.ndim)
#
#print(arr1.shape[1])
#arange:always creates 1D array
#arr1 = np.arange(5,21,2)
#
#print(arr1)
#random.randint
#arr2 = np.random.randint(30,45, size = 10)
#arr2 = np.random.randint(30,45, size = (4,5))
#arr2 = np.random.randint(50,55,size=(4,5,2))
#
#print(arr2)
#reshape
#one_d = np.arange(1,29)
#print(one_d)
#
#two_d = one_d.reshape(7,4)
##print(two_d[3:5,1:3])
##print(two_d[2:,1])
#
#three_d = np.arange(1,31).reshape(3,5,2)
#
#print(three_d[1][2][1])
#print(one_d)
#
#print(one_d + 2)
arr1 = np.array([2,4,6,8,10,12])
#
#arr2 = np.array([4,5,6,7,8,8])
#
#print(arr1-arr2)
#print(arr1 + 2)
#
#print(arr1 - 2)
#
#print(arr1 * 2)
#
#print(arr1 ** 2)
#
print(arr1.max())
print(arr1.min())
print(arr1.mean())

print(arr1.std())