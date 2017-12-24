# 0 1 1 2 3 5 ....
def fib():
    i,j=0,1

    while(True):

        yield i
        tmp=i+j
        i=j
        j=tmp

if __name__ == '__main__':
    n=int(input("Enter how may number of fibonacci required: "))
    for num in fib():
        if num > n:
            break
        print(num,end=" ")
