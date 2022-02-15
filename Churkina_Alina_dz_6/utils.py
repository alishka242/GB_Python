def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    list_hob = []
    with open(path_users_file, 'r', encoding='utf-8') as us_name:
        us_name = [x.strip() for x in us_name.readlines()]

    with open(path_hobby_file, 'r', encoding='utf-8') as us_hob:
        us_hob = [x.strip() for x in us_hob.readlines()]

    if len(us_name) < len(us_hob):
        return "None"
    elif len(us_name) > len(us_hob):
        us_hob.append(None)
    for key, val in zip(us_name, us_hob):
        list_hob.append(f'{key}: {val}\n')
    print(*list_hob)
    return  list_hob


def write_in(file_from_1:str, file_from_2:str, file_wr:str):

    dict_out = prepare_dataset(file_from_1, file_from_2)

    with open(file_wr, 'w', encoding='utf-8') as fw:
        for str_h in dict_out:
            fw.write(str_h)