from hashlib import new
from random import uniform
import re

def transfer_list_in_str(list_in: list) -> str:
    str_out = ''
    for el in list_in:
        pr = str(el).split(".")

        if len(pr[1]) < 2:
            pr[1] = f'0{pr[1]}'
        elif len(pr[1]) < 1:
            pr[1] = '00'
        
        str_out += f'{pr[0]} руб {pr[1]} коп, '
    
    str_out = "Здесь итоговая строка:" + str_out[:-2]
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'\nИсходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    # """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()

    return list_in


# зафиксируйте здесь информацию по исходному списку my_list\
print("\nСписок элементов отсортированный по вызрастанию(только для вещественных чисел")
print(id(my_list))
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)
print(id(result_2))


def sort_price_adv(list_in: list) -> list:
    #"""Создаёт новый список и возвращает список с элементами по убыванию"""
    
    list_out = sorted(list_in, reverse=True)
    return list_out

print("\nСписок элементов отсортированный по убыванию")
print(id(my_list))

result_3 = sort_price_adv(my_list)

print(result_3)
print(id(result_3))


def check_five_max_elements(list_in: list) -> list:
    # """Проверяет элементы входного списка вещественных чисел и возвращает
    #     список из ПЯТИ максимальных значений"""
    
    list_out = sorted(list_in, reverse=True)[:5:]
    return list_out

print("\nСписок из пяти самых больших вещественных чисел")
result_4 = check_five_max_elements(my_list)
print(result_4)