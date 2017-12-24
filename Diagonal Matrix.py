#This code will return the absolute Differnce of sum of diagonals

#size of the square matrix
n = int(input().strip())
a = []

#Input: element of the square matrix
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
i=0
j=0
sum1=0
#calculating the sum of primary Diagonal
while(i<n):
    sum1+=a[i][j]
    j+=1
    i+=1

j=n-1
i=0
sum2=0
#calculating the sum of secondary Diagonal
while(i<n):
    sum2+=a[i][j]
    j-=1
    i+=1

#Output: Absolute difference of the Diagonals
print(abs(sum1-sum2))
