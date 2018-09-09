import math

from copy import deepcopy

from ai.board import Board

class GameState(object):
    def __init__(self, board, over):
        super(GameState, self).__init__()
        self.board = board
        self.over = over
        self.plays = len(self.board) - self.board.board.count('-')
        self.last = (-1, -1)

    def next(self, x, y, val):
        '''
        Creates a copy of the state, apply the play to this copy and returns it.
        '''

        copy = deepcopy(self)

        place = copy.board.get(x, y)
        if place == '-' and val != '-':
            copy.plays += 1
        if place != '-' and val == '-':
            copy.plays -= 1

        copy.board.set(x, y, val)
        copy.last = (x, y)
        copy.over = copy.over or copy._is_over(x, y)

        return copy

    def _is_over(self, x, y):
        '''
        Checks if the inputted piece finished the game.

        It is called every time a piece is placed in the board.

        Returns:
            True if the piece finished the game. False otherwise.
        '''
        # this values are checked for the board borders
        max_x = min(x + 5, self.board.width)
        min_x = max(x - 5, 0)
        max_y = min(y + 5, self.board.height)
        min_y = max(y - 5, 0)

        if self.plays == len(self.board):
            return True

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
            if sub_line == 'X' * 5 or sub_line == 'O' * 5:
                return True
        return False

    @property
    def moves(self):
        '''
        Returns an iterator of possible moves.

        Every space of the board that is not 1 or -1 is considered a possible
        move.
        '''
        for x, y in self._iter():
            if self.board.get(x, y) == '-':
                yield (x, y)

    def _iter(self):
        order = int(math.sqrt(len(self.board)))

        cycles = order // 2

        if order % 2 == 1:
            yield (cycles, cycles)
            calc_n = lambda i: i * 2 + 2
            calc_c = lambda i : cycles + 1 + i
        else:
            calc_c = lambda i : cycles + i
            calc_n = lambda i: i * 2 + 1

        for i in range(cycles):
            x = calc_c(i)
            y = calc_c(i)

            n = calc_n(i)

            # left
            for _ in range(n):
                yield (x, y)
                x -= 1

            # down
            for _ in range(n):
                yield (x, y)
                y -= 1

            # right
            for _ in range(n):
                yield (x, y)
                x += 1

            # up
            for _ in range(n):
                yield (x, y)
                y += 1

    def sub_board(self, x, y, m=7):
        q = m // 2
        # get max and min values
        w = self.board.width
        h = self.board.height
        max_x = min(w, x + q + 1)
        max_y = min(h, y + q + 1)
        min_x = max(0, x - q - 1)
        min_y = max(0, y - q - 1)

        # threat borders of board
        if min_x == 0:
            max_x = m
        if min_y == 0:
            max_y = m

        if max_x == w:
            min_x = w - m
        if max_y == h:
            min_y = h - m

        # get rows of sub board
        rows = ( self.board.row(i) for i in range(min_y, max_y) )
        # filter the right cols from the rows
        sub_rows = ( row[min_x:max_x] for row in rows )

        board = Board(max_x - min_x, max_y - min_y)
        board.board =''.join(sub_rows)

        return board

    def __str__(self):
        return str(self.board)

    def __eq__(self, g):
        board = self.board == g.board
        over = self.over == g.over
        plays = self.plays == g.plays
        return board and over and plays

    def __hash__(self):
        return hash(self.board.board)
