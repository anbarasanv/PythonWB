import itertools
import random as rand
#Below line creates a card deck.
deck = list(itertools.product(range(2,11),['Spade','Heart','Diamond','Club']))+list(itertools.product(['A','J','Q','K'],['Spade','Heart','Diamond','Club']))
#The below line Shuffles the card deck.
rand.shuffle(deck)
#The below line creating four players.
p1,p2,p3,p4 = [],[],[],[]
#from the below loop we are spliting the card among 4.
for item in deck:
    if(len(p1)<13):
        p1.append(item)
    elif(len(p2)<13):
        p2.append(item)
    elif(len(p3)<13):
        p3.append(item)
    else:
        p4.append(item)
print(p1,p2,p3,p4)
