from unittest import TestCase

from ai.board import Board
from ai.gamestate import GameState
from ai import heuristic as heur

class TestHeuristic(TestCase):
    def setUp(self):
        board = Board(5, 5)
        board.set(2, 0, 'X')
        board.set(1, 1, 'O')
        board.set(0, 2, 'X')
        board.set(1, 2, 'X')
        board.set(2, 2, 'X')
        board.set(3, 2, 'X')
        board.set(4, 2, 'X')
        board.set(3, 4, 'X')
        board.set(4, 4, 'O')
        self.game = GameState(board, False)
        heur.MEMOIZE = {}
        # - - - X O
        # - - - - -
        # X X X X X
        # - O - - -
        # - - X - -

    def test_evaluate_line(self):
        expected = [ 3, -3, 3**14, 0, 0 ]
        result = [ heur.evaluate_line(l) for l in self.game.board.rows ]
        self.assertListEqual(expected, result)

    def test_utility(self):
        # rows
        expected = 3**14
        # cols
        expected += 3 + 3**2 + 3**2
        # diagonals
        expected += 3

        # plays
        expected /= 9

        result = heur.utility(self.game)
        result = heur.utility(self.game)
        self.assertEqual(expected, result)

    def test_heuristic(self):
        # rows
        expected = 3**14
        # cols
        expected += 3 + 3**2 + 3**2
        # diagonals
        expected += 3
        heur.SUB_BOARD_SIZE = 5
        result = heur.heuristic(self.game)
        self.assertEqual(expected, result)
