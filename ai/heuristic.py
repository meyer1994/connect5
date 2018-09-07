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


def evaluate_line(line):
    return VALUE_TABLE[line]


def evaluate(game):
    '''
    Calculates heuristic value.

    Iterates over the rows, cols, and diagonals. In the respective order.

    Returns:
        The heuristic value.
    '''
    result = 0
    plays = game.plays

    # adapted from:
    #   https://stackoverflow.com/a/571928/5092038
    iterators = [ game.board.rows, game.board.cols, game.board.diags ]
    combined = chain(*iterators)
    filtered = filter(lambda i: len(i) >= 5, combined)
    for line in filtered:
        # number of len 5 lines in current line
        l = len(line) - 4
        for i in range(l):
            sub_line = line[i:i+5]
            result += evaluate_line(sub_line)

    return result / plays
