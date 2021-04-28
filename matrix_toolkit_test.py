import unittest
import matrix_toolkit

# Decimal place to round franctions to
DECIMAL_PLACE = 14


class TestMatrixToolkit(unittest.TestCase):

    # Test matrix_toolkit's add_matrices method
    def test_add_matrices(self):

        # Test adding two matrices with different dimensions
        matrix_1 = [[1, 2], [3, 4]]
        matrix_2 = [[1, 2], [3, 4], [5, 6]]

        try:
            matrix_toolkit.add_matrices(matrix_1, matrix_2)
            self.fail()
        except ArithmeticError as e:
            self.assertEqual("Incompatible matrices.", e.args[0])

        # Test adding two 2x2 matrices
        matrix_1 = [[1, 2], [3, 4]]
        matrix_2 = [[1, 2], [3, 4]]

        resultant_matrix = [[2, 4], [6, 8]]

        self.assertEqual(matrix_toolkit.add_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test adding two 3x3 matrices
        matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        resultant_matrix = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

        self.assertEqual(matrix_toolkit.add_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test adding two 5x2 matrices
        matrix_1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        matrix_2 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

        resultant_matrix = [[2, 4], [6, 8], [10, 12], [14, 16], [18, 20]]

        self.assertEqual(matrix_toolkit.add_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test adding two 2x5 matrices
        matrix_1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        matrix_2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

        resultant_matrix = [[2, 4, 6, 8, 10], [12, 14, 16, 18, 20]]

        self.assertEqual(matrix_toolkit.add_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test adding two 2x5 matrices with negative elements
        matrix_1 = [[1, 2, -3, 4, -5], [-6, 7, 8, -9, -10]]
        matrix_2 = [[-1, -2, 3, -4, 5], [6, 7, -8, -9, -10]]

        resultant_matrix = [[0, 0, 0, 0, 0], [0, 14, 0, -18, -20]]

        self.assertEqual(matrix_toolkit.add_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test adding two 2x5 matrices with float elements
        matrix_1 = [[1 / 34, 2 / 27, 3 / 654, 4 / 932, 5], [6, 7, 8 / 543, 9, 10 / 3]]
        matrix_2 = [[1 / 5, 2 / 2, 3 / 7, 4 / 332, 5 / 1234432], [6 / 342, 7, 8, 9 / 43, 10]]

        resultant_matrix = [[39 / 170, 29 / 27, 661 / 1526, 316 / 19339, 6172165 / 1234432],
                            [343 / 57, 14, 4352 / 543, 396 / 43, 40 / 3]]
        for x in range(len(resultant_matrix)):
            for y in range(len(resultant_matrix[x])):
                resultant_matrix[x][y] = round(resultant_matrix[x][y], DECIMAL_PLACE)

        self.assertEqual(matrix_toolkit.add_matrices(matrix_1, matrix_2), resultant_matrix)

    # Test matrix_toolkit's subtract_matrices method
    def test_subtract_matrices(self):
        # Test subtracting two matrices with different dimensions - causes ArithmeticError
        matrix_1 = [[1, 2], [3, 4]]
        matrix_2 = [[1, 2], [3, 4], [5, 6]]

        try:
            matrix_toolkit.subtract_matrices(matrix_1, matrix_2)
            self.fail()
        except ArithmeticError as e:
            self.assertEqual("Incompatible matrices.", e.args[0])

        # Test subtracting two 2x2 matrices
        matrix_1 = [[1, 2], [3, 4]]
        matrix_2 = [[1, 2], [3, 4]]

        resultant_matrix = [[0, 0], [0, 0]]

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test subtracting two 3x3 matrices
        matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

        resultant_matrix = [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]]

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test subtracting two 5x2 matrices
        matrix_1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        matrix_2 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

        resultant_matrix = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test subtracting two 2x5 matrices
        matrix_1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        matrix_2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

        resultant_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test subtracting two 2x5 matrices with negative elements
        matrix_1 = [[1, 2, -3, 4, -5], [-6, 7, 8, -9, -10]]
        matrix_2 = [[-1, -2, 3, -4, 5], [6, 7, -8, -9, -10]]

        resultant_matrix = [[2, 4, -6, 8, -10], [-12, 0, 16, 0, 0]]

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test subtracting two 2x5 matrices with float elements
        matrix_1 = [[1 / 34, 2 / 27, 3 / 654, 4 / 932, 5], [6, 7, 8 / 543, 9, 10 / 3]]
        matrix_2 = [[1 / 5, 2 / 2, 3 / 7, 4 / 332, 5 / 1234432], [6 / 342, 7, 8, 9 / 43, 10]]

        resultant_matrix = [[-29 / 170, -25 / 27, -647 / 1526, -150 / 19339, 6172155 / 1234432],
                            [341 / 57, 0, -4336 / 543, 378 / 43, -20 / 3]]
        for x in range(len(resultant_matrix)):
            for y in range(len(resultant_matrix[x])):
                resultant_matrix[x][y] = round(resultant_matrix[x][y], DECIMAL_PLACE)

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_1, matrix_2), resultant_matrix)

    # Test matrix_toolkit's scale_matrix method
    def test_scale_matrices(self):

        # Test scaling a 2x2 matrix by 4
        scalar = 4
        matrix = [[1, 2], [3, 4]]

        resultant_matrix = [[4, 8], [12, 16]]

        self.assertEqual(matrix_toolkit.scale_matrix(matrix, scalar), resultant_matrix)

        # Test scaling a 3x3 matrix by -2
        scalar = -2
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        resultant_matrix = [[-2, -4, -6], [-8, -10, -12], [-14, -16, -18]]

        self.assertEqual(matrix_toolkit.scale_matrix(matrix, scalar), resultant_matrix)

        # Test scaling a 5x2 matrix by -5
        scalar = -5
        matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

        resultant_matrix = [[-5, -10], [-15, -20], [-25, -30], [-35, -40], [-45, -50]]

        self.assertEqual(matrix_toolkit.scale_matrix(matrix, scalar), resultant_matrix)

        # Test scaling a 2x5 matrix by 0
        scalar = 0
        matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

        resultant_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        self.assertEqual(matrix_toolkit.scale_matrix(matrix, scalar), resultant_matrix)

    # Test matrix_toolkit's vector_dot_product method
    def test_vector_dot_product(self):
        # Test getting dot product of vectors with differing size
        vector_1 = [1, 2]
        vector_2 = [1, 2, 3]

        try:
            matrix_toolkit.vector_dot_product(vector_1, vector_2)
            self.fail()
        except ArithmeticError as e:
            self.assertEqual("Incompatible vectors.", e.args[0])

        # Test getting dot product of 2-element vectors 
        vector_1 = [1, 2]
        vector_2 = [3, 4]

        dot_product = 11

        self.assertEqual(matrix_toolkit.vector_dot_product(vector_1, vector_2), dot_product)
        self.assertEqual(matrix_toolkit.vector_dot_product(vector_2, vector_1), dot_product)

        # Test getting dot product of 2-element vectors with negatives 
        vector_1 = [-1, -2]
        vector_2 = [3, -4]

        dot_product = 5

        self.assertEqual(matrix_toolkit.vector_dot_product(vector_1, vector_2), dot_product)
        self.assertEqual(matrix_toolkit.vector_dot_product(vector_2, vector_1), dot_product)

        # Test getting dot product of 10-element vectors 
        vector_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        vector_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        dot_product = 935

        self.assertEqual(matrix_toolkit.vector_dot_product(vector_1, vector_2), dot_product)
        self.assertEqual(matrix_toolkit.vector_dot_product(vector_2, vector_1), dot_product)

    # Test matrix_toolkit's transpose_matrix method
    def test_transpose_matrix(self):
        # Test transposing a 1x2 matrix then reversing the transpose
        matrix = [[1, 2]]

        resultant_matrix = [[1], [2]]

        self.assertEqual(matrix_toolkit.transpose_matrix(matrix), resultant_matrix)
        self.assertEqual(matrix_toolkit.transpose_matrix(matrix_toolkit.transpose_matrix(matrix)), matrix)

        # Test transposing a 3x3 matrix then reversing the transpose
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        resultant_matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

        self.assertEqual(matrix_toolkit.transpose_matrix(matrix), resultant_matrix)
        self.assertEqual(matrix_toolkit.transpose_matrix(matrix_toolkit.transpose_matrix(matrix)), matrix)

        # Test transposing a 3x8 matrix then reversing the transpose
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24]]

        resultant_matrix = [[1, 9, 17], [2, 10, 18], [3, 11, 19], [4, 12, 20], [5, 13, 21], [6, 14, 22], [7, 15, 23],
                            [8, 16, 24]]

        self.assertEqual(matrix_toolkit.transpose_matrix(matrix), resultant_matrix)
        self.assertEqual(matrix_toolkit.transpose_matrix(matrix_toolkit.transpose_matrix(matrix)), matrix)

    # Test matrix_toolkit's multiply_matrices method
    def test_multiply_matrices(self):
        # Test getting the product of two incompatible matrices
        matrix_1 = [[1, 2, 3], [4, 5, 6]]
        matrix_2 = [[1, 2], [3, 4]]

        try:
            matrix_toolkit.multiply_matrices(matrix_1, matrix_2)
            self.fail()
        except ArithmeticError as e:
            self.assertEqual("Incompatible matrices.", e.args[0])

        # Test getting the product of two 2x2 matrices
        matrix_1 = [[2]]
        matrix_2 = [[2]]

        resultant_matrix = [[4]]

        self.assertEqual(matrix_toolkit.multiply_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test getting the product of two 2x2 matrices
        matrix_1 = [[1, 2], [3, 4]]
        matrix_2 = [[1, 2], [3, 4]]

        resultant_matrix = [[7, 10], [15, 22]]

        self.assertEqual(matrix_toolkit.multiply_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test getting the product of a 1x2 and 2x5 matrix
        matrix_1 = [[1, 2]]
        matrix_2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

        resultant_matrix = [[13, 16, 19, 22, 25]]

        self.assertEqual(matrix_toolkit.multiply_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test getting the product of a 2x1 and 1x5 matrix
        matrix_1 = [[1], [2]]
        matrix_2 = [[1, 2, 3, 4, 5]]

        resultant_matrix = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]]

        self.assertEqual(matrix_toolkit.multiply_matrices(matrix_1, matrix_2), resultant_matrix)

        # Test getting the product of a 5x2 and 2x3 matrix
        matrix_1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        matrix_2 = [[1, 2, 3], [4, 5, 6]]

        resultant_matrix = [[9, 12, 15], [19, 26, 33], [29, 40, 51], [39, 54, 69], [49, 68, 87]]

        self.assertEqual(matrix_toolkit.multiply_matrices(matrix_1, matrix_2), resultant_matrix)

    # # Test matrix_toolkit's matrix_REF method
    # def test_matrix_REF(self):
    #     # Test getting the row echeleon form of a 2x2 matrix
    #     matrix = [[1,2],[3,4]]

    #     resultant_matrix = [[3,4],[0,2/3]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)

    #     # Test getting the row echeleon form of a 2x5 matrix
    #     matrix = [[1,2,3,4,5],[6,7,8,9,10]]

    #     resultant_matrix = [[6,7,8,9,10],[0,5/6,5/3,5/2,10/3]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)

    #     # Test getting the row echeleon form of a 7x3 matrix
    #     matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

    #     resultant_matrix = [[19,20,21],[0,18/19,36/19],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)

    #     # Test getting the row echeleon form of a 4x3 matrix with negative elements
    #     matrix = [[1,2,3],[-4,5,-6],[-7,-8,-9],[10,11,-12]]

    #     resultant_matrix = [[10,11,-12],[0,47/5,-54/5],[0,0,-834/47],[0,0,0]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)

    #     # Test getting the row echeleon form of a 4x3 matrix with float elements
    #     matrix = [[1/3,2/6,3/2],[4/45,5/234,6],[7/98,8,9/1234],[10/3,11/546,12]]

    #     resultant_matrix = [[10/3,11/546,12],[0,203829/25480,-10791/43190],
    #     [0,0,(142/25)+(2045494/3144062325)],[0,0,0]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)

    # # Test matrix_toolkit's matrix_RREF method
    # def test_matrix_RREF(self):
    #     # Test getting the row echeleon form of a 2x2 matrix
    #     matrix = [[1,2],[3,4]]

    #     resultant_matrix = [[1,0],[0,1]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)

    #     # Test getting the row echeleon form of a 2x5 matrix
    #     matrix = [[1,2,3,4,5],[6,7,8,9,10]]

    #     resultant_matrix = [[1,0,-1,-2,-3],[0,1,2,3,4]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)

    #     # Test getting the row echeleon form of a 7x3 matrix
    #     matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

    #     resultant_matrix = [[1,0,-1],[0,1,2],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)

    #     # Test getting the row echeleon form of a 4x3 matrix with negative elements
    #     matrix = [[1,2,3],[-4,5,-6],[-7,-8,-9],[10,11,-12]]

    #     resultant_matrix = [[1,0,0],[0,1,0],[0,0,1],[0,0,0]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)

    #     # Test getting the row echeleon form of a 4x3 matrix with float elements
    #     matrix = [[1/3,2/6,3/2],[4/45,5/234,6],[7/98,8,9/1234],[10/3,11/546,12]]

    #     resultant_matrix = [[1,0,0],[0,1,0],[0,0,1],[0,0,0]]

    #     self.assertEqual(matrix_toolkit.matrix_REF(matrix), resultant_matrix)


if __name__ == '__main__':
    unittest.main()
