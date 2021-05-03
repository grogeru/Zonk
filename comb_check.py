# на вход в каждую функцию подается отсортированный массив -- результат выпадения каждого из кубиков, а также Counter
from collections import Counter

data_check_all_of_a_kind = {1: 6000, 2: 1600, 3: 2400, 4: 3200, 5: 4000, 6: 4800}
data_check_for_5 = {}
data_check_for_4 = {1: 2000, 2: 400, 3: 600, 4: 800, 5: 1000, 6: 1200}
data_check_for_3 = {}




def check_1_2_3_4_5_6(lst):
    if lst == [1, 2, 3, 4, 5, 6]: # 1
        return 1000

def check_3_pair(lst):
    if len(set(lst)) == 3 and lst[0] == lst[1] and lst[2] == lst[3] and lst[4] == lst[5]: # 4
        return 750

def check_all_of_a_kind(lst): # 1
    if len(set(lst)) == 1:
        return data_check_all_of_a_kind[lst[0]]


def check_for_5(lst):
    if len(set(lst)) == 2 and (lst[0] != lst[1] or lst[4] != lst[5]): # 3
        if lst.count(1) == 5:
            return 3000
        elif lst.count(2) == 5:
            return 800
        elif lst.count(3) == 5:
            return 800
        elif lst.count(4) == 5:
            return 1600
        elif lst.count(5) == 5:
           return 2000
        else:
            return 2400

def check_for_4(count): # count = Counter(lst) # 6
    for num in count:
        if count[num] == 4:
            return data_check_for_4[num]

def check_for_3(count): # 6
    for num in count:  # if len(set(lst)) == 2 and lst[2] != lst[3]:
        if count[num] == 3:
            return








        #self.combinations = {

                             #   (1, 1, 1, 1): 2000, (6, 6, 6, 6): 1200, (5, 5, 5, 5): 1000, (4, 4, 4, 4): 800, (3, 3, 3, 3): 600, (2, 2, 2, 2): 400,


                             #(1, 1, 1): 1000, (2, 2, 2): 200, (3, 3, 3): 300, (4, 4, 4): 400, (5, 5, 5): 500,
                             #(6, 6, 6): 600, (1): 100, (5): 50}
