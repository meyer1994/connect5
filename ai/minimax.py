from math import inf as INFINITY

from ai.heuristic import evaluate

MAX_DEPTH = 10
depth = 0

def min_play(game, player):
    global depth
    global MAX_DEPTH

    if depth > MAX_DEPTH:
        return evaluate(game.board)
    depth += 1

    moves = game.moves
    best_score = INFINITY
    for x, y in moves:
        copy = game.next(x, y, player)
        score = max_play(copy, player)
        if score < best_score:
            best_score = score
    return best_score


def max_play(game, player):
    global depth
    global MAX_DEPTH

    if depth > MAX_DEPTH:
        return evaluate(game.board)
    depth += 1

    moves = game.moves
    best_score = -INFINITY
    for x, y in moves:
        copy = game.next(x, y, player)
        score = min_play(copy, player)
        if score > best_score:
            best_score = score
    return best_score


def minimax(game, player):
    moves = game.moves
    best_move = next(moves)
    best_score = -INFINITY
    for x, y in moves:
        copy = game.next(x, y, player)
        score = min_play(copy, player)
        if score > best_score:
            best_move = (x, y)
            best_score = score
    return best_move

