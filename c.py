from random import choice


class Dice:
    def __init__(self):
        self.throws = (1, 2, 3, 4, 5, 6)

    def throw(self):
        return choice(self.throws)


first_dice = Dice()
