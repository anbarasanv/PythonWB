x = [1,2,3,[4,5,6,[7,8,[9,10]]],11]
result = []
def decursive(x):
    for i in x:
        if type(i)==list:
            decursive(i)
        else:
            result.append(i)
    return result
    
print(decursive(x))
