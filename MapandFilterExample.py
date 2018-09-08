li = [1,2,4,5,6,6,7,8]
#Filter example
fli = list(filter(lambda x: x%2 == 0,li))
print(fli)
#map Example
mli = list(map(lambda x: x**2, li))
print(mli)
