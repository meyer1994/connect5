from math import inf as INFINITY

from ai.heuristic import evaluate

MAX_DEPTH = 50
depth = -1

def min_play(game):
    global depth, MAX_DEPTH
    depth += 1
    if depth >= MAX_DEPTH or game.over:
        return evaluate(game.board)

    games = ( game.next(x, y, -1) for x, y in game.moves )
    scores = map(max_play, games)
    return min(scores)

def max_play(game):
    global depth, MAX_DEPTH
    depth += 1
    if depth >= MAX_DEPTH or game.over:
        return evaluate(game.board)

    games = ( game.next(x, y, 1) for x, y in game.moves )
    scores = map(min_play, games)
    return max(scores)


def minimax(game):
    global depth

    best_move = None
    best_score = -INFINITY
    for x, y in game.moves:
        depth = -1
        copy = game.next(x, y, 1)
        score = min_play(copy)
        if score > best_score:
            best_move = (x, y)
            best_score = score
    return best_move

