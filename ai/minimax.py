from math import inf as INFINITY

from ai.heuristic import evaluate

MAX_DEPTH = 10
depth = -1

def min_play(game, alpha, beta):
    global depth, MAX_DEPTH
    depth += 1
    if depth >= MAX_DEPTH or game.over:
        return evaluate(game.board)

    best = INFINITY

    for x, y in game.moves:
        copy = game.next(x, y, -1)
        max_value = max_play(copy, alpha, beta)
        best = min(best, max_value)
        if best <= alpha:
            return best
        beta = min(beta, best)
    return best


def max_play(game, alpha, beta):
    global depth, MAX_DEPTH
    depth += 1
    if depth >= MAX_DEPTH or game.over:
        return evaluate(game.board)

    best = -INFINITY

    for x, y in game.moves:
        copy = game.next(x, y, 1)
        min_value = min_play(copy, alpha, beta)
        best = max(best, min_value)
        if best >= beta:
            return best
        alpha = max(alpha, best)
    return best


def minimax(game):
    global depth

    best_move = None
    best_score = -INFINITY
    for x, y in game.moves:
        depth = -1
        copy = game.next(x, y, 1)
        score = min_play(copy, best_score, INFINITY)
        if score > best_score:
            best_move = (x, y)
            best_score = score
    return best_move

