from board import Board


def test_reset():
    b1 = Board()
    b2 = b1.reset()
    actual = b2
    expected = Board()
    assert actual == expected, 'reset should create a new board'


def test_row_winner_true():
    b1 = Board(['X', 'X', 'X', '-', '-', '-', '-', '-', '-'])
    actual = b1.isThereAWinnerFromRows()
    expected = True
    assert actual == expected, 'should return true when there is a win in a row'


def test_row_winner_false():
    b1 = Board(['X', '-', 'X', '-', '-', '-', '-', '-', '-'])
    actual = b1.isThereAWinnerFromRows()
    expected = False
    assert actual == expected, 'should return false when there is not a win in a row'


def test_col_winner_true():
    b1 = Board(['X', '-', '-', 'X', '-', '-', 'X', '-', '-'])
    actual = b1.isThereAWinnerFromCols()
    expected = True
    assert actual == expected, 'should return true when there is a win in a col'


def test_row_winner_false():
    b1 = Board(['X', '-', 'X', '-', '-', '-', '-', '-', '-'])
    actual = b1.isThereAWinnerFromCols()
    expected = False
    assert actual == expected, 'should return false when there is not a win in a col'


def test_diagonal_winner_true():
    b1 = Board(['X', '-', '-', '-', 'X', '-', '-', '-', 'X'])
    actual = b1.isThereAWinnerFromDiagonals()
    expected = True
    assert actual == expected, 'should return true when there is a win in a diagonal'


def test_diagonal_winner_false():
    b1 = Board(['X', '-', 'X', '-', '-', '-', '-', '-', '-'])
    actual = b1.isThereAWinnerFromDiagonals()
    expected = False
    assert actual == expected, 'should return false when there is not win in a diagonal'


def test_winner_true():
    b1 = Board(['X', '-', '-', '-', 'X', '-', '-', '-', 'X'])
    actual = b1.isThereAWinner()
    expected = True
    assert actual == expected, 'should return true when there is a win on the board'


def test_winner_false():
    b1 = Board(['X', '-', 'X', '-', '-', '-', '-', '-', '-'])
    actual = b1.isThereAWinner()
    expected = False
    assert actual == expected, 'should return false when there is not win on the board'


def test_whoIsWinner_no_winner():
    b1 = Board(['X', '-', 'X', '-', '-', '-', '-', '-', '-'])
    actual = b1.whoIsWinner()
    expected = '-'
    assert actual == expected, 'should return - when there is no winner'


def test_whoIsWinner_X():
    b1 = Board(['X', 'X', 'X', '-', '-', '-', '-', '-', '-'])
    actual = b1.whoIsWinner()
    expected = 'X'
    assert actual == expected, 'should return X when X player is the winner'
