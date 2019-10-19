class Board:
    def __init__(self, state=None):
        if state is None:
            self.state = ['-', '-', '-',
                          '-', '-', '-',
                          '-', '-', '-']
        else:
            self.state = state.copy()

    def __repr__(self):
        return f' {self.state[0]} | {self.state[1]} | {self.state[2]} \n' \
               f'- - - - - - \n' \
               f' {self.state[3]} | {self.state[4]} | {self.state[5]} \n' \
               f'- - - - - - \n' \
               f' {self.state[6]} | {self.state[7]} | {self.state[8]} \n'

    def __hash__(self):
        return ''.join(self.state)

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.state == other.state)

    def isThereAWinner(self):
        return self.isThereAWinnerFromRows() or self.isThereAWinnerFromCols() or self.isThereAWinnerFromDiagonals()

    def isThereAWinnerFromRows(self):
        return (self.state[0] != '-' and self.state[0] == self.state[1] and self.state[1] == self.state[2]) or \
               (self.state[3] != '-' and self.state[3] == self.state[4] and self.state[4] == self.state[5]) or \
               (self.state[6] != '-' and self.state[6] == self.state[7] and self.state[7] == self.state[8])

    def isThereAWinnerFromCols(self):
        return (self.state[0] != '-' and self.state[0] == self.state[3] and self.state[3] == self.state[6]) or \
               (self.state[1] != '-' and self.state[1] == self.state[4] and self.state[4] == self.state[7]) or \
               (self.state[2] != '-' and self.state[2] == self.state[5] and self.state[5] == self.state[8])

    def isThereAWinnerFromDiagonals(self):
        return (self.state[0] != '-' and self.state[0] == self.state[4] and self.state[4] == self.state[8]) or \
               (self.state[2] != '-' and self.state[2] == self.state[4] and self.state[4] == self.state[6])

    def openSquares(self):
        return [i for i, x in enumerate(self.state) if x == '-']

    def setSquare(self, location: int, value: str):
        new_state = self.state.copy()
        new_state[location] = value
        return Board(state=new_state)

    def reset(self):
        return Board(state=None)
