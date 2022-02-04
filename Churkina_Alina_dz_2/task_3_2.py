from task_3_1 import num_translate

def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский. И первую букву делает заглавной"""

    return num_translate(value.lower()).capitalize()

print("\nпереводит числительное с английского на русский")
"""Вызов ф-ии первого задания"""
print(f'\nt_3_1: {num_translate("one")}')
print(f't_3_1: {num_translate("eight")}')

"""Вызов ф-ии второго задания"""
print(f'\nt_3_2: {num_translate_adv("one")}')
print(f't_3_2: {num_translate_adv("Eight")}')
print(f't_3_2: {num_translate_adv("eig")}')