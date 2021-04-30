from random import choice


class Game:
    def __init__(self):
        self.turn = choice((1, -1))
        self.player1_score = 0
        self.player2_score = 0
        self.comb_plus_throw = {(1, 2, 3, 4, 5, 6): 1000, (1, 1, 2, 2, 3, 3): 750}
        self.combinations = {(1, 1, 1, 1, 1, 1): 6000, (2, 2, 2, 2, 2, 2): 1600, (3, 3, 3, 3, 3, 3): 2400, (4, 4, 4, 4, 4, 4): 3200, (5, 5, 5, 5, 5, 5): 4000, (6, 6, 6, 6, 6, 6): 4800,
                             (1, 1, 1, 1, 1): 3000, (2, 2, 2, 2, 2): 800, (3, 3, 3, 3, 3): 1200, (4, 4, 4, 4, 4): 1600, (5, 5, 5, 5, 5): 2000, (6, 6, 6, 6, 6): 2400}

    def finish_turn(self):
        self.turn *= -1

    def put_away(self):
        def count_(self):
            pass

