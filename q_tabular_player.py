from player import Player
from board import Board
import pickle


class QTabularPlayer(Player):

    def __init__(self, symbol):
        super().__init__(symbol=symbol)
        self.qFileName = "QTabularPlayer.p"
        self.learned_q = pickle.load(open(self.qFileName, "rb"))
        self.learning_rate = .9
        self.discount_rate = .9
        self.epsilon = .3

    def make_move(self, board: Board) -> int:
        available_squares = board.openSquares()
        state: str = board.__hash__()
        if state in self.learned_q:
            learned_actions = self.learned_q[state]



        return available_squares[0]

    def save_qs(self):
        pickle.dump(self.learned_q, open(self.qFileName, "wb"))

