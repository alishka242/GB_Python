def type_logger(func):

    def wraper(*arg):
        str_resp = ''
        # создаю list comprehensions
        cube_info = [f'{func(numb)}: {type(func(numb))}' for numb in arg]
        # переворачиваю список, потому что 
        cube_info.reverse()

        while len(cube_info) > 1: 
            str_resp += cube_info.pop() + ', '
        
        str_resp += cube_info.pop()

        return str_resp

    return wraper

@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5, 6)
print(a)