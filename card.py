'''
NAME
    card

DESCRIPTION
    This module provides a simple class for a playing card.

Created on January 19, 2024

@author: ryan_ovalley
'''


class Card:
    '''
    Constructor
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    '''
    display rank and suit method
    '''
    def __str__(self):
        # display card rank and suit
        return f"{self.rank}{self.suit}"
