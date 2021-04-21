import copy

# Returns sum of two matrices
def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        raise Exception("Incompatible matrices.")

    return_matrix = copy.deepcopy(matrix1)
    for x in range(len(matrix1)):
        if(len(matrix1[x]) != len(matrix2[x])):
            raise Exception("Incompatible matrices.")

        for y in range(len(matrix1[x])):
            return_matrix[x][y] += matrix2[x][y]

    return return_matrix

# Returns difference of two matrices
def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        raise Exception("Incompatible matrices.")

    return_matrix = copy.deepcopy(matrix1)
    for x in range(len(matrix1)):
        if(len(matrix1[x]) != len(matrix2[x])):
            raise Exception("Incompatible matrices.")

        for y in range(len(matrix1[x])):
            return_matrix[x][y] -= matrix2[x][y]

    return return_matrix

# Returns a scaled matrix
def scale_matrix(matrix1, scalar):

    return_matrix = copy.deepcopy(matrix1)
    for x in range(len(matrix1)):
        for y in range(len(matrix1[x])):
            return_matrix[x][y] *= scalar

    return return_matrix


def main():
    matrix1 = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    
    matrix2 = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    
    print(add_matrices(matrix1, matrix2))
    print(subtract_matrices(matrix1, matrix2))
    print(scale_matrix(matrix1, 4))

if __name__ == '__main__':
    main()