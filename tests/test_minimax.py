from unittest import TestCase

from ai.board import Board
from ai.minimax import minimax
from ai.gamestate import GameState

class TestMiniMax(TestCase):
    def setUp(self):
        board = Board(8, 9)
        board.board = [
            0, -1,  0,  0,  0,  0,  0, 0,
            0,  0,  1, -1,  0,  0,  0, 0,
            0,  0, -1,  1, -1,  0,  0, 0,
            1, -1, -1,  1,  1,  1, -1, 0,
            0, -1,  1,  1,  1, -1,  0, 0,
            0,  0, -1,  1,  1,  1,  0, 0,
            0,  0, -1, -1, -1,  1,  0, 0,
            0,  0,  0,  0,  0,  0,  0, 0,
            0,  0,  0,  0,  0,  0,  0, 0,
        ]
        self.game = GameState(board, False)
        # 8 - - - - - - - -
        # 7 - - - - - - - -
        # 6 - - O O O X - -
        # 5 - - O X X X - -
        # 4 - O X X X O - -
        # 3 X O O X X X O -
        # 2 - - O X O - - -
        # 1 - - X O - - - -
        # 0 - O - - - - - -
        #   0 1 2 3 4 5 6 7

    def test_minimax(self):
        expected = {
            (6, 5),
            (6, 6),
            (6, 7)
        }
        result = minimax(self.game)
        self.assertIn(result, expected)
