a = {1, 2, 3} 
def power_set_finder(set_val):
    result = set()
    for x in range(len(set_val)+1):
        for i in it.combinations(set_val,x):
            result.add(i)
    return result
print(power_set_finder(a))
