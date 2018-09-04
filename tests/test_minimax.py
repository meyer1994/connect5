from unittest import TestCase

from ai.board import Board
from ai.minimax import minimax
from ai.gamestate import GameState

class TestMiniMax(TestCase):

    def setUp(self):
        board = Board(15, 15)
        board.set(5, 0, -1)
        board.set(6, 0, -1)
        board.set(7, 0, -1)
        board.set(8, 0, -1)
        board.set(9, 0, 1)
        self.game = GameState(board, False)
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
        # - - - - - O O O O X - - - - -

    def test_minimax(self):
        expected = (4, 0)
        result = minimax(self.game, 1)
        self.assertEqual(result, expected)
