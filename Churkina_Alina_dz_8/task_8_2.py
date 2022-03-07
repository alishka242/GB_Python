import re
from pprint import pprint

ip_add = re.compile(r'[0-9]*\.{4}')

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for str_fr in fr:
        # parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
        # print(ip_add.findall(str_fr))
        pprint(str_fr)
