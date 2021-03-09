import numpy as np

def project (a , b):
    return (a.T * b) / np.linalg.norm(a)


def runCGS (arr):
    ## QR factorization Using Classical Gram Schmidt process.
    nCols = np.size(arr , 1)
    nRows = np.size(arr , 0)

    q = np.empty([nRows , nCols])
    v = np.empty([nCols])
    r = np.empty([nRows , nCols])

    q[:,0] =  arr[:,0]/(np.sqrt(arr[:,0].T@arr[:,0]))

    for j in range(1,nCols):
        v = arr[:,j]
        for k in range(0,j):
            v = v - (q[:,k]@arr[:,j])*q[:,k] 
        q[:,j] =  v / (np.sqrt(v.T@v))    
    
    r = np.transpose(q) @ arr
    return q , r  
        

a = np.array([[1,1],[2,-1],[-2,4]])
q , r = runCGS(a)
print(q)
print(r)
print(q@r)