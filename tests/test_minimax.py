from unittest import TestCase

from ai.board import Board
from ai.minimax import minimax
from ai.gamestate import GameState

class TestMiniMax(TestCase):

    def setUp(self):
        board = Board(13, 13)
        board.set(5, 4, -1)
        board.set(6, 5, 1)
        board.set(7, 5, -1)
        board.set(6, 6, -1)
        board.set(7, 6, 1)
        board.set(8, 6, -1)
        board.set(4, 7, 1)
        board.set(5, 7, -1)
        board.set(6, 7, -1)
        board.set(7, 7, 1)
        board.set(8, 7, 1)
        board.set(9, 7, 1)
        board.set(10, 7, -1)
        board.set(5, 8, -1)
        board.set(6, 8, 1)
        board.set(7, 8, 1)
        board.set(8, 8, 1)
        board.set(9, 8, -1)
        board.set(6, 9, -1)
        board.set(7, 9, 1)
        board.set(8, 9, 1)
        board.set(9, 9, 1)
        board.set(6, 10, -1)
        board.set(7, 10, -1)
        board.set(8, 10, -1)
        board.set(9, 10, 1)

        print(board)
        self.game = GameState(board, False)
        # E - - - - - - - - - - - - - - -
        # D - - - - - - - - - - - - - - -
        # C - - - - - - - - - - - - - - -
        # B - - - - - - - - - - - - - - -
        # A - - - - - - O O O X - - - - -
        # 9 - - - - - - O X X X - - - - -
        # 8 - - - - - O X X X O - - - - -
        # 7 - - - - X O O X X X O - - - -
        # 6 - - - - - - O X O - - - - - -
        # 5 - - - - - - X O - - - - - - -
        # 4 - - - - - O - - - - - - - - -
        # 3 - - - - - - - - - - - - - - -
        # 2 - - - - - - - - - - - - - - -
        # 1 - - - - - - - - - - - - - - -
        # 0 - - - - - - - - - - - - - - -
        #   0 1 2 3 4 5 6 7 8 9 A B C D E

    def test_minimax(self):
        result = minimax(self.game)
        print(result)
        self.assertFalse(True)


