

class Board(object):
    '''
    Holds the representation of the game board.

    The board consists of one single string.

    Attributes:
        board: string representing the board.
        width: width of the board.
        height: height of the board.
    '''

    def __init__(self, width, height):
        '''
        Constructor.

        Attributes:
            width: width of the board.
            height: height of the board.
        '''
        super(Board, self).__init__()
        self.board = '-' * (width * height)
        self.width = width
        self.height = height

    def row(self, i):
        '''
        Returns the ith row of the board.
        '''
        start = i * self.width
        end = start + self.width
        return self.board[start:end]

    @property
    def rows(self):
        '''
        Generator for all rows of board.
        '''
        for i in range(self.height):
            yield self.row(i)

    def col(self, i):
        '''
        Returns the ith column of the board.
        '''
        start = i
        end = (self.width * self.height)
        step = self.width
        return self.board[start:end:step]

    @property
    def cols(self):
        '''
        Generator for all columns of board.
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
        gen = ( self.board[(i - q) * w + q] for q in range(mx, mn) )
        return ''.join(gen)

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
        gen = ( self.board[(h - i + q - 1) * w + q] for q in range(mx, mn) )
        return ''.join(gen)

    @property
    def diags(self):
        '''
        Generator for all the diagonals.

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
            X for a player, O for the other player, - for nothing.
        '''
        return self.board[y * self.width + x]

    def set(self, x, y, val):
        '''
        Set the value in the coordinate.
        '''
        s = y * self.width + x
        self.board = self.board[:s] + val.upper() + self.board[s + 1:]

    def __str__(self):
        '''
        Returns string representation of board.

        Note that the representation follow the coordinate system where both
        minimum values of x and y are located in the lower left corner.
        '''
        rows = []
        for row in self.rows:
            line = ' '.join( str(i) for i in row )
            line = line.strip()
            rows.append(line)
        return '\n'.join(rows[::-1])

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.board)

    def __eq__(self, b):
        return self.board == b.board

    def __hash__(self):
        '''
        Used in memoization.
        '''
        return hash(self.board)
