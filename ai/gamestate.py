
from copy import deepcopy

class GameState(object):
    def __init__(self, board, over):
        super(GameState, self).__init__()
        self.board = board
        self.over = over

    def next(self, x, y, val):
        copy = deepcopy(self)
        copy.board.set(x, y, val)
        copy.over = copy._is_over(x, y)
        return copy

    def _is_over(self, x, y):
        max_x = max(x + 4, self.board.width - 1)
        min_x = min(x - 4, 0)
        max_y = max(y + 4, self.board.height - 1)
        min_y = min(y - 4, 0)
        max_d = max(max_x, max_y)
        min_d = min(min_x, min_y)

        row = self.board.row(y)[min_x:max_x]
        col = self.board.col(x)[min_y:max_y]
        ldiag = self.board.ldiag(x + y)
        rdiag = self.board.rdiag(x + self.board.height - 1 - y)

    @property
    def moves(self):
        for i, v in enumerate(self.board):
            if v == 0:
                x = i % self.board.width
                y = i // self.board.width
                yield (x, y)

    def __eq__(self, g):
        return self.board == g.board and self.over == g.over

