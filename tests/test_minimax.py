from unittest import TestCase

from ai.board import Board
from ai.minimax import minimax
from ai.gamestate import GameState

class TestMiniMax(TestCase):

    def setUp(self):
        board = Board(6, 6)
        board.set(1, 0, -1)
        board.set(2, 0, -1)
        board.set(3, 0, -1)
        board.set(4, 0, -1)
        board.set(5, 0, 1)
        self.game = GameState(board, False)
        # - - - - - -
        # - - - - - -
        # - - - - - -
        # - - - - - -
        # - - - - - -
        # - O O O O X

    def test_minimax(self):
        expected = (4, 0)
        result = minimax(self.game, 1)
        self.assertTupleEqual(result, expected)

        expected = (4, 0)
        result = minimax(self.game, -1)
        self.assertTupleEqual(result, expected)
