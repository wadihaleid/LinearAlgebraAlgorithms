import numpy as np
import matplotlib.pyplot as plt


def generateOrthognalArray (m , n):
    arr = np.empty([m,n])
    arr[:,0] = np.ones(m , np.int)
    for i in range(0,m-1):
        item = i * (1/(m - 1))
        for j in range(1 , n):
            arr[i , j] = pow(item , j-1)
    return arr


arr1 = generateOrthognalArray(3 , 3)

print(arr1)

print('Conditioning number : ' + str(np.linalg.cond(arr1)))


