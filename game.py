from board import Board


class Game:
    def __init__(self, player_1, player_2, board=None):

        if board is None:
            self.board = Board()
        else:
            self.board = board.copy()

        self.player_1 = player_1
        self.player_2 = player_2
        self.message = ""
        self.players_turn = player_1


