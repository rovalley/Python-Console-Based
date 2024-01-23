'''
NAME
    gofish

DESCRIPTION
    This module lets you play a game of gofish.

Created on January 19, 2024

@author: ryan_ovalley
'''

from deck import Deck
from player import Player


def play_game():
    # create deck
    deck = Deck()
    # create players
    player = Player("John")
    player2 = Player("Sam")
    # deal out cards to players
    for i in range(7):
        card = deck.draw()
        player.add_card(card)
        card = deck.draw()
        player2.add_card(card)
    current_player = player
    other_player = player2
    # continue game until deck runs out or a player runs out of cards
    while deck.has_cards() and player.has_cards() and player2.has_cards():
        # display whose turn it is
        print(f"{current_player.name}'s turn")
        # display hand
        current_player.display_hand()
        # ask other player for a rank
        rank = current_player.ask_for_card()
        # remove other player's card
        received_cards = other_player.remove_cards(rank)

        go_again = False
        # receive other players card
        if len(received_cards) > 0:
            for card in received_cards:
                current_player.add_card(card)
            print(f"received {len(received_cards)} cards")
            go_again = True
        else:
            card = deck.draw()
            current_player.add_card(card)
            print("Go Fish!")
        # check for a set of 4 cards
        current_player.check_for_complete_rank()
        # display players score
        player.display_score()
        player2.display_score()
        # change to other players turn
        if not go_again:
            temp = current_player
            current_player = other_player
            other_player = temp

        print()
    # display who won the game of go fish
    if player.get_score() > player2.get_score():
        print(f"{player.name} wins!")
    elif player2.get_score() > player.get_score():
        print(f"{player2.name} wins!")
    else:
        print(f"Tie game.")


if __name__ == "__main__":
    play_game()
