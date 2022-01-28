def transform_string(number: int) -> str:
    #Возвращает строку вида 'N процентов' с учётом склонения по указанному number
    str1 = ' процент'
    str2 = ' процента'
    str3 = ' процентов'
    list2 = [2, 3, 4]
    list3 = [5, 6, 7, 8, 9, 0]

    if (number % 10) == 1:
            return str(number) + str1

    for val in list2:
        if (number % 10) == val:
            return str(number) + str2

    return str(number) + str3

for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))