import numpy as np
def matrixMultiplication(A,B,n):
    '''This function will return multiplication of two n*n matrices
    '''
    #Initializing result array with 0
    c = [[0 for x in range(n)]for y in range(n)]
    #for rows
    for i in range(n):
        #for columns
        for j in range(n):
            c[i][j]=0
            #for result matrix calculation
            for k in range(n):
                c[i][j] = c[i][j]+A[i][k]*B[k][j]
    return c
            
A = [[1,0],[0,1]]
B = [[-8,4],[2,5]]
n = 2
result  = matrixMultiplication(A,B,n)
#for better output display
result = np.reshape(result,(2,2))
print(result)
#print(np.matmul(A,B)) Using Numpy will get same result
