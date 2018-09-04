from math import inf as INFINITY

from ai.heuristic import evaluate

MAX_DEPTH = 3
depth = -1

def min_play(game, player):
    global depth, MAX_DEPTH
    depth += 1
    if depth >= MAX_DEPTH or game.over:
        return evaluate(game.board)

    moves = game.moves
    best_score = INFINITY
    for x, y in moves:
        copy = game.next(x, y, -player)
        score = max_play(copy, player)
        if score < best_score:
            best_score = score
    return best_score


def max_play(game, player):
    global depth, MAX_DEPTH
    depth += 1
    if depth >= MAX_DEPTH or game.over:
        return evaluate(game.board)

    moves = game.moves
    best_score = -INFINITY
    for x, y in moves:
        copy = game.next(x, y, player)
        score = min_play(copy, player)
        if score > best_score:
            best_score = score
    return best_score


def minimax(game, player):
    global depth
    depth = -1

    moves = list(game.moves)
    best_move = moves[0]
    best_score = -INFINITY
    for x, y in moves:
        copy = game.next(x, y, player)
        score = min_play(copy, player)
        if score > best_score:
            best_move = (x, y)
            best_score = score
    return best_move

