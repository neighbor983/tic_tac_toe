from board import Board
from human_player import HumanPlayer
import random
import pickle
from q_tabular_player import QTabularPlayer
from game import Game
from collections import Counter


# sample_board = ['-', 'X', '-', '-', '-', '-', '-', '-', '-']
#
# b1 = Board(sample_board)
#
# print(b1)
# print(b1.openSquares())
#
# b2 = b1.reset()
#
# print(b2)
# b3 = b2.setSquare(location=1, value='X')
# print(b3)
#
# print(b1 == b3)
#
# b4 = Board(['X', 'X', 'X', '-', '-', '-', '-', '-', '-'])
#
# print(b4.isThereAWinner())
# print(b4.isThereAWinnerFromRows())
# print(b4.isThereAWinnerFromCols())
# print(b4.isThereAWinnerFromDiagonals())
#
# human = HumanPlayer()
# human.make_move(b1)
def create_q_table_pickle_file(filename):
    possible_values = [-1, 0, 1]
    q_dicts = {}

    for a in range(len(possible_values)):
        a1 = possible_values[a]
        for b in range(len(possible_values)):
            b1 = possible_values[b]
            for c in range(len(possible_values)):
                c1 = possible_values[c]
                for d in range(len(possible_values)):
                    d1 = possible_values[d]
                    for e in range(len(possible_values)):
                        e1 = possible_values[e]
                        for f in range(len(possible_values)):
                            f1 = possible_values[f]
                            for g in range(len(possible_values)):
                                g1 = possible_values[g]
                                for h in range(len(possible_values)):
                                    h1 = possible_values[h]
                                    for i in range(len(possible_values)):
                                        i1 = possible_values[i]
                                        key_array = [str(a1), str(b1), str(c1), str(d1), str(e1), str(f1), str(g1), str(
                                            h1), str(i1)]
                                        key = str(a1) + str(b1) + str(c1) + str(d1) + str(e1) + str(f1) + str(g1) + str(
                                            h1) + str(i1)

                                        freq_map = Counter(key_array)
                                        ones = freq_map['1']
                                        minus_ones = freq_map['-1']
                                        if abs(int(ones) - int(minus_ones)) > 1:
                                            continue

                                        actions = []
                                        if a1 == 0:
                                            actions.append(0)
                                        else:
                                            actions.append(-1)

                                        if b1 == 0:
                                            actions.append(0)
                                        else:
                                            actions.append(-1)

                                        if c1 == 0:
                                            actions.append(0)
                                        else:
                                            actions.append(-1)

                                        if d1 == 0:
                                            actions.append(0)
                                        else:
                                            actions.append(-1)

                                        if e1 == 0:
                                            actions.append(0)
                                        else:
                                            actions.append(-1)

                                        if f1 == 0:
                                            actions.append(0)
                                        else:
                                            actions.append(-1)

                                        if g1 == 0:
                                            actions.append(0)
                                        else:
                                            actions.append(-1)

                                        if h1 == 0:
                                            actions.append(0)
                                        else:
                                            actions.append(-1)

                                        if i1 == 0:
                                            actions.append(0)
                                        else:
                                            actions.append(-1)

                                        q_dicts[key] = actions

    with open(filename, 'wb') as f:
        pickle.dump(q_dicts, f)


q_pickle_filename = 'QTabularPlayer.p'

# create_q_table_pickle_file(q_pickle_filename)

# with open(q_pickle_filename, 'rb') as file:
#     data = pickle.load(file)
#
# #
# # #q_table = pickle.load(open(q_pickle_filename))
# empty_board = '000000000'
# actions_array = data[empty_board]
# print(','.join([str(x) for x in actions_array]))
#
# full_board = '111111111'
# actions_array = data[full_board]
# print(','.join([str(x) for x in actions_array]))
#
# full_board = '-11-110001-1'
# actions_array = data[full_board]
# print(','.join([str(x) for x in actions_array]))


for _ in range(10):

    p1 = QTabularPlayer(symbol='X')
    p2 = QTabularPlayer(symbol='O')

    g = Game(player_1=p1, player_2=p2)

    g.start()


# p1 = HumanPlayer(symbol='X')
# p2 = QTabularPlayer(symbol='O')
#
# g = Game(player_1=p1, player_2=p2)
# g.start()
# p1 = QTabularPlayer(symbol='X')
# del p1.learned_q['111110110']
# del p1.learned_q['111110111']
# del p1.learned_q['111111-1-1-1']
#
#
# p1.save_qs()
# p2 = QTabularPlayer(symbol='X')
# print(f'qs: {p2.learned_q}')
print(f'q table: {p1.learned_q}')
