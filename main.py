from ai.board import Board
from ai.heuristic import utility, heuristic
from ai.gamestate import GameState
from ai.minimax import MiniMax


def user_input():
    move = input('Your move (x, y) separated by spaces:')
    try:
        x, y = map(int, move.split())
        return (x, y)
    except Exception:
        print('Try again')
        return user_input()


# Empty board
board = Board(15, 15)
game = GameState(board, False)
minimax = MiniMax(utility, heuristic, 2)

# Sample board used for tests
# board = Board(10, 10)
# board.board = ''.join([
#     '-O--------',
#     '--XO------',
#     '--OXO-----',
#     'XOOXXXO---',
#     '-OXXXO----',
#     '--OXXX----',
#     '--OOOX----',
#     '----------',
#     '----------',
#     '----------',
# ])
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


while not game.over:
    print('Computer thinking...')
    x, y = minimax.search(game)
    game = game.next(x, y, 'X')
    print(game)
    print(f'Computer played ({x}, {y})')

    if game.over:
        print('Game is over')
        break

    print()

    x, y = user_input()
    game = game.next(x, y, 'O')
    print(game)

