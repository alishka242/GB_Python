list_out = list()

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for str_fr in fr:
        list_out.append(fr.readline().split(" ")[0])

def get_spam_info(data_list):
    dict_ip_adr = {}

    for i in data_list:
        if dict_ip_adr.get(i) is None:
            dict_ip_adr.setdefault(i, 1)
        else:
            dict_ip_adr[i] += 1
    
    spam = list(dict_ip_adr.popitem())

    for el in dict_ip_adr:
        if dict_ip_adr[el] > spam[1]:
            spam[0] = el
            spam[1] = dict_ip_adr[el]

    return spam

print(get_spam_info(list_out))