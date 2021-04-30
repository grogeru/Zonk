class Game:
    def __init__(self):
        self.turn = choice((1, -1))
        self.player1_score = 0
        self.player2_score = 0
        self.comb_plus_throw = {(1, 2, 3, 4, 5, 6): 1000, (1, 1, 2, 2, 3, 3): 750}
        self.combinations = {(1): 100, (5): 50, }

    def finish_turn(self):
        self.turn *= -1

    def put_away(self):
        def count_(self):
            pass
