from player import Player
from board import Board
import pickle
import random


class QTabularPlayer(Player):
    learning_rate = .9
    discount_rate = .9
    epsilon = .3

    def __init__(self, symbol):
        super().__init__(symbol=symbol)
        self.qFileName = "QTabularPlayer.p"
        with open(self.qFileName, 'rb') as file:
            self.learned_q = pickle.load(file)
        self.state_action_pairs = []

    def make_move(self, board: Board, epsilon: float = 0.3) -> int:
        ran = random.random()
        available_squares = board.openSquares()
        state: str = board.__hash__()
        player_state = ''.join(self.convert_board_for_player_view(state, self.symbol))

        if epsilon > ran:
            action = random.choice(available_squares)

            self.state_action_pairs.append((player_state, action))
            # print(f'state action pairs: {self.state_action_pairs}')
            return action

        action_values = self.learned_q[player_state]
        action = action_values.index(max(action_values))
        self.state_action_pairs.append((player_state, action))
        return action

    def save_qs(self):
        pickle.dump(self.learned_q, open(self.qFileName, "wb"))

    def convert_board_for_player_view(self, board, symbol):
        state = board
        # print(f'state: {state}')
        return [self.convert_str_to_player_value(x, symbol) for x in state]

    def convert_str_to_player_value(self, string, symbol):
        if string == '-':
            return '0'
        elif string == symbol:
            return '1'
        else:
            return '-1'

    def update_reward(self, reward):
        last_state, last_action = self.state_action_pairs.pop()
        # last_state = ''.join(last_state)
        # print(f'last state: {last_state} , last action: {last_action}')
        current_q = self.learned_q[last_state][last_action]
        new_q = (1 - self.learning_rate) * current_q + self.learning_rate * reward
        # print(f'new_q: {new_q}')
        self.learned_q[last_state][last_action] = new_q

        for q in reversed(self.state_action_pairs):
            # print(f'q: {q}')
            current_state, current_action = q
            current_q = self.learned_q[current_state][current_action]

            actions = self.learned_q[last_state]
            max_q = max(actions)
            # print(f'max_q: {max_q}')

            new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (self.discount_rate * max_q)
            # print(f'new_q: {new_q}')
            self.learned_q[current_state][current_action] = new_q

            last_state, last_action = current_state, current_action

        self.save_qs
