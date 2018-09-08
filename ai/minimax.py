from math import inf as INFINITY
from copy import deepcopy

class MiniMax(object):
    def __init__(self, util, heur, max_depth=3):
        super(MiniMax, self).__init__()
        self.utility = util
        self.heuristic = heur
        self.MAX_DEPTH = max_depth

    def min_play(self, game, alpha, beta, depth):
        if game.over:
            return self.utility(game)

        if depth >= self.MAX_DEPTH or game.plays < 6:
            return self.heuristic(game)

        games = ( game.next(x, y, 'O') for x, y in game.moves )
        scores = ( self.max_play(g, alpha, beta, depth + 1) for g in games )

        value = INFINITY

        for score in scores:
            value = min(value, score)
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

    def max_play(self, game, alpha, beta, depth):
        if game.over:
            return self.utility(game)

        if depth >= self.MAX_DEPTH or game.plays < 6:
            return self.heuristic(game)

        games = ( game.next(x, y, 'X') for x, y in game.moves )
        scores = ( self.min_play(g, alpha, beta, depth + 1) for g in games )

        value = -INFINITY

        for score in scores:
            value = max(value, score)
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def search(self, game):
        best_move = None
        best_score = -INFINITY

        for x, y in game.moves:
            copy = game.next(x, y, 'X')
            print(x, y)
            score = self.min_play(copy, best_score, INFINITY, 0)
            print(score)
            if score > best_score:
                best_move = (x, y)
                best_score = score
        return best_move

