from random import choice


class Game:
    def __init__(self):
        self.combinations = []
        self.turn = choice((1, -1))
        self.player1_score = 0
        self.player2_score = 0
        self.comb_plus_throw = {(1, 2, 3, 4, 5, 6): 1000, (1, 1, 2, 2, 3, 3): 750}
        self.combinations = []

    def check_combinations_player1(self):
        self.combinations.sort()
        while self.combinations != []:
            if self.combinations.count(1) == 6:
                self.combinations.clear()
                self.player1_score += 8000
            elif self.combinations.count(1) == 5:
                self.combinations = self.combinations[5:]
                self.player1_score += 4000
            elif self.combinations.count(1) == 4:
                self.combinations = self.combinations[4:]
                self.player1_score += 2000
            elif self.combinations.count(1) == 3:
                self.combinations = self.combinations[3:]
                self.player1_score += 1000
            elif self.combinations.count(1) == 2:
                self.combinations = self.combinations[2:]
                self.player1_score += 200
            elif self.combinations.count(1) == 1:
                self.combinations = self.combinations[1:]
                self.player1_score += 100

            if self.combinations.count(2) == 6:
                self.combinations.clear()
                self.player1_score += 1600
            elif self.combinations.count(2) == 5:
                self.combinations = self.combinations[5:]
                self.player1_score += 800
            elif self.combinations.count(2) == 4:
                self.combinations = self.combinations[4:]
                self.player1_score += 400
            elif self.combinations.count(2) == 3:
                self.combinations = self.combinations[3:]
                self.player1_score += 200

            if self.combinations.count(3) == 6:
                self.combinations.clear()
                self.player1_score += 2400
            elif self.combinations.count(3) == 5:
                self.combinations = self.combinations[5:]
                self.player1_score += 1200
            elif self.combinations.count(3) == 4:
                self.combinations = self.combinations[4:]
                self.player1_score += 600
            elif self.combinations.count(3) == 3:
                self.combinations = self.combinations[3:]
                self.player1_score += 300

            if self.combinations.count(4) == 6:
                self.combinations.clear()
                self.player1_score += 3200
            elif self.combinations.count(4) == 5:
                self.combinations = self.combinations[5:]
                self.player1_score += 1600
            elif self.combinations.count(4) == 4:
                self.combinations = self.combinations[4:]
                self.player1_score += 800
            elif self.combinations.count(4) == 3:
                self.combinations = self.combinations[3:]
                self.player1_score += 400

            if self.combinations.count(5) == 6:
                self.combinations.clear()
                self.player1_score += 4000
            elif self.combinations.count(5) == 5:
                self.combinations = self.combinations[5:]
                self.player1_score += 2000
            elif self.combinations.count(5) == 4:
                self.combinations = self.combinations[4:]
                self.player1_score += 1000
            elif self.combinations.count(5) == 3:
                self.combinations = self.combinations[3:]
                self.player1_score += 500
            elif self.combinations.count(5) == 1:
                self.combinations = self.combinations[1:]
                self.player1_score += 50

            if self.combinations.count(6) == 6:
                self.combinations.clear()
                self.player1_score += 4800
            elif self.combinations.count(6) == 5:
                self.combinations = self.combinations[5:]
                self.player1_score += 2400
            elif self.combinations.count(6) == 4:
                self.combinations = self.combinations[4:]
                self.player1_score += 1200
            elif self.combinations.count(6) == 3:
                self.combinations = self.combinations[3:]
                self.player1_score += 600

    def check_combinations_player2(self):
        self.combinations.sort()
        while self.combinations != []:
            if self.combinations.count(1) == 6:
                self.combinations.clear()
                self.player2_score += 8000
            elif self.combinations.count(1) == 5:
                self.combinations = self.combinations[5:]
                self.player2_score += 4000
            elif self.combinations.count(1) == 4:
                self.combinations = self.combinations[4:]
                self.player2_score += 2000
            elif self.combinations.count(1) == 3:
                self.combinations = self.combinations[3:]
                self.player2_score += 1000
            elif self.combinations.count(1) == 2:
                self.combinations = self.combinations[2:]
                self.player2_score += 200
            elif self.combinations.count(1) == 1:
                self.combinations = self.combinations[1:]
                self.player2_score += 100

            if self.combinations.count(2) == 6:
                self.combinations.clear()
                self.player2_score += 1600
            elif self.combinations.count(2) == 5:
                self.combinations = self.combinations[5:]
                self.player2_score += 800
            elif self.combinations.count(2) == 4:
                self.combinations = self.combinations[4:]
                self.player2_score += 400
            elif self.combinations.count(2) == 3:
                self.combinations = self.combinations[3:]
                self.player2_score += 200

            if self.combinations.count(3) == 6:
                self.combinations.clear()
                self.player2_score += 2400
            elif self.combinations.count(3) == 5:
                self.combinations = self.combinations[5:]
                self.player2_score += 1200
            elif self.combinations.count(3) == 4:
                self.combinations = self.combinations[4:]
                self.player2_score += 600
            elif self.combinations.count(3) == 3:
                self.combinations = self.combinations[3:]
                self.player2_score += 300

            if self.combinations.count(4) == 6:
                self.combinations.clear()
                self.player2_score += 3200
            elif self.combinations.count(4) == 5:
                self.combinations = self.combinations[5:]
                self.player2_score += 1600
            elif self.combinations.count(4) == 4:
                self.combinations = self.combinations[4:]
                self.player2_score += 800
            elif self.combinations.count(4) == 3:
                self.combinations = self.combinations[3:]
                self.player2_score += 400

            if self.combinations.count(5) == 6:
                self.combinations.clear()
                self.player2_score += 4000
            elif self.combinations.count(5) == 5:
                self.combinations = self.combinations[5:]
                self.player2_score += 2000
            elif self.combinations.count(5) == 4:
                self.combinations = self.combinations[4:]
                self.player2_score += 1000
            elif self.combinations.count(5) == 3:
                self.combinations = self.combinations[3:]
                self.player2_score += 500
            elif self.combinations.count(5) == 1:
                self.combinations = self.combinations[1:]
                self.player2_score += 50

            if self.combinations.count(6) == 6:
                self.combinations.clear()
                self.player2_score += 4800
            elif self.combinations.count(6) == 5:
                self.combinations = self.combinations[5:]
                self.player2_score += 2400
            elif self.combinations.count(6) == 4:
                self.combinations = self.combinations[4:]
                self.player2_score += 1200
            elif self.combinations.count(6) == 3:
                self.combinations = self.combinations[3:]
                self.player2_score += 600

    def finish_turn(self):
        self.turn *= -1

    def put_away(self):
        def count_(self):
            pass
