def convert_name_extract(list_in: list) -> list:
    i = 0

    while i < len(list_in):
        new_el = list_in.pop(i) 
        list_in.insert(i, f'Привет, {new_el.split(" ")[-1].capitalize()}!')
        i += 1
        
    return list_in

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)