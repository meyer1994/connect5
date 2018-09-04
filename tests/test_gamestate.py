from unittest import TestCase

from ai.board import Board
from ai.gamestate import GameState

class TestGameState(TestCase):

    def setUp(self):
        board = Board(5, 5)
        board.board = [
            0, 0, 0, 0,  1,
            1, 1, 1, 1,  0,
            0, 0, 0, 0,  0,
            1, 1, 1, 1, -1,
            1, 0, 1, 0,  1
        ]
        self.game = GameState(board, False)
        # X - X - X
        # X X X X O
        # - - - - -
        # X X X X -
        # - - - - X

    def test_next(self):
        result = self.game.next(0, 0, -1)
        self.game.board.set(0, 0, -1)
        self.assertEqual(result, self.game)

    def test_moves(self):
        expected = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (3, 2),
            (4, 2),
            (1, 4),
            (3, 4)
        ]
        result = self.game.moves
        for res, exp in zip(result, expected):
            self.assertEqual(res, exp)

    def test_is_winner(self):
        line = self.game.board.row(1)
        result = self.game._is_winner(line)
        self.assertFalse(result)

        # make it a winning line
        line[-1] = 1
        result = self.game._is_winner(line)
        self.assertTrue(result)

    def test_is_over(self):
        result = self.game._is_over(3, 1)
        self.assertFalse(result)

        # Test cols
        copy = self.game.next(4, 1, 1)
        result = copy._is_over(4, 1)
        self.assertTrue(result)

        # Test rows
        copy = self.game.next(0, 0, 1)
        copy.board.set(0, 2, 1)
        result = copy._is_over(0, 0)
        self.assertTrue(result)

        # Test rdiag
        copy = self.game.next(2, 2, 1)
        result = copy._is_over(2, 2)
        self.assertTrue(result)

        # Test ldiag
        copy = self.game.next(2, 2, 1)
        copy.board.set(0, 0, 1)
        copy.board.set(0, 4, 0)
        result = copy._is_over(2, 2)
        self.assertTrue(result)
