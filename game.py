from board import Board


class Game:
    winning_reward = 1
    tie_reward = .5

    def __init__(self, player_1, player_2, board=None):

        if board is None:
            self.board = Board()
        else:
            self.board = board.copy()

        self.player_1 = player_1
        self.player_2 = player_2
        self.message = ""

    def start(self):
        winner = None

        game_done = False
        while not game_done:
            move = self.player_1.make_move(board=self.board)
            # print(f'player one move: {move}')
            self.board = self.board.setSquare(move, self.player_1.symbol)
            game_done = self.board.isThereAWinner() or len(self.board.openSquares()) == 0
            if game_done:
                if not (self.board.whoIsWinner() == '-'):
                    winner = 'player1'
                break

            move = self.player_2.make_move(board=self.board)
            # print(f'player two move: {move}')

            self.board = self.board.setSquare(move, self.player_2.symbol)
            game_done = self.board.isThereAWinner() or len(self.board.openSquares()) == 0
            if game_done:
                if not (self.board.whoIsWinner() == '-'):
                    winner = 'player2'
                break

            # print(self.board)

        # print(self.board)

        if winner == 'player1':
            # print(f'player 1 wins')
            # print(f'player one reward update')
            self.player_1.update_reward(self.winning_reward)
            # print(f'player two reward update')
            self.player_2.update_reward(0)

        if winner == 'player2':
            # print(f'player 2 wins')
            # print(f'player one reward update')
            self.player_1.update_reward(0)
            # print(f'player two reward update')
            self.player_2.update_reward(self.winning_reward)

        if winner == None:
            # print(f'tie')
            # print(f'player one reward update')
            self.player_1.update_reward(self.tie_reward)
            # print(f'player two reward update')
            self.player_2.update_reward(self.tie_reward)
