

class Heuristic(object):
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
        total = abs(sum(line))
        return total == 5 - zeroes

    def _check_line(self, line):
        if not self._is_open(line):
            return 0

        summ = sum(line)
        res = 3 ** abs(summ)
        if summ >= 0:
            return res
        else:
            return -res

    def value(self):
        pass
