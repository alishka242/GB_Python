class MyErrorDivisionZero(Exception):
    err_message = 'В школе не учили, что на 0 делить нельзя?'

    def __str__(self) -> str:
        return self.err_message

class MyErrIsInt(Exception):
    err_message = 'Ошибка при вводе, Вы ввели не число.'

    def __str__(self) -> str:
        return self.err_message

class CheckVal:
    def is_int(par):

        if par.isnumeric():
            par = int(par)
            return par
        else:
            raise MyErrIsInt