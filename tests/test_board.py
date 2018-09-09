from unittest import TestCase

from ai.board import Board

class TestBoard(TestCase):

    def setUp(self):
        self.board = Board(5, 5)
        self.board.board = ''.join([
            '----X',
            'XXXX-',
            '-----',
            'XXXXO',
            'X-X-X'
        ])
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
        print(type(self.board.board))
        row = '----X'
        self.assertEqual(res, row)

        res = self.board.row(3)
        row = 'XXXXO'
        self.assertEqual(res, row)

    def test_rows(self):
        for i, row in enumerate(self.board.rows):
            exp = self.board.row(i)
            self.assertEqual(exp, row)

    def test_cols(self):
        for i, col in enumerate(self.board.cols):
            exp = self.board.col(i)
            self.assertEqual(exp, col)

    def test_col(self):
        res = self.board.col(0)
        col = '-X-XX'
        self.assertEqual(res, col)

        res = self.board.col(3)
        col = '-X-X-'
        self.assertEqual(res, col)

    def test_rdiag(self):
        expected = [
            'X',
            'X-',
            '-XX',
            'X-X-',
            '-X-XX',
            '-X-O',
            '-X-',
            '--',
            'X'
        ]
        for diag, exp in enumerate(expected):
            res = self.board.rdiag(diag)
            print(res)
            self.assertEqual(res, exp)

    def test_ldiag(self):
        expected = [
            '-',
            'X-',
            '-X-',
            'X-X-',
            'XX-XX',
            '-X--',
            'XX-',
            '-O',
            'X'
        ]

        for i, exp in enumerate(expected):
            res = self.board.ldiag(i)
            self.assertEqual(res, exp)

    def test_diags(self):
        expected = [
            'X',
            'X-',
            '-XX',
            'X-X-',
            '-X-XX',
            '-X-O',
            '-X-',
            '--',
            'X',
            '-',
            'X-',
            '-X-',
            'X-X-',
            'XX-XX',
            '-X--',
            'XX-',
            '-O',
            'X'
        ]
        results = list(self.board.diags)
        self.assertListEqual(results, expected)

    def test_get(self):
        coords = [ (0, 0), (0, 3), (0, 1), (3, 3) ]
        expected = [ '-', 'X', 'X', 'X' ]
        results = [ self.board.get(x, y) for x, y in coords ]
        self.assertListEqual(expected, results)

    def test_set(self):
        self.board.set(1, 1, 'O')
        res = self.board.get(1, 1)
        self.assertEqual(res, 'O')

    def test_str(self):
        string = ('X - X - X\n'
                  'X X X X O\n'
                  '- - - - -\n'
                  'X X X X -\n'
                  '- - - - X')
        res = str(self.board)
        self.assertEqual(string, res)
        res = repr(self.board)
        self.assertEqual(string, res)

    def test_len(self):
        res = len(self.board)
        self.assertEqual(res, 25)

    def test_eq(self):
        b1 = Board(20, 20)
        b2 = Board(20, 20)
        self.assertEqual(b1, b2)

        b1.set(0, 0, 'x')
        self.assertNotEqual(b1, b2)

