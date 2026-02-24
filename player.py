from abc import ABC, abstractmethod
import random


class Player(ABC):
    def __init__(self, symbol):
        self._symbol = symbol

    @abstractmethod
    def make_move(self, board):
        pass

    def get_symbol(self):
        return self._symbol


class HumanPlayer(Player):
    def make_move(self, board):
        move = input(f"Gracz {self._symbol}, podaj pole (1-9): ")
        return int(move) - 1


class AIPlayer(Player):
    def make_move(self, board):
        free_fields = [i for i, field in enumerate(board) if field == " "]
        return random.choice(free_fields)
