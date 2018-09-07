from unittest import TestCase

from ai.board import Board
from ai.gamestate import GameState
from ai.heuristic import evaluate, evaluate_line, is_open

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
        # - - - X O
        # - - - - -
        # X X X X X
        # - O - - -
        # - - X - -

    def test_is_open(self):
        inpt = '--XO-'
        res = is_open(inpt)
        self.assertFalse(res)

        inpt = '-----'
        res = is_open(inpt)
        self.assertFalse(res)

        inpt = '----X'
        res = is_open(inpt)
        self.assertTrue(res)

        inpt = '--O--'
        res = is_open(inpt)
        self.assertTrue(res)

    def test_evaluate_line(self):
        expected = [ 3, -3, 3**14, 0, 0 ]
        result = [ evaluate_line(l) for l in self.game.board.rows ]
        self.assertListEqual(expected, result)

    def test_evaluate(self):
        # rows
        expected = 3**14
        # cols
        expected += 3 + 3**2 + 3**2
        # diagonals
        expected += 3

        # plays
        expected /= 9

        result = evaluate(self.game)
        self.assertEqual(expected, result)
