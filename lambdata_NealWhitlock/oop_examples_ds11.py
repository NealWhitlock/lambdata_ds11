"""
Classes to represent games.
"""
from random import random

class Game:
    """
    General representation of an abstract game
    """
    fun_level = 5
    def __init__(self, rounds=2, player1='Mathias', player2='Daniel'): # initializes a version of this class
        self.rounds = 2             # These become the default
        self.current_round = 0      # values unless they are
        self.player1 = player1      # specifically changed
        self.player2 = player2      # later on.

    def print_players(self):
        """
        Print game players
        """
        print('{} is playing {}.'.format(self.player1, self.player2))

    def add_rounds(self):
        """
        Increment rounds by 1
        """
        self.rounds += 1

    def winner(self):
        """
        Pick a winner
        """
        return self.player1 if random() > 0.5 else self.player2

class Tic(Game):
    """
    TicTacToe subclass of Game
    """
    
    def __init__(self, rounds=3, player1='Mike', player2='Emma'):
        super().__init__(rounds, player1, player2)

    def print_players(self):
        print(f"{self.player1} is playing TIC TAC TOEwith {self.player2}")