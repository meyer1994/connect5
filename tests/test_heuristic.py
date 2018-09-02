from unittest import TestCase

from ai.board import Board
from ai.heuristic import Heuristic

class TestHeuristic(TestCase):

    def setUp(self):
        board = Board(5, 5)
        board.set(2, 0, 1)
        board.set(1, 1, -1)
        for i in range(5):
            board.set(i, 2, 1)
        board.set(3, 4, 1)
        board.set(4, 4, -1)
        # - - - X O
        # - - - - -
        # X X X X X
        # - O - - -
        # - - X - -
        self.heuristic = Heuristic(board)

    def test_is_open(self):
        inpt = [ 0, 0, 1, -1, 0 ]
        res = self.heuristic._is_open(inpt)
        self.assertFalse(res)

        inpt = [ 0, 0, 0, 0, 0 ]
        res = self.heuristic._is_open(inpt)
        self.assertFalse(res)

        inpt = [ 0, 0, 0, 0, 1 ]
        res = self.heuristic._is_open(inpt)
        self.assertTrue(res)

        inpt = [ 0, 0, -1, 0, 0 ]
        res = self.heuristic._is_open(inpt)
        self.assertTrue(res)

    def test_check_line(self):
        expected = [ 3, -3, 3**14, 0, 0 ]
        rows = self.heuristic.board.rows
        for exp, row in zip(expected, rows):
            res = self.heuristic._line_value(row)
            self.assertEqual(exp, res)

    def test_value(self):
        # rows
        expected = 3**14
        # cols
        expected += 3 + 3**2 + 3**2
        # diagonals
        expected += 3

        result = self.heuristic.value()
        self.assertEqual(expected, result)
