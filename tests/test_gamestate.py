from unittest import TestCase
from itertools import chain

from ai.board import Board
from ai.gamestate import GameState

class TestGameState(TestCase):
    def setUp(self):
        board = Board(9, 9)
        board.board = ''.join([
            '-O-------',
            '--XO-----',
            '--OXO----',
            'XOOXXXO--',
            '-OXXXO---',
            '--OXXX---',
            '--OOOX---',
            '---------',
            '---------',
        ])
        self.game = GameState(board, False)
        # 8 - - - - - - - - -
        # 7 - - - - - - - - -
        # 6 - - O O O X - - -
        # 5 - - O X X X - - -
        # 4 - O X X X O - - -
        # 3 X O O X X X O - -
        # 2 - - O X O - - - -
        # 1 - - X O - - - - -
        # 0 - O - - - - - - -
        #   0 1 2 3 4 5 6 7 8

    def test_next(self):
        result = self.game.next(0, 0, 'O')
        self.game.last = (0, 0)
        self.game.plays += 1
        self.game.board.set(0, 0, 'O')
        self.assertEqual(result, self.game)

    def test_moves(self):
        # yes, I did byt hand...
        expected = [
            (6, 6), (5, 2), (6, 2), (6, 4), (6, 5), (7, 7), (6, 7),
            (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (1, 6), (1, 5),
            (1, 2), (1, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2),
            (7, 3), (7, 4), (7, 5), (7, 6), (8, 8), (7, 8), (6, 8),
            (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7),
            (0, 6), (0, 5), (0, 4), (0, 2), (0, 1), (0, 0), (2, 0),
            (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (8, 1),
            (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)
        ]
        result = list(self.game.moves)
        from pprint import pprint
        pprint(list(zip(result, expected)))
        self.assertListEqual(expected, result)

    def test_is_winner(self):
        lines = [
            self.game.board.rows,
            self.game.board.cols,
            self.game.board.diags
        ]
        for line in chain(*lines):
            res = self.game._is_winner(line)
            self.assertFalse(res)

        # make a winning line
        self.game.board.set(6, 5, 'x')
        self.game.board.set(7, 5, 'x')
        line = self.game.board.row(5)
        result = self.game._is_winner(line)
        self.assertTrue(result)

    def test_is_over(self):
        # Test cols
        copy = self.game.next(3, 6, 'x')
        self.assertTrue(copy.over)

        # Test rows
        copy = self.game.next(6, 5, 'x')
        self.assertFalse(copy.over)
        copy = copy.next(7, 5, 'x')
        self.assertTrue(copy.over)

        # Test rdiag
        copy = self.game.next(0, 4, 'o')
        self.assertFalse(copy.over)
        copy = copy.next(4, 0, 'o')
        self.assertTrue(copy.over)

        # Test ldiag
        copy = self.game.next(6, 7, 'x')
        self.assertFalse(copy.over)
        copy = copy.next(7, 8, 'x')
        self.assertTrue(copy.over)

    def test_full_board_is_over(self):
        board = Board(4, 4)
        game = GameState(board, False)
        for x, y in game.moves:
            game = game.next(x, y, 'X')
        self.assertTrue(game.over)
        self.assertEqual(game.plays, 16)

    def test_plays(self):
        # original
        expected = 26
        result = self.game.plays
        self.assertEqual(expected, result)

        # add piece
        copy = self.game.next(0, 0, 'x')
        expected = 27
        result = copy.plays
        self.assertEqual(expected, result)

        # add piece on top of another
        copy = copy.next(0, 0, 'o')
        expected = 27
        result = copy.plays
        self.assertEqual(expected, result)

        # remove piece
        copy = copy.next(0, 0, '-')
        expected = 26
        result = copy.plays
        self.assertEqual(expected, result)

    def test_str(self):
        expected = str(self.game.board)
        result = str(self.game)
        self.assertEqual(expected, result)

    def test_sub_board(self):
        expected = Board(7, 7)
        expected.board = ''.join([
            'OOOX---',
            'OXXX---',
            'XXXO---',
            'OXXXO--',
            'OXO----',
            'XO-----',
            '-------'
        ][::-1])

        result = self.game.sub_board(6, 4)
        print()
        print(expected)
        print('='*10)
        print(result)
        self.assertEqual(expected, result)

    def test_hash(self):
        hash(self.game)
        d = {self.game: '' }
        s = { self.game }
