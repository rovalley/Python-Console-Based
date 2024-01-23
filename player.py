'''
NAME
    player

DESCRIPTION
    This module provides a class to represent a player in a game of gofish.

@author: ryan_ovalley
'''


class Player:
    '''
    Constructor
    '''
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.completed_set = []

    '''
    add a card method
    '''
    def add_card(self, card):
        # add card to hand
        self.hand.append(card)

    '''
    remove a card method
    '''
    def remove_cards(self, rank):
        # create give array
        give = []
        # loop through your hand
        for card in self.hand:
            # if the rank matches
            if card.rank == rank:
                # add card to give array
                give.append(card)
        # loop through give array
        for card in give:
            # remove card from hand
            self.hand.remove(card)
        return give

    '''
    check for a completed set method
    '''
    def check_for_complete_rank(self):
        # create rank count dictionary
        rank_count = {
            "A": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "J": 0,
            "Q": 0,
            "K": 0
        }
        # loop through hand
        for card in self.hand:
            # add 1 to the rank
            rank_count[card.rank] += 1
        # loop through rank count
        for rank in rank_count:
            # set count to rank
            count = rank_count[rank]
            # if count equals 4
            if count == 4:
                # add rank to completed set
                self.completed_set.append(rank)
                # remove rank
                self.remove_cards(rank)
                # display completed set with the rank
                print(f"Completed a set: {rank}")

    '''
    ask for a card method
    '''
    def ask_for_card(self):
        while True:
            # ask user to enter a rank
            rank = input("Please enter a rank: ")
            # only allow uppercase letters
            rank = rank.upper()
            # validate rank for only these inputs
            if rank not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                # display error message
                print("Invalid rank try again")
                # display hand
                self.display_hand()
            else:
                break
        return rank

    '''
    display hand method
    '''
    def display_hand(self):
        # loop through hand
        for card in self.hand:
            # print card
            print(card, end=" ")
        print()

    '''
    check if you have cards method
    '''
    def has_cards(self):
        # if hand is equal to 0 return false
        if len(self.hand) == 0:
            return False
        else:
            return True

    '''
    display score method
    '''
    def display_score(self):
        # display name with the score
        print(f"{self.name}'s score: {len(self.completed_set)} ")

    '''
    get score method
    '''
    def get_score(self):
        # return score
        return len(self.completed_set)
