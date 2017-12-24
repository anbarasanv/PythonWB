n = int(input().strip())
i=n
while(i>0):
    j=0
    while(j<n):
        if(j<i-1):
            print(" ",end='')
        else:
            print("#",end='')
        j+=1
    print('\n')
    i-=1

