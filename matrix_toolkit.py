import copy
import decimal

# Decimal place to round franctions to
DECIMAL_PLACE = 14

# Returns sum of two matrices
def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        raise ArithmeticError("Incompatible matrices.")

    return_matrix = copy.deepcopy(matrix1)
    for x in range(len(matrix1)):
        if len(matrix1[x]) != len(matrix2[x]):
            raise ArithmeticError("Incompatible matrices.")

        for y in range(len(matrix1[x])):
            return_matrix[x][y] = round(matrix1[x][y] + matrix2[x][y], DECIMAL_PLACE)

    return return_matrix

# Returns difference of two matrices
def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        raise ArithmeticError("Incompatible matrices.")

    return_matrix = copy.deepcopy(matrix1)
    for x in range(len(matrix1)):
        if len(matrix1[x]) != len(matrix2[x]):
            raise ArithmeticError("Incompatible matrices.")

        for y in range(len(matrix1[x])):
            return_matrix[x][y] = round(matrix1[x][y] - matrix2[x][y], DECIMAL_PLACE)

    return return_matrix

# Returns a scaled matrix
def scale_matrix(matrix, scalar):

    return_matrix = copy.deepcopy(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            return_matrix[x][y] *= scalar

    return return_matrix

# Returns the dot product of two vectors
def vector_dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ArithmeticError("Incompatible vectors.")

    sum = 0

    for x in range(len(vector1)):
        sum += vector1[x] * vector2[x]

    return sum

# Returns the transpose of a matrix
def transpose_matrix(matrix):
    transpose = []
    for x in range(len(matrix[0])):
        temp = []
        for y in range(len(matrix)):
            temp.append(matrix[y][x])
        transpose.append(temp)
    
    return transpose

# Returns the product of two matrices
def multiply_matrices(matrix1, matrix2):
    transposed_matrix2 = transpose_matrix(copy.deepcopy(matrix2))

    product = []
    for x in range(len(matrix1)):
        temp = []
        for y in range(len(transposed_matrix2)):
            if len(matrix1[x]) != len(transposed_matrix2[y]):
                raise ArithmeticError("Incompatible matrices.")
            temp.append(vector_dot_product(matrix1[x], transposed_matrix2[y]))
        product.append(temp)

    return product

# Returns the row echelon form of a matrix TODO
def matrix_REF(matrix1):
    return 'TODO'

# Returns the reduced row echelon form of a matrix TODO
def matrix_RREF(matrix1):
    return 'TODO'
