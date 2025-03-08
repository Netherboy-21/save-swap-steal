import random
from card import Card

class Deck():
    def __init__(self):
        """ Construct the deck """

        self.cards = []
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank,suit))

        self.shuffle()

    def shuffle(self):
        """ Shuffle the deck"""

        random.shuffle(self.cards)
        
    def draw(self):
        """ Remove the top card from the deck and return it """

        return self.cards.pop(0)