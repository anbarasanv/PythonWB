import itertools
import operator

l1 = [2,4,8,7,5]
l2 = [6,7,8,9,10]
l3 = [11,23,4,56,34]
l4 = [(2,4,5),(5,6,7),(8,6,8)]

# print("Print sum:",end=" ")
# print(list(itertools.accumulate(l1)))
# print(list(itertools.accumulate(l1,operator.mul)))
# print(l4)
# print(list(itertools.dropwhile(lambda x: x%2==0,l1)))
# print(list(itertools.filterfalse(lambda x: x%2==0,l3)))


print(list(itertools.starmap(min,l4)))