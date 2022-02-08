import decimal 
import requests

def get_val_from_xml(res_t, start_ind_code, teg):
    """Ищет тег, чтобы получить значение номинала или валюты в рублях и возвращает это значение"""
    
    ind_nominal = start_ind_code + res_t[start_ind_code:].find(teg) + len(teg) + 1
    nom_numb = ""

    while res_t[ind_nominal:ind_nominal + 1].isnumeric() or res_t[ind_nominal:ind_nominal + 1] == ',':
        if res_t[ind_nominal:ind_nominal + 1] == ',':
            nom_numb += "."
        else: 
            nom_numb += res_t[ind_nominal:ind_nominal + 1]
        ind_nominal += 1

    return nom_numb

def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    nominal = 'Nominal'
    couse_val = 'Value'

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    res_t = str(response.text)
    start_ind_code = res_t.find(code.upper())

    if start_ind_code == -1:
        return None
    
    """Получаем значение номинала"""
    nominal_val = get_val_from_xml(res_t, start_ind_code, nominal)
        
    """Получаем значение переданной валюты в рублях"""
    valute_val_rub = decimal.Decimal(get_val_from_xml(res_t, start_ind_code, couse_val)) / int(nominal_val)

    return valute_val_rub

print(currency_rates("USD"))
print(currency_rates("NOK"))
print(currency_rates("KRW"))
print(currency_rates("noname"))

""" Ответ на вопрос про decimal. Думаю, что в нашем случае есть смысл использовать decimal для большей точности, 
т.к. денежные величины требуют точности для избежания ошибок. Важное замечание! decimal нужно переводить или 
из целого числа (можно с использованием кортедей), либо из строки, как бы это странно не звучало. 
Если переводить в decimal из float, есть вероятность ошибки, т.к. последний округляет до 
ближайшего меньшего/большего числа.
"""