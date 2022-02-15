import json

def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    dict_hob = {}
    us_name = [x.strip() for x in open(path_users_file, 'r', encoding='utf-8').readlines()]
    us_hob = [x.strip().split(',') for x in open(path_hobby_file, 'r', encoding='utf-8').readlines()]

    if len(us_name) < len(us_hob):
        return 1
    elif len(us_name) > len(us_hob):
        us_hob.append(None)
    for key, val in zip(us_name, us_hob):
        dict_hob.setdefault(key, val)

    return  dict_hob

dict_out = prepare_dataset('users.csv', 'hobby.csv')

with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)