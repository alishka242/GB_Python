import re
from pprint import pprint

def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    ip_add = re.compile(r'(?:\d*\.){3}\d*') #'188.138.60.101'
    time_is = re.compile(r'\d*\/\w*\/(?:\d*\:){3}\d+\s\+\d*') #'17/May/2015:08:05:49 +0000'
    API_req = re.compile(r'GET|POST') #'GET'
    uri = re.compile(r'\/\w*\/[a-z]*\_\d') #'/downloads/product_2'
    resp_str = re.compile(r' \d* \d*') #'304', '0'

    list_str = ip_add.findall(line)[0]
    
    pprint(list_str)

list_out = list()

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for str_fr in fr:
        # parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
        list_out.append(get_parse_attrs(fr.readline()))

#print(list_out)