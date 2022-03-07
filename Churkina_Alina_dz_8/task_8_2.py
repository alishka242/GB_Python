import re
from pprint import pprint

def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    ip_add = re.compile(r'(?:\d*\.){3}\d*') #'188.138.60.101'
    time_is = re.compile(r'\d*\/\w*\/(?:\d*\:){3}\d+\s\+\d*') #'17/May/2015:08:05:49 +0000'
    API_req = re.compile(r'GET|POST') #'GET'
    uri = re.compile(r'\/\w*\/[a-z]*\_\d') #'/downloads/product_2'
    resp = re.compile(r' \d* \d*') #'304', '0'

    ip_add_list = ip_add.search(line)[0] if ip_add.search(line) else 'Not found'
    time_is_list = time_is.search(line)[0] if time_is.search(line) else 'Not found'
    API_req_list = API_req.search(line)[0] if API_req.search(line) else 'Not found'
    uri_list = uri.search(line)[0] if uri.search(line) else 'Not found'
    resp_str = resp.findall(line)[0] if resp.search(line) else 'Not found'
    resp_str_list= resp_str.split(' ')
    
    return f"{ip_add_list} {time_is_list} {API_req_list} {uri_list} {resp_str_list[1]} {resp_str_list[2]}"

list_out = list()

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for str_fr in fr:
        # parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
        list_out.append(get_parse_attrs(fr.readline()))

pprint(list_out)