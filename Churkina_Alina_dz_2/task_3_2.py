def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский. Захотела применить новые функции в решении задачки:)"""

    eng_numb = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")
    rus_numb = ("один", "два", "три", "четыре", "пять", "шесть", "семь ","восемь", "девять", "десять")
    dict_numb = dict(zip(eng_numb, rus_numb))

    return dict_numb.get(value.lower(), "ошибка в написании или число больше 10").capitalize()

print(num_translate_adv("one"))
print(num_translate_adv("Eight"))
print(num_translate_adv("eig"))