# на вход в каждую функцию подается отсортированный массив -- результат выпадения каждого из кубиков, а также Counter
from collections import Counter

# Как нужно отредактироватировать:
#1) Добавить Bul выражение для проверки, что комбинацию нельзя отложить
#2)
#
#
#




data_check_all_of_a_kind = {1: 6000, 2: 1600, 3: 2400, 4: 3200, 5: 4000, 6: 4800}
data_check_for_5 = {1: 3000, 2: 800, 3: 1200, 4: 1600, 5: 2000, 6: 2400}
data_check_for_4 = {1: 2000, 2: 400, 3: 600, 4: 800, 5: 1000, 6: 1200}
data_check_for_3 = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
data_check_for_1 = {1: 100, 5: 50}


def check_1_2_3_4_5_6(lst, count):
    if len(set(lst)) == 6: # 1
        count.clear()
        return 1000

def check_3_pair(lst, count):
    if len(set(lst)) == 3 and lst[0] == lst[1] and lst[2] == lst[3] and lst[4] == lst[5]: # 4
        count.clear()
        return 750

def check_all_of_a_kind(lst, count): # 1
    if len(set(lst)) == 1:
        count.clear()
        return data_check_all_of_a_kind[lst[0]]


def check_for_5(count):
    for num in count:
        if count[num] == 5:
            del count[num]
            return data_check_for_5[num]

def check_for_4(count): # count = Counter(lst) # 6
    for num in count:
        if count[num] == 4:
            del count[num]
            return data_check_for_4[num]

def check_for_3(count): # сделать сумму всех, принудительно пройдясь по всем элементам Counter
    del_list = []
    sum_for_return = 0
    for num in count:  # if len(set(lst)) == 2 and lst[2] != lst[3]:
        if count[num] == 3:
            del_list.append(num)
            sum_for_return += data_check_for_3[num]
    for num in del_list:
        del count[num]
    return sum_for_return

def check_for_1(count):
    del_list = []
    return_sum = 0
    for num in count:
        if count[num] == 1 or count[num] == 2:
            if num == 1:
                return_sum += 100 * count[num]
                del_list.append(num)
            elif num == 5:
                return_sum += 50 * count[num]
                del_list.append(num)
    for item in del_list:
        del count[num]
    return return_sum

def check_if_there_is_a_combination(smth): # smth - откопированный результат бросков кубиков
    lst = sorted(smth.copy())
    count = Counter(lst)
    res = [check_1_2_3_4_5_6(lst, count), check_3_pair(lst, count), check_all_of_a_kind(lst, count), check_for_5(count), check_for_4(count),
            check_for_3(count), check_for_1(count)]
    if any(res): # нашлась хоть какая-нибудь комбинация
        if count: # count остался/не остался пустым
            return sum(filter(lambda x: x, res)), False # в текущем варианте кубики отложить нельзя
        else:
            return sum(filter(lambda x: x, res)), True # можно
    else: # не нашлось, и откладывать нечего
        return 0, False
