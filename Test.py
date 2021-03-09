import numpy as np
import scipy
import scipy.linalg

a = np.array([[1,1,1,1] , [1,2,3,4] , [1,3,6,10] , [1,4,10,20]])

P, L, U = scipy.linalg.lu(a)

print(P)
print(L)
print(U)