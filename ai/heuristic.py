import itertools

VALUE_TABLE = {
    0: 0,
    1: 3**1,
    2: 3**2,
    3: 3**3,
    4: 3**4,
    5: 3**14,
    -5: -(3**14),
    -4: -(3**4),
    -3: -(3**3),
    -2: -(3**2),
    -1: -(3**1),
}

def is_open(line):
    '''
    Checks if a line is open.

    An open line is a line of length 5 in which there is only pieces of one
    player.

    Args:
        line: line to check.

    Returns:
        True if it is open, False otherwise.
    '''
    zeroes = line.count(0)
    if zeroes == 5:
        return False
    total = abs(sum(line))
    return total == 5 - zeroes


def evaluate_line(line):
    s = sum(line)
    return VALUE_TABLE[s]


def evaluate(board):
    '''
    Calculates heuristic value.

    Iterates over the rows, cols, and diagonals. In the respective order.

    Returns:
        The heuristic value.
    '''
    result = 0
    plays = len(board) - board.board.count(0)

    # copied from:
    #   https://stackoverflow.com/a/571928/5092038
    iterators = [ board.rows, board.cols, board.diags ]
    for line in itertools.chain(*iterators):

        if len(line) < 5:
            continue

        for i in range(len(line) - 4):
            sub_line = line[i:i+5]
            if is_open(sub_line):
                result += evaluate_line(sub_line)

    return result / plays
