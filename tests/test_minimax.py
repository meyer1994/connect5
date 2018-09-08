from unittest import TestCase

from ai.board import Board
from ai.minimax import MiniMax
from ai.gamestate import GameState
from ai.heuristic import evaluate, semi

class TestMiniMax(TestCase):
    def setUp(self):
        board = Board(8, 9)
        board.board = ''.join([
        '--------',
        '--------',
        '--OOOX--',
        '--OXXX--',
        '-OXXXO--',
        'XOOXXXO-',
        '--OXO---',
        '--XO----',
        '-O------'][::-1])
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
        self.minimax = MiniMax(evaluate, semi, 4)

    def test_minimax(self):
        return
        expected = {
            (6, 5),
            (6, 6),
            (6, 7)
        }
        result = self.minimax.search(self.game)
        self.assertIn(result, expected)
