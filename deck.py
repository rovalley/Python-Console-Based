'''
NAME
    deck

DESCRIPTION
    This module provides a simple class for a deck of playing cards.

Created on January 19, 2024

@author: ryan_ovalley
'''

from card import Card
import random


class Deck:

    '''
    Constructor
    '''
    def __init__(self):
        # create an array of cards
        self.cards = []
        #loop through the deck
        for suit in ['C', 'S', 'D', 'H']:
            for rank in range(1, 14):
                # assign specific numbers to a letter rank
                if rank == 1:
                    card = Card(suit, "A")
                elif rank == 11:
                    card = Card(suit, "J")
                elif rank == 12:
                    card = Card(suit, "Q")
                elif rank == 13:
                    card = Card(suit, "K")
                else:
                    card = Card(suit, str(rank))
                # add cards to array
                self.cards.append(card)
        # shuffle the cards
        self.shuffle()

    '''
    shuffle cards method
    '''
    def shuffle(self):
        #shuffle cards
        random.shuffle(self.cards)

    '''
    draw a single card method
    '''
    def draw(self):
        # draw the top card
        if len(self.cards) == 0:
            return None
        card = self.cards.pop()
        return card

    '''
    Check a player's card method
    '''
    def has_cards(self):
        # check if they have a certain card
        if len(self.cards) == 0:
            return False
        else:
            return True
