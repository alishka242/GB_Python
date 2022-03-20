from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        for list_numb in matrix:
            if (len(matrix) == 3 and len(list_numb) == 2 and len(list_numb) == len(matrix[0])) or (len(matrix) == 2 and len(list_numb) == 4 and len(list_numb) == len(matrix[0])) or (len(matrix) == 3 and len(list_numb) == 3 and len(list_numb) == len(matrix[0])):
                self.matrix = matrix   
            else:
                raise ValueError ('fail initialization matrix')
                            
    def __str__(self) -> str:
        self.martix_str = ""
        for row in self.matrix:
            row_str= [str(r_str) for r_str in row]
            self.martix_str += f'| {" ".join(row_str)} |\n'

        return self.martix_str 

    def __add__(self, other):
        new_list =  [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(new_list)

if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    print(fail_matrix)
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
