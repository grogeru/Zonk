# на вход в каждую функцию подается отсортированный массив -- результат выпадения каждого из кубиков, а также Counter
from collections import Counter

data_check_all_of_a_kind = {1: 6000, 2: 1600, 3: 2400, 4: 3200, 5: 4000, 6: 4800}
data_check_for_5 = {1: 3000, 2: 800, 3: 1200, 4: 1600, 5: 2000, 6: 2400}
data_check_for_4 = {1: 2000, 2: 400, 3: 600, 4: 800, 5: 1000, 6: 1200}
data_check_for_3 = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
data_check_for_1 = {1: 100, 5: 50}


def check_1_2_3_4_5_6(lst):
    if lst == [1, 2, 3, 4, 5, 6]: # 1
        return 1000

def check_3_pair(lst):
    if len(set(lst)) == 3 and lst[0] == lst[1] and lst[2] == lst[3] and lst[4] == lst[5]: # 4
        return 750

def check_all_of_a_kind(lst): # 1
    if len(set(lst)) == 1:
        return data_check_all_of_a_kind[lst[0]]


def check_for_5(count):
    for num in count:
        if count[num] == 5:
            return data_check_for_5[num]

def check_for_4(count): # count = Counter(lst) # 6
    for num in count:
        if count[num] == 4:
            return data_check_for_4[num]

def check_for_3(count): # 6
    for num in count:  # if len(set(lst)) == 2 and lst[2] != lst[3]:
        if count[num] == 3:
            return data_check_for_3[num]

def check_for_1(count):
    for num in count:
        if count[num] == 1 or count[num] == 2:
            if num == 1:
                return 100 * count[num]
            elif num == 5:
                return 50 * count[num]
            else:
                return None

def check_if_there_is_a_combination(smth):
    lst = sorted(smth.copy())
    count= Counter(lst)
    if any([check_1_2_3_4_5_6(lst), check_3_pair(lst), check_all_of_a_kind(lst), check_for_5(count), check_for_4(count),
            check_for_3(count), check_for_1(count)]):
        return "есть контакт"
    else:
        return "иди нахуй"
