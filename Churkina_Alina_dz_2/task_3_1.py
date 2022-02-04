def num_translate(value: str) -> str:
    """переводит числительное с английского на русский. Захотела применить новые функции в решении задачки:)"""

    eng_numb = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")
    rus_numb = ("один", "два", "три", "четыре", "пять", "шесть", "семь ","восемь", "девять", "десять")
    dict_numb = dict(zip(eng_numb, rus_numb))

    return dict_numb.get(value, "Ошибка в написании или число больше 10")

# Перенесла вызов ф-ии в файл task_3_2.py, чтобы результат task_3_2.py был ожидаемым!
# print(num_translate("one"))
# print(num_translate("eight"))