from random import choice
from _collections import OrderedDict
import time
from comb_check import check_if_there_is_a_combination as mass_check


class Game:
    def __init__(self):
        self.turn = choice((1, -1))  # 1 - первый игрок, -1 - второй игрок
        self.player1_score = 0
        self.player2_score = 0
        self.player1_deck = []
        self.player2_deck = []

    def finish_turn(self):
        self.turn *= -1

    def add_cube(self, dice):
        if self.turn == 1:
            if len(self.player1_deck) < 6:
                self.player1_deck.append(dice)
                print(f"Кость {dice} добавлена в колоду первого игрока")
            else:
                print("В колоде уже хватает кубиков для игры!")
        else:
            if len(self.player2_deck) < 6:
                self.player2_deck.append(dice)
                print(f"Кость {dice} добавлена в колоду второго игрока")
            else:
                print("В колоде уже хватает кубиков для игры!")

    def make_throw(self):
        players_deck = self.choose_deck()
        res = [each_dice.throw for each_dice in players_deck]
        # print(*res)
        return res

    def choose_deck(self):
        if self.turn == 1:
            return self.player1_deck.copy()
        else:
            return self.player2_deck.copy()

    def have_turn(self, lst):
        return mass_check(lst)[1]

    def someone_has_won(self):
        if self.turn == 1 and self.player2_score >= 5000:
            print("Игрок №2 победил!")
            return True
        elif self.turn == -1 and self.player1_score >= 5000:
            print("Игрок №1 победил!")
            return True
        else:
            return False

    def put_away(self):
        def count(self):
            pass

    def whos_turn(self):
        if self.turn == 1:
            print("Ходит игрок №1")
        else:
            print("Ходит игрок №2")

    def make_turn(self):  # (choose_deck())

        print("Игра начинается!")  # объявление о начале игры и о праве первого хода
        self.whos_turn()

        while not self.someone_has_won():
            pass
