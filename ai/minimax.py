from math import inf as INFINITY

from ai.heuristic import evaluate

MAX_DEPTH = 2

def min_play(game, alpha, beta, depth):
    global MAX_DEPTH
    if depth >= MAX_DEPTH or game.over:
        return evaluate(game.board)

    games = ( game.next(x, y, -1) for x, y in game.moves )
    scores = ( max_play(g, alpha, beta, depth + 1) for g in games )

    value = INFINITY

    for score in scores:
        value = min(value, score)
        if value <= alpha:
            return value
        beta = min(beta, value)
    return value

def max_play(game, alpha, beta, depth):
    global MAX_DEPTH
    if depth >= MAX_DEPTH or game.over:
        return evaluate(game.board)

    games = ( game.next(x, y, 1) for x, y in game.moves )
    scores = ( min_play(g, alpha, beta, depth + 1) for g in games )

    value = -INFINITY

    for score in scores:
        value = max(value, score)
        if value >= beta:
            return value
        alpha = max(alpha, value)
    return value


def minimax(game):
    best_move = None
    best_score = -INFINITY

    for x, y in game.moves:
        print(x, y)
        copy = game.next(x, y, 1)
        score = min_play(copy, best_score, INFINITY, 0)
        if score > best_score:
            best_move = (x, y)
            best_score = score
    return best_move

