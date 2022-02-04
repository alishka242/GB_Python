from task_3_3 import thesaurus

def turn_over_str(args):
    list_name = []

    for i in args:
        list_name.append(f'{i.split(" ")[1]} {i.split(" ")[0]}')

    return list_name
    

def thesaurus_adv(*args):
    list_name = turn_over_str(args)
    dict_names = thesaurus(*list_name)
    dict_names_2 = {}
    
    for i in dict_names:
        dict_items = {i: thesaurus(*turn_over_str(dict_names[i]))}
        dict_names_2.update(dict_items)

    return dict_names_2


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Игорь", "Андрей"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))