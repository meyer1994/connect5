from unittest import TestCase

from ai.board import Board
from ai.heuristic import Heuristic

class TestHeuristic(TestCase):

    def setUp(self):
        board = Board(5, 5)
        board.set(0, 2, 1)
        board.set(1, 1, -1)
        board.set(2, 0, 1)
        board.set(4, 4, -1)
        board.set(3, 4, 1)
        # - - - X O
        # - - - - -
        # X - - - -
        # - O - - -
        # - - X - -
        self.heuristic = Heuristic(board)
        self.board = board

    def test_is_open(self):
        inpt = [ 0, 0, 1, -1, 0 ]
        res = self.heuristic._is_open(inpt)
        self.assertFalse(res)

        inpt = [ 0, 0, 0, 0, 0 ]
        res = self.heuristic._is_open(inpt)
        self.assertTrue(res)

        inpt = [ 0, 0, 0, 0, 1 ]
        res = self.heuristic._is_open(inpt)
        self.assertTrue(res)

    def test_check_line(self):
        expected = [ 3, -3, 3, 1, 0 ]
        rows = self.board.rows
        for exp, row in zip(expected, rows):
            res = self.heuristic._check_line(row)
            self.assertEqual(exp, res)
