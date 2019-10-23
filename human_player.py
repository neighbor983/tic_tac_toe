from player import Player
from board import Board

from typing import List


class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol=symbol)

    def make_move(self, board: Board) -> int:
        available_squares = board.openSquares()
        while True:
            selected_value = get_selected_value(available_squares=available_squares)

            try:

                while True:

                    int_selected_value = int(selected_value)

                    if int_selected_value in available_squares:
                        return int_selected_value
                    else:
                        print("Error!, you did not select an open square, Please try again.")

                    selected_value = get_selected_value(available_squares=available_squares)

            except ValueError:
                print("Error!, you did not input an integer. Please try again.")
            else:
                break
        return int_selected_value

    def set_symbol(self, symbol):
        self.symbol = symbol


def get_selected_value(available_squares: List[int]):
    return input(
        "Select an open square from the following choices " + ','.join(
            [str(x) for x in available_squares]) + " :")
