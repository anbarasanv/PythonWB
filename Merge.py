#Merge function declartion
def Merge(a,b,c,n,m):
    i,j,k = 0,0,0
    #Comparing Both list
    while i<n and j<m:
        if a[i] < b[j]:
            c[k] = a[i]
            k+=1
            i+=1
        else:
            c[k] = b[j]
            k+=1
            j+=1
    #Elements those are not compared will be copied Here
    for r in range(i,n):
        c[k] = a[i]
        k+=1
        i+=1
    for r in range(j,m):
        c[k] = b[j]
        k+=1
        j+=1
    print(c)


#Variable declaration
a = [int(x) for x in input("Enter the first list: ").split(' ')]
b = [int(x) for x in input("Enter the second list: ").split(' ')]

#Calculation length of the new list
n = len(a)
m = len(b)

#Creating new list with the size of total length 
c = [None for i in range(n+m)]

# Calling Merge function
Merge(a,b,c,n,m)
