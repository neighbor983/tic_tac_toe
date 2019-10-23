from human_player import HumanPlayer

def test_set_symbol():
    human = HumanPlayer(symbol='-')
    human.set_symbol('X')
    actual = human.symbol
    expected = 'X'
    assert actual == expected, "set symbol should set the symbol"