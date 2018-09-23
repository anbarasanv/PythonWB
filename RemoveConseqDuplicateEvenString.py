inp = 'aaabbabbbccbc'
lst = list(inp)
def popitems(lst):
    print('\n',lst)
    prev = lst[0]
    count = 0
    strlen = len(lst)
    for i in range(strlen):
        if(prev == lst[i]):
            count +=1
            if(i==strlen-1):
                if(count%2 == 0):
                    j = i
                    while(count > 0):
                        lst.pop(j)
                        count -=1
                        j -=1                
        else:
            if(count%2 == 0):
                j = i
                while(count > 0):
                    lst.pop(j-1)
                    count -=1
                    j -=1
                return popitems(lst)
            count = 1
        if(i<len(lst)):
            prev = lst[i]
    return lst
print('\n final list',popitems(lst))
                
