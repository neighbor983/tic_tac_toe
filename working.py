from board import Board

sample_board = ['-', 'X', '-', '-', '-', '-', '-', '-', '-']

b1 = Board(sample_board)

print(b1)
print(b1.openSquares())

b2 = b1.reset()

print(b2)
b3 = b2.setSquare(location=1, value='X')
print(b3)

print(b1 == b3)

b4 = Board(['X', 'X', 'X', '-', '-', '-', '-', '-', '-'])

print(b4.isThereAWinner())
print(b4.isThereAWinnerFromRows())
print(b4.isThereAWinnerFromCols())
print(b4.isThereAWinnerFromDiagonals())