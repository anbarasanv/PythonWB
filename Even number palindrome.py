from itertools import product
def Even_palindrom():
    inp = int(input("Please Enter a number: "))
    lst = ['1','2']
    count = 2
    i = 0
    while(True):
        l = [lst]*count
        permutations = [list(i) for i in list(product(*l))]
        for p in permutations:
            num = ''.join(p)
            reverse = ''.join(list(reversed(list(num))))
            if(num == reverse):
                i +=1
                if(i == inp):
                    return int(num)              
        count += 2

result = Even_palindrom()
print("Result: ",result)
