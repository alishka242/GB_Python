from random import choice


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int = 1, **kwarg) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []

    while count > 0:
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        count -= 1

    return list_out 


print(get_jokes(2))
print(get_jokes(10))
print(get_jokes())


# Голова уже не варит :|

# # Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы 
# def get_jokes_adv(count: int = 1, flag: bool = 1) -> list:
#     """Аргументы: 

#     count - определяет кол-во возвращаемых шуток
#     flag - определяет можно повторять использованные слова для шуток или нет(1, 0 соответственно)

#     """

#     get_jokes(count, flag)

#     return []

# get_jokes_adv(2, 0)