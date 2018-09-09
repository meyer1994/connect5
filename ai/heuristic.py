import functools

from itertools import product, chain
from collections import defaultdict

# This part of the code generates all the possible combinations for the open
# lines.

# Generates all open lines for X
ONLY_X = { ''.join(k): 3**k.count('X') for k in product('X-', repeat=5) }
ONLY_X['XXXXX'] = 3**14
del ONLY_X['-----']

# All open lines for O
ONLY_O = { ''.join(k): -3**k.count('O') for k in product('O-', repeat=5) }
ONLY_O['OOOOO'] = -3**14
del ONLY_O['-----']

# Creates a dict that returns 0 for everything
VALUE_TABLE = defaultdict(lambda: 0)

# Adds the values generated before
VALUE_TABLE.update(ONLY_X)
VALUE_TABLE.update(ONLY_O)

# By definition, this is not an open line
VALUE_TABLE['-----'] = 0


# Customizable sub board size for the heuristic function
SUB_BOARD_SIZE = 7



def evaluate_line(line):
    '''
    Gets the value of the line.
    '''
    return VALUE_TABLE[line]


@functools.lru_cache(maxsize=None)
def evaluate_lines(board):
    '''
    This functions iterates over all the possible lines of a board and returns
    the values for each line.

    It is memoized. It only executes once per board.

    Args:
        board: game board.

    Returns:
        Sum of all line values.
    '''
    result = 0
    # adapted from:
    #   https://stackoverflow.com/a/571928/5092038
    iterators = [ board.rows, board.cols, board.diags ]
    combined = chain(*iterators)
    for line in combined:
        line_len = len(line)
        if line_len < 5:
            continue
        for i in range(line_len - 4):
            sub_line = line[i:i+5]
            result += evaluate_line(sub_line)
    return result


def heuristic(game):
    '''
    Returns the heuristic value for some game.

    It takes a part of the original board and applies the same function of the
    utility into it.

    Args:
        game: game state.

    Returns:
        Sum of all line values.
    '''
    x, y = game.last
    board = game.sub_board(x, y, SUB_BOARD_SIZE)
    return evaluate_lines(board)


def utility(game):
    '''
    Calculates heuristic value.

    Iterates over the rows, cols, and diagonals. In the respective order.

    Args:
        game: game state.

    Returns:
        Sum of all line values divided by the total number of plays.
    '''
    result = evaluate_lines(game.board)
    return result / game.plays

