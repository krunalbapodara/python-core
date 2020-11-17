import itertools
import random

cards = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

print(cards)

random.shuffle(cards)

print('You got ')

for i in range(5):
    print(cards[i][0], 'of', cards[i][1])