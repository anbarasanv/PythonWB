import itertools
import random as rand
n = list(itertools.product(range(2,11),['Spade','Heart','Diamond','Club']))+list(itertools.product(['A','J','Q','K'],['Spade','Heart','Diamond','Club']))
rand.shuffle(n)
p1 = []
p2 = []
p3 = []
p4 = []
for item in n:
    if(len(p1)<13):
        p1.append(item)
    elif(len(p2)<13):
        p2.append(item)
    elif(len(p3)<13):
        p3.append(item)
    else:
        p4.append(item)
print(p1,p2,p3,p4)
