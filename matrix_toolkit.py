import copy

# Returns sum of two matrices
def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        raise ArithmeticError("Incompatible matrices.")

    return_matrix = copy.deepcopy(matrix1)
    for x in range(len(matrix1)):
        if len(matrix1[x]) != len(matrix2[x]):
            raise ArithmeticError("Incompatible matrices.")

        for y in range(len(matrix1[x])):
            return_matrix[x][y] += matrix2[x][y]

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
            return_matrix[x][y] -= matrix2[x][y]

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

# Returns the transpose of a matrix TODO
def transpose_matrix(matrix):
    return "TODO"

# Returns the product of two matrices TODO
def multiply_matrices(matrix1, matrix2):
    return "TODO"

