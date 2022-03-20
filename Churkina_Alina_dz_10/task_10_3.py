from ctypes import resize

class Cell:
    def __init__(self, cells: int):
        self.cells = cells
    
    def make_order(self, number: int) -> str:
        self.str_stars = ''
        val = self.cells
        while val > 0:
            if val // number:
                self.str_stars += '*' * number + '\n'
            else:
                self.str_stars += '*' * val + '\n'
            val -= number
        return self.str_stars

    # def check_type(self):
    #     if not isinstance(self, Cell):
    #         raise ValueError('действие допустимо только для экземпляров того же класса')
            

    def __add__(self, others):
        check_type(self)
        check_type(others)

        return Cell(self.cells + others.cells)

    def __sub__(self, others):
        check_type(self)
        check_type(others)

        if self.cells <= others.cells:   
            raise ValueError('недопустимая операция')
        return Cell(self.cells - others.cells)

    def __mul__(self, others):
        check_type(self)
        check_type(others)

        return Cell(self.cells * others.cells)

    def __truediv__(self, others):
        check_type(self)
        check_type(others)

        return Cell(int(self.cells / others.cells))

    def __floordiv__(self, others):
        check_type(self)
        check_type(others)

        return Cell(int(self.cells // others.cells))

def check_type(self):
    if not isinstance(self, Cell):
        raise TypeError('действие допустимо только для экземпляров того же класса')
             

if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса