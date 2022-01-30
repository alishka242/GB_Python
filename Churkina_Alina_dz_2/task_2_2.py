def chenge_numb_str(numb_str: str) -> str:
    if len(numb_str) < 2:
        numb_str = f'0{numb_str}' 
    if (numb_str[0:1:] == '+' or numb_str[0:1:] == '-') and len(numb_str[1::]) < 2:
        mark = numb_str[0:1:]
        numb_str = f'{mark}0{numb_str[1::]}'

    numb_str = f'{numb_str}'

    return numb_str

def convert_list_in_str(list_in: list) -> str:
    i = 0
    str_out = ''

    for el in list_in:
        if el.isnumeric() or el[1::].isnumeric():
            el = f'"{chenge_numb_str(el)}"'
 
        list_in.insert(i, el)
        i =  i + 1
        list_in.remove(list_in[i])

    str_out = ' '.join(list_in)

    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)

print(result)