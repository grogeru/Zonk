from random import choice


class Game:
    def __init__(self, combination):
        self.turn = choice((1, -1))
        self.player1_score = 0
        self.player2_score = 0
        self.comb_plus_throw = {(1, 2, 3, 4, 5, 6): 1000, (1, 1, 2, 2, 3, 3): 750}
        self.combinations = combination
        self.list_of_pars = [[1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 4, 4], [1, 1, 2, 2, 5, 5],
                             [1, 1, 2, 2, 6, 6], [1, 1, 3, 3, 4, 4], [1, 1, 3, 3, 5, 5],
                             [1, 1, 3, 3, 6, 6], [1, 1, 4, 4, 5, 5], [1, 1, 4, 4, 6, 6],
                             [1, 1, 5, 5, 6, 6], [2, 2, 3, 3, 4, 4], [2, 2, 3, 3, 5, 5],
                             [2, 2, 3, 3, 6, 6], [2, 2, 4, 4, 5, 5], [2, 2, 4, 4, 6, 6],
                             [3, 3, 4, 4, 5, 5], [3, 3, 4, 4, 6, 6], [4, 4, 5, 5, 6, 6]]

    def input_comb(self, new_combination):
        self.combinations = new_combination

    def check_combinations_player1(self):
        self.combinations.sort()
        for i in range(4):
            if self.combinations == [1, 2, 3, 4, 5, 6]:
                self.combinations.clear()
                self.player1_score += 1000

            if self.combinations in self.list_of_pars:
                self.combinations.clear()
                self.player1_score += 750

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
            elif self.combinations.count(5) == 2:
                self.combinations.pop(self.combinations.index(5))
                self.combinations.pop(self.combinations.index(5))
                self.player1_score += 100
            elif self.combinations.count(5) == 1:
                self.combinations.pop(self.combinations.index(5))
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

        if self.combinations:
            print('Такой комбинации нет, выберите другую.')
            self.player1_score = 0  # Чтоб не считались неудачные попытки ввода, обнуляем счёт
            self.input_comb(input_list())  # Вводим новую комбинацию, введённую игроком
            self.check_combinations_player1()  # По новой чекаем комбинацию

    def finish_turn(self):
        self.turn *= -1

    def put_away(self):
        def count_(self):
            pass

    def print_score(self):
        return self.player1_score

# Ниже часть кода для проверки правильности вывода счёта комбинации
# Чисто для проверки, потом снесём

comb = []


def input_list():
    global comb
    comb = []
    print('Введи кол-во кубиков, которое выбрал юзер')
    x = int(input())
    print('Вводи значение на кубах по одному')
    for i in range(x):
        comb.append(int(input()))
    return comb


input_list()
test = Game(comb)
test.check_combinations_player1()
print(f'Юзер заработал: {str(test.print_score())} очков')
