def fib(limit):
    #Initializing Initial values
    a,b = 0,1

    #generating the Next values

    for i in range(limit):
        #returning values
        yield a
        a,b=b,a+b
if __name__ == '__main__':
    x=int(input("Enter the number of fibonacii numbers required: "))
    for i in fib(x):
        print(i)

