class Date:
    def __init__(self, date: str):
        self.date = date
    
    @classmethod
    def change_type_on_int(cls, date):
        list_date = [int(val) for val in date.split('.')]
        # cls.day = int(date[0])
        # cls.month = int(date[1])
        # cls.year = int(date[2])
        return list_date

    @staticmethod
    def check_day(day, max_day):
        return True if (day == 1 or day <= max_day) else False

    @staticmethod
    def get_len_d_m_2(val):
        if len(val) == 1 and val.isnumeric():
            return '0' + val
        if len(val) == 2 and int(val):
            return val
        else:
            return False

    @staticmethod
    def check_date(date: str):
        err_mess ='Вы ошиблись при указании даты. Мы ожидаем дату в виде dd.mm.yyyy в виде строки.\n'
        
        if not isinstance(date, str):
            raise ValueError(err_mess)

        list_date = [val for val in date.split('.')]

        if not Date.get_len_d_m_2(list_date[0]) and not Date.get_len_d_m_2(list_date[1]):
            raise ValueError(err_mess)

        list_date[0] = Date.get_len_d_m_2(list_date[0])
        list_date[1] = Date.get_len_d_m_2(list_date[1])
        flag = False

        if list_date[1] != '02' and (list_date[1] == '01' or list_date[1] <= '12'):
            if int(list_date[1]) % 2 and Date.check_day(list_date[0], '31'):
                flag = True
            if Date.check_day(list_date[0], '30'):
                flag = True
        else: 
            if list_date[1] == '02' and Date.check_day(list_date[0], '28'):
                flag = True

        if len(list_date[2]) != 4:
            flag = False

        if flag:
            return "Дата принята!\n"
        else:
            return err_mess

if __name__ == '__main__':
    date = Date('22.02.1987')

    print(Date.change_type_on_int('13.04.1244'))
    print(date.change_type_on_int('22.02.1987'))
    print(Date.check_date('13.05.1353'))
    print(Date.check_date(11))