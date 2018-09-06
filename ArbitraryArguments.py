#This Average function
def Averagefunc(*items):
    n = len(items)
    total = 0
    for x in items:
        total +=x
    return total/n
average = Averagefunc(1,1,1,1,1)
print(average)
