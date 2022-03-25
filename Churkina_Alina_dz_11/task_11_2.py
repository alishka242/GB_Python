from checker_error import MyErrorDivisionZero, CheckVal, MyErrIsInt

class Division:
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2

    def get_res_div(self):
        flag = 0
        try:
            self.par1 = CheckVal.is_int(self.par1) 
            self.par2 = CheckVal.is_int(self.par2)
            
            flag = 1
        except MyErrIsInt as er:
            return(er)
        if self.par2 != 0 and flag == 1:  
            return (self.par1 / self.par2)
        else:
            raise MyErrorDivisionZero
            

if __name__ == "__main__":
    try:
        par1 = input('Введите делимое: ')
        par2 = input('Введите делитель: ')
        div = Division(par1, par2)

        print(div.get_res_div())
    except MyErrorDivisionZero as e:
        print(e)
    except MyErrorDivisionZero as e:
        print(e)