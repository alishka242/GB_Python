from pprint import pprint

def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    # pass  ()
    list_str = line.split(" ")
    remote_addr = list_str[0]
    request_type = list_str[5][1:]
    requested_resource = list_str[6]
    return remote_addr, request_type, requested_resource  # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>

list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for str_fr in fr:
        list_out.append(get_parse_attrs(fr.readline()))
    
    pass # передавайте данные в функцию и наполняйте список list_out кортежами

pprint(list_out)