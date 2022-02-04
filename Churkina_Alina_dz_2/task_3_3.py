def thesaurus(*args) -> dict:
    dict_out = {}

    for i in args:
        if dict_out.get(i[0]) is not None:
            dict_out.get(i[0]).append(i)
        else:
            dict_out.setdefault(i[0], [i])
    
    return dict(sorted(dict_out.items(), key = lambda x: x[0]))


# Вызов перенесен в файл task_3_3.py, для того, чтобы результат task_3_4.py был ожидаемым!
# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Игорь", "Андрей"))