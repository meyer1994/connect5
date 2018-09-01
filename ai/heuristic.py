

class Heuristic(object):

    LINE_TABLE = {
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

    def __init__(self, board):
        super(Heuristic, self).__init__()
        self.board = board
        self.sum = 0

    def _is_open(self, line):
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

    def _line_value(self, line):
        s = sum(line)
        return Heuristic.LINE_TABLE[s]

    def value(self):
        pass
