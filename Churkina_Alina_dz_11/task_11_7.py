from checker_error import CheckVal, MyErrIsInt

class Operation:

    def plus(self, x, y):
        print ( x + y)

    def minus(self, x, y):
        print( x - y)

    def umnoj(self, x, y):
        print (x * y)

    def delenie(self, x, y):
        print (x / y)

    def modul(self, x, y):
        print (abs(7 + 8j))

    def stepen(self, x, y):
        print (pow(x + y, 2))

if __name__ == '__main__':
    print('Всего Вы введете 4 числа для рассчета!\nx = complex(v1, v2)\ny = complex(v3, v4)')
    v1 = input(f'Введите v1: ')
    v2 = input(f'Введите v2: ')
    v3 = input(f'Введите v3: ')
    v4 = input(f'Введите v4: ')
    try:
        n_v1 = CheckVal.is_int(v1) 
        n_v2 = CheckVal.is_int(v2) 
        n_v3 = CheckVal.is_int(v3) 
        n_v4 = CheckVal.is_int(v4) 

        obj1 = Operation()
        
        x = complex(n_v1, n_v2)
        y = complex(n_v3, n_v4)
        obj1.plus(x, y)
        obj1.minus(x, y)
        obj1.umnoj(x, y)
        obj1.modul(x, y)
        obj1.delenie(x, y)
        obj1.stepen(x, y)
    except MyErrIsInt as er:
        print(er)
