import functools

from itertools import product, chain
from collections import defaultdict


ONLY_X = { ''.join(k): 3**k.count('X') for k in product('X-', repeat=5) }
ONLY_X['XXXXX'] = 3**14
del ONLY_X['-----']

ONLY_O = { ''.join(k): -3**k.count('O') for k in product('O-', repeat=5) }
ONLY_O['OOOOO'] = -3**14
del ONLY_O['-----']

VALUE_TABLE = defaultdict(lambda: 0)
VALUE_TABLE.update(ONLY_X)
VALUE_TABLE.update(ONLY_O)
VALUE_TABLE['-----'] = 0


SUB_BOARD_SIZE = 7


def evaluate_line(line):
    return VALUE_TABLE[line]


@functools.lru_cache(maxsize=None)
def evaluate_lines(board):
    result = 0
    # adapted from:
    #   https://stackoverflow.com/a/571928/5092038
    iterators = [ board.rows, board.cols, board.diags ]
    combined = chain(*iterators)
    filtered = filter(lambda i: len(i) >= 5, combined)
    for line in filtered:
        # number of len 5 lines in current line
        l = len(line) - 4
        for i in range(l):
            sub_line = line[i:i+5]
            result += evaluate_line(sub_line)
    return result


def heuristic(game):
    x, y = game.last
    board = game.sub_board(x, y, SUB_BOARD_SIZE)
    return evaluate_lines(board)


def utility(game):
    '''
    Calculates heuristic value.

    Iterates over the rows, cols, and diagonals. In the respective order.

    Returns:
        The heuristic value.
    '''
    result = evaluate_lines(game.board)
    return result / game.plays

