import random
import math
#Fisher–Yates shuffle Algorithm
#Initializing an array list
arr = []
#getting user input
arr = [int(x) for x in input("Enter the input:\n").split()]
length = len(arr) -1
print("Input array :",arr,"length of the array :",len(arr))

for i in range(length,0,-1):
    pic=math.floor((i+1)*random.random())
    temp=arr[i]
    arr[i]=arr[pic]
    arr[pic]=temp
    length-=1

print("shuffled  array :",arr,"length of the array :",len(arr))





