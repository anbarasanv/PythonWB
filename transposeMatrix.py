'''
        transpose matrix in single line for loop
'''
print("=============================================")
print("Enter the size of the matrix:\n")
row = int(input("Enter Number of Rows:"))
col = int(input("Enter Number of columns:"))

#Creating a 2D Matrix and intialized that with 0
Matrix=[[0 for i in range(col)] for j in range(row)]

#Getting the user Input
print("\nEnter the Matrix elements One by one!!!\n")
for i in range(row):
    for j in range(col):
        #print("\nEnter the element for Matrix [",i," ][",j," ]:")
        Matrix[i][j]=int(input())

#This below line computing the transpose_Matrix
transpose_Matrix= [[Matrix[j][i] for j in range(len(Matrix))] for i in range(len(Matrix[0]))]

#Printing The old Matrix
print("\n\nYour Intial Matrix\n")
for r in Matrix:
  print(r)
print("\n")

print("Converted transpose_Matrix \n")
#printing The new transpose_Matrix
for r in transpose_Matrix:
  print(r)
  
'''
Reference from : http://www.geeksforgeeks.org/transpose-matrix-single-line-python/

'''
