from board import Board


def test_reset():
    b1 = Board()
    b2 = b1.reset()
    actual = b2
    expected = Board()
    assert actual == expected, 'reset should create a new board'


def test_row_winner():
    b1 = Board(['X', 'X', 'X', '-', '-', '-', '-', '-', '-'])
    actual = b1.isThereAWinnerFromRows()
    expected = True
    assert actual == expected, 'should return true when there is a win in a row'
