#The below code will identify the number of zeros, positive and negative numbers and fractions of those with size of array
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
negative,positive,zero=0,0,0
for i in arr:
    if(i<0):
        negative+=1
    elif(i>0):
        positive+=1
    elif(i==0):
        zero+=1
frn=round(negative/n,6)
frp=round(positive/n,6)
frz=round(zero/n,6)

print(frp)
print(frn)
print(frz)