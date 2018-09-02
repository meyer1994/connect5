from unittest import TestCase

from ai.board import Board
from ai.minimax import minimax

class TestMiniMax(TestCase):

    def setUp(self):
        board = Board(15, 15)
        board.set(5, 0, 1)
        board.set(6, 0, 1)
        board.set(7, 0, 1)
        board.set(8, 0, 1)
        self.board = board
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
        # - - - - - X X X X - - - - - -

    def test_minimax(self):
        expected = { (4, 0), (9, 0) }
        result = minimax(self.board, 1)
        self.assertIn(result, expected)
