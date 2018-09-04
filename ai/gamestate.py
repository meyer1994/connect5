from copy import deepcopy

class GameState(object):
    def __init__(self, board, over):
        super(GameState, self).__init__()
        self.board = board
        self.over = over

    def next(self, x, y, val):
        '''
        Creates a copy of the state, apply the play to this copy and returns it.
        '''
        copy = deepcopy(self)
        copy.board.set(x, y, val)
        copy.over = copy._is_over(x, y)
        return copy

    def _is_over(self, x, y):
        '''
        Checks if the inputted piece won the game.

        It is called every time a piece is placed in the board.

        Returns:
            True if the piece won the game. False otherwise.
        '''
        # this values are checked for the board borders
        max_x = min(x + 5, self.board.width)
        min_x = max(x - 5, 0)
        max_y = min(y + 5, self.board.height)
        min_y = max(y - 5, 0)

        row = self.board.row(y)[min_x:max_x]
        if self._is_winner(row):
            return True

        col = self.board.col(x)[min_y:max_y]
        if self._is_winner(col):
            return True

        ldiag = self.board.ldiag(x + y)
        if len(ldiag) >= 5 and self._is_winner(ldiag):
            return True

        rdiag = self.board.rdiag(x + self.board.height - 1 - y)
        if len(rdiag) >= 5 and self._is_winner(rdiag):
            return True

        return False

    def _is_winner(self, line):
        '''
        Checks if line is the winning one.

        A line is a winning one if the sum of all its values equals to 5 or -5.

        Args:
            List representing the line.

        Returns:
            True if the line has the winning line. False otherwise.
        '''
        lines = len(line) - 4
        for i in range(lines):
            sub_line = line[i:i+5]
            line_sum = sum(sub_line)
            if abs(line_sum) == 5:
                return True
        return False

    @property
    def moves(self):
        '''
        Returns an iterator of possible moves.

        Every space of the board that is not 1 or -1 is considered a possible
        move.
        '''
        for i, v in enumerate(self.board):
            if v == 0:
                x = i % self.board.width
                y = i // self.board.width
                yield (x, y)

    def __eq__(self, g):
        return self.board == g.board and self.over == g.over
