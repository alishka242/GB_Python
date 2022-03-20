def isint(*arg):
    if not int(arg):
        raise ValueError("It's not int!")

def val_checker(func):
    def wrapper(*arg):
        #func(*arg)
        res = func(*arg)
        return res
    return wrapper

    

@val_checker(isint)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))