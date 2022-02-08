import requests
import datetime

def get_val_from_xml(res_t, start_ind_code, teg):
    """Ищет тег, чтобы получить значение номинала или валюты в рублях и возвращает это значение"""
    
    ind_nominal = start_ind_code + res_t[start_ind_code:].find(teg) + len(teg) + 1
    nom_numb = ""

    while res_t[ind_nominal:ind_nominal + 1].isnumeric() or res_t[ind_nominal:ind_nominal + 1] == ',' or res_t[ind_nominal:ind_nominal + 1] == '.':
        if res_t[ind_nominal:ind_nominal + 1] == ',':
            nom_numb += "."
        else: 
            nom_numb += res_t[ind_nominal:ind_nominal + 1]
        ind_nominal += 1

    return nom_numb

def currency_rates_adv(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    nominal = 'Nominal'
    couse_val = 'Value'
    val_curs_date = 'ValCurs Date='

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    res_t = str(response.text)
    start_ind_date = res_t.find(val_curs_date)
    
    date_val = get_val_from_xml(res_t, start_ind_date, val_curs_date)
    date_val = datetime.datetime(year=int(date_val[6:]), month=int(date_val[3:5]), day=int(date_val[0:2]))

    start_ind_code = res_t.find(code.upper())

    if start_ind_code == -1:
        return None, date_val
    
    """Получаем значение номинала"""
    nominal_val = get_val_from_xml(res_t, start_ind_code, nominal)
        
    """Получаем значение переданной валюты в рублях"""
    valute_val_rub = float(get_val_from_xml(res_t, start_ind_code, couse_val)) / int(nominal_val)

    return valute_val_rub, date_val

kurs, date_value = currency_rates_adv("USD")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)