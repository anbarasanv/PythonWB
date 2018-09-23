inp = 'aaaxaaxbbbd'
lst = list(inp)
def popitems(lst):
    print('\n',lst)
    prev = lst[0]
    count = 0
    strlen = len(lst)
    for i in range(strlen):
        if(prev == lst[i]):
            count +=1
            if(count%2 == 0):
                lst.pop(i)
                lst.pop(i-1)
                print('Modified: ',lst)
                return popitems(lst)
        prev = lst[i]
    return lst
print(popitems(lst))
                
