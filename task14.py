"""Create a deck of cards class. Internally, the deck of cards should use another class, a card class.
Your requirements are:
The Deck class should have a deal method to deal a single card from the deck
After a card is dealt, it is removed from the deck.
There should be a "mix" method which makes sure the deck of cards has all 52 cards and then
rearranges them randomly.
Класс карты должен иметь масть (червы, бубны, трефы, пики) и ценность (A,
2,3,4,5,6,7,8,9,10, J, Q, K)"""


from random import shuffle
import random

class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val
    def show(self):
        print('{}  {}'.format(self.value,self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ['Червы','Бубны','Трефы','Пики']:
            for v in [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K','A']:
                self.cards.append(Card(s,v))

    def show(self):
        for x in self.cards:
            x.show()
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r], self.cards[i]

deck = Deck()
deck.shuffle()
deck.show()