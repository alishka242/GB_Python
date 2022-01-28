def sum_list_1(dataset: list) -> int:
    # Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7
    sum = 0
    for el in dataset:
        el_list = [int(a) for a in str(el)]
        numb_sum = 0

        for numb in el_list:
            numb_sum += numb
            
        if ((numb_sum % 7) == 0):
            sum += el
        numb_sum = 0

    return sum # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    #К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, 
    #сумма цифр которых делится нацело на 7
    sum = 0
    for el in dataset:
        el += 17
        el_list = [int(a) for a in str(el)]
        numb_sum = 0

        for numb in el_list:
            numb_sum += numb
            
        if ((numb_sum % 7) == 0):
            sum += el
        numb_sum = 0

    return sum  # Верните значение полученной суммы


my_list = []  # Соберите нужный список по заданию
start_val = 1
finish_val = 1000

while start_val < finish_val:
    if ((start_val % 2) != 0 or (start_val == 1)):
        new_val = start_val ** 3
        my_list.append(new_val)
    start_val += 1

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)