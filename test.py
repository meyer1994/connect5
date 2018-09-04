from ai.board import Board
from ai.minimax import minimax
from ai.gamestate import GameState

board = Board(6, 6)
board.set(1, 0, -1)
board.set(2, 0, -1)
board.set(3, 0, -1)
board.set(4, 0, -1)
board.set(5, 0, 1)
game = GameState(board, False)
# - - - - - -
# - - - - - -
# - - - - - -
# - - - - - -
# - - - - - -
# - O O O O X

expected = (0, 0)
result = minimax(game, 1)
print(result)

expected = (0, 0)
result = minimax(game, -1)
print(result)
