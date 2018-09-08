from ai.board import Board
from ai.heuristic import evaluate, semi
from ai.gamestate import GameState
from ai.minimax import MiniMax

import math

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
board = Board(15, 15)
game = GameState(board, False)
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

minimax = MiniMax(evaluate, semi, 2)

print(game)
while not game.over:
    x, y = minimax.search(game)
    print(x, y)
    game = game.next(x, y, 'X')
    print(game)
    x, y = map(int, input('play:').split())
    game = game.next(x, y, 'O')
    print(game)
