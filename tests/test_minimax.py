from unittest import TestCase

from ai.board import Board
from ai.minimax import MiniMax
from ai.gamestate import GameState
from ai.heuristic import utility, heuristic

class TestMiniMax(TestCase):
    def setUp(self):
        board = Board(10, 10)
        board.board = ''.join([
            '----------',
            '----------',
            '----------',
            '--OOOX----',
            '--OXXX----',
            '-OXXXO----',
            'XOOXXXO---',
            '--OXO-----',
            '--XO------',
            '-O--------'][::-1]
        )
        self.game = GameState(board, False)
        self.game.plays = 25
        # 9 - - - - - - - - - -
        # 8 - - - - - - - - - -
        # 7 - - - - - - - - - -
        # 6 - - O O O X - - - -
        # 5 - - O X X X - - - -
        # 4 - O X X X O - - - -
        # 3 X O O X X X O - - -
        # 2 - - O X O - - - - -
        # 1 - - X O - - - - - -
        # 0 - O - - - - - - - -
        #   0 1 2 3 4 5 6 7 8 9
        self.minimax = MiniMax(utility, heuristic, 3)

    def test_minimax(self):
        # I 've made this way because the algorithm will alwasy return some
        # value on the top right of the board.
        # So i get a sub board and add values to the possible moves, because
        # i am lazy...
        # return
        board = self.game.sub_board(8, 8, 4)
        game = GameState(board, False)
        expected = { (x + 5, y + 5) for x, y in game.moves }
        result = self.minimax.search(self.game)
        self.assertIn(result, expected)

    def test_min_depth(self):
        self.minimax = MiniMax(utility, heuristic, 2)

        expected = (6, 2)
        result = self.minimax.search(self.game)
        self.assertEqual(result, expected)
