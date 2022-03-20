import re

def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(^\w*)[\@](\w*[\.]+\w{2}$|\w*[\.]+\w{3}$)')
    dict_emails = {'username': RE_MAIL.findall(email)[0][0], 'domain': RE_MAIL.findall(email)[0][1]}
    
    if dict_emails:
        return dict_emails
    else:
        raise ValueError (f'wrong email: {email}')

if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrains.com')
    email_parse('someone@geekbrains.rugdf')
    email_parse('someone@geekbrainsru')
    email_parse('@geekbrainsru')