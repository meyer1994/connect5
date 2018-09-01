

class Board(object):
    def __init__(self, width, height):
        super(Board, self).__init__()
        self.width = width
        self.height = height
        self.board = [ 0 for _ in range(width * height) ]

    def row(self, i):
        '''
        Gets row from of board.
        '''
        start = i * self.width
        end = start + self.width
        return self.board[start:end]

    @property
    def rows(self):
        '''
        Iterator for all the rows in the board.
        '''
        for i in range(self.height):
            yield self.row(i)

    def col(self, i):
        '''
        Gets col of board.
        '''
        start = i
        end = (self.width * self.height)
        step = self.width
        return self.board[start:end:step]

    @property
    def cols(self):
        '''
        Iterator for all the cols in the board.
        '''
        for i in range(self.width):
            yield self.col(i)

    def ldiag(self, i):
        '''
        Returns the i-th left diagonal.

        Adapted from:
            https://stackoverflow.com/a/23069625/5092038

        A left diagonal is one that starts in the top-left and goes
        right-bottom. Note that the index count starts on the top-left.
        '''
        h = self.height
        w = self.width
        mx = max(i - h + 1, 0)
        mn = min(i + 1, w)
        return [ self.board[(i - q) * w + q] for q in range(mx, mn) ]

    def rdiag(self, i):
        '''
        Returns the i-th left diagonal.

        Adapted from:
            https://stackoverflow.com/a/23069625/5092038

        A right diagonal is one that starts in the top-right and goes
        left-bottom. Note that the index starts on the bottom-left.
        '''
        h = self.height
        w = self.width
        mx = max(i - h + 1, 0)
        mn = min(i + 1, w)
        board = [ self.board[(h - i + q - 1) * w + q] for q in range(mx, mn) ]
        return board[::-1]

    @property
    def diags(self):
        '''
        Simple iterator for all the diagonals.

        It starts with the right diagonals first and goes to the left ones.
        '''
        total = self.height + self.width - 1
        for i in range(total):
            yield self.rdiag(i)
        for i in range(total):
            yield self.ldiag(i)

    def get(self, x, y):
        '''
        Gets the play at the coordinate.

        Returns:
            1 for a player, -1 for the other, 0 for nothing.
        '''
        return self.board[y * self.width + x]

    def set(self, x, y, val):
        '''
        Set the val in the coordinate.
        '''
        self.board[y * self.width + x] = val

    def __str__(self):
        '''
        Returns string representation of board.

        Note that the representation follow the coordinate system where both
        minimum values of x and y are located in the lower left corner.
        '''
        rows = []
        for row in self.rows:
            line = ''.join( str(i) for i in row )
            line = line.replace('-1', 'O ')
            line = line.replace('0', '- ')
            line = line.replace('1', 'X ')
            line = line.strip()
            rows.append(line)
        return '\n'.join(rows[::-1])

    def __len__(self):
        return len(self.board)
