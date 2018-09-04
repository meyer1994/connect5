from unittest import TestCase

from ai.board import Board

class TestBoard(TestCase):

    def setUp(self):
        self.board = Board(5, 5)
        self.board.board = [
            0, 0, 0, 0,  1,
            1, 1, 1, 1,  0,
            0, 0, 0, 0,  0,
            1, 1, 1, 1, -1,
            1, 0, 1, 0,  1
        ]
        # X - X - X
        # X X X X O
        # - - - - -
        # X X X X -
        # - - - - X

    def test_constructor(self):
        self.assertEqual(self.board.width, 5)
        self.assertEqual(self.board.height, 5)

    def test_row(self):
        res = self.board.row(0)
        row = [ 0, 0, 0, 0, 1 ]
        self.assertListEqual(res, row)

        res = self.board.row(3)
        row = [ 1, 1, 1, 1, -1 ]
        self.assertListEqual(res, row)

    def test_rows(self):
        for i, row in enumerate(self.board.rows):
            exp = self.board.row(i)
            self.assertListEqual(exp, row)

    def test_cols(self):
        for i, col in enumerate(self.board.cols):
            exp = self.board.col(i)
            self.assertListEqual(exp, col)

    def test_col(self):
        res = self.board.col(0)
        col = [ 0, 1, 0, 1, 1 ]
        self.assertListEqual(res, col)

        res = self.board.col(3)
        col = [ 0, 1, 0, 1, 0 ]
        self.assertListEqual(res, col)

    def test_rdiag(self):
        expected = [
            [ 1 ],
            [ 0, 1 ],
            [ 1, 1, 0 ],
            [ 0, 1, 0, 1 ],
            [ 1, 1, 0, 1, 0 ],
            [ -1, 0, 1, 0 ],
            [ 0, 1, 0 ],
            [ 0, 0 ],
            [ 1 ]
        ]
        for i, exp in enumerate(expected):
            res = self.board.rdiag(i)
            self.assertListEqual(res, exp)

    def test_ldiag(self):
        expected = [
            [ 0 ],
            [ 1, 0 ],
            [ 0, 1, 0 ],
            [ 1, 0, 1, 0 ],
            [ 1, 1, 0, 1, 1 ],
            [ 0, 1, 0, 0 ],
            [ 1, 1, 0 ],
            [ 0, -1 ],
            [ 1 ]
        ]
        for i, exp in enumerate(expected):
            res = self.board.ldiag(i)
            self.assertListEqual(res, exp)

    def test_diags(self):
        expected = [
            [ 1 ],
            [ 0, 1 ],
            [ 1, 1, 0 ],
            [ 0, 1, 0, 1 ],
            [ 1, 1, 0, 1, 0 ],
            [ -1, 0, 1, 0 ],
            [ 0, 1, 0 ],
            [ 0, 0 ],
            [ 1 ],
            [ 0 ],
            [ 1, 0 ],
            [ 0, 1, 0 ],
            [ 1, 0, 1, 0 ],
            [ 1, 1, 0, 1, 1 ],
            [ 0, 1, 0, 0 ],
            [ 1, 1, 0 ],
            [ 0, -1 ],
            [ 1 ]
        ]
        diags = self.board.diags
        for res, exp in zip(diags, expected):
            self.assertListEqual(res, exp)

    def test_get(self):
        coords = [ (0, 0), (0, 3), (0, 1), (3, 3) ]
        results = [ 0, 1, 1, 1 ]

        for coord, res in zip(coords, results):
            at = self.board.get(*coord)
            self.assertEqual(at, res)

    def test_set(self):
        self.board.set(1, 1, -1)
        res = self.board.get(1, 1)
        self.assertEqual(res, -1)

    def test_str(self):
        string = ('X - X - X\n'
                  'X X X X O\n'
                  '- - - - -\n'
                  'X X X X -\n'
                  '- - - - X')
        res = str(self.board)
        self.assertEqual(string, res)

    def test_len(self):
        res = len(self.board)
        self.assertEqual(res, 25)
