

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
    for row in board.rows:
        for i in range(len(row) - 4):
            line = row[i:i+5]
            if is_open(line):
                result += evaluate_line(line)

    for col in board.cols:
        for i in range(len(col) - 4):
            line = col[i:i+5]
            if is_open(line):
                result += evaluate_line(line)

    for diag in board.diags:
        for i in range(len(diag) - 4):
            line = diag[i:i+5]
            if is_open(line):
                result += evaluate_line(line)

    return result
