from math import inf as INFINITY


class MiniMax(object):
    '''
    MiniMax class.

    This class is used to perform searches for the best cases in many game/ai
    related situations.

    Attributes:
        utility: function called when the game is in finished
            state.
        heuristic: function called when the search reaches maximum depth.
        max_depth: maximum depth allowed in the search. The higher the number
            more precise is the search and takes longer times.
    '''

    def __init__(self, util, heur, max_depth=3):
        '''
        Constructor.

        Args:
            util: utility function.
            heur: heuristic function.
            max_depth: maximum depth allowed.
        '''
        super(MiniMax, self).__init__()
        self.utility = util
        self.heuristic = heur
        self.max_depth = max_depth

    def _min_play(self, state, alpha, beta, depth):
        # Game finished has precedence over depth
        if state.over:
            return self.utility(state)

        if depth >= self.max_depth:
            return self.heuristic(state)

        states = ( state.next(x, y, 'O') for x, y in state.children )
        scores = ( self._max_play(g, alpha, beta, depth + 1) for g in states )

        value = INFINITY

        for score in scores:
            value = min(value, score)
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

    def _max_play(self, state, alpha, beta, depth):
        # Game finished has precedence over depth
        if state.over:
            return self.utility(state)

        if depth >= self.max_depth:
            return self.heuristic(state)

        states = ( state.next(x, y, 'X') for x, y in state.children )
        scores = ( self._min_play(g, alpha, beta, depth + 1) for g in states )

        value = -INFINITY

        for score in scores:
            value = max(value, score)
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def search(self, state):
        '''
        Performs the search for the best play from the current state.
        '''
        best_move = None
        best_score = -INFINITY
        beta = INFINITY

        for x, y in state.children:
            copy = state.next(x, y, 'X')
            score = self._min_play(copy, best_score, beta, 0)
            if score > best_score:
                best_move = (x, y)
                best_score = score
        return best_move
