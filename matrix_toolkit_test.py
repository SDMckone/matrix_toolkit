import unittest
import matrix_toolkit

class TestMatrixToolkit(unittest.TestCase):
    def test_add_matrices(self): 

        # Test adding two matrices with different dimensions
        # TODO

        # Test adding two 2x2 matrices
        matrix_A1 = [[1,2],[3,4]]
        matrix_A2 = [[1,2],[3,4]]

        resultant_matrix_A = [[2,4],[6,8]]

        self.assertEqual(matrix_toolkit.add_matrices(matrix_A1, matrix_A2), resultant_matrix_A)

    
        # Test adding two 3x3 matrices
        matrix_B1 = [[1,2,3],[4,5,6],[7,8,9]]
        matrix_B2 = [[1,2,3],[4,5,6],[7,8,9]]

        resultant_matrix_B = [[2,4,6],[8,10,12],[14,16,18]]

        self.assertEqual(matrix_toolkit.add_matrices(matrix_B1, matrix_B2), resultant_matrix_B)

        # Test adding two 5x2 matrices
        matrix_C1 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
        matrix_C2 = [[1,2],[3,4],[5,6],[7,8],[9,10]]

        resultant_matrix_C = [[2,4],[6,8],[10,12],[14,16],[18,20]]

        self.assertEqual(matrix_toolkit.add_matrices(matrix_C1, matrix_C2), resultant_matrix_C)

        # Test adding two 2x5 matrices
        matrix_D1 = [[1,2,3,4,5],[6,7,8,9,10]]
        matrix_D2 = [[1,2,3,4,5],[6,7,8,9,10]]

        resultant_matrix_D = [[2,4,6,8,10],[12,14,16,18,20]]

        self.assertEqual(matrix_toolkit.add_matrices(matrix_D1, matrix_D2), resultant_matrix_D)

    def test_subtract_matrices(self): 
        # Test subtracting two matrices with different dimensions
        # TODO

        # Test subtracting two 2x2 matrices
        matrix_A1 = [[1,2],[3,4]]
        matrix_A2 = [[1,2],[3,4]]

        resultant_matrix_A = [[0,0],[0,0]]

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_A1, matrix_A2), resultant_matrix_A)

    
        # Test adding two 3x3 matrices
        matrix_B1 = [[1,2,3],[4,5,6],[7,8,9]]
        matrix_B2 = [[1,2,3],[4,5,6],[7,8,9]]

        resultant_matrix_B = [[0,0,0],[0,0,0],[0,0,0]]

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_B1, matrix_B2), resultant_matrix_B)

        # Test adding two 5x2 matrices
        matrix_C1 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
        matrix_C2 = [[1,2],[3,4],[5,6],[7,8],[9,10]]

        resultant_matrix_C = [[0,0],[0,0],[0,0],[0,0],[0,0]]

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_C1, matrix_C2), resultant_matrix_C)

        # Test adding two 2x5 matrices
        matrix_D1 = [[1,2,3,4,5],[6,7,8,9,10]]
        matrix_D2 = [[1,2,3,4,5],[6,7,8,9,10]]

        resultant_matrix_D = [[0,0,0,0,0],[0,0,0,0,0]]

        self.assertEqual(matrix_toolkit.subtract_matrices(matrix_D1, matrix_D2), resultant_matrix_D)
    
    def test_scale_matrices(self): 

        # Test scaling a 2x2 matrix by 4
        scalar_A = 4
        matrix_A = [[1,2],[3,4]]

        resultant_matrix_A = [[4,8],[12,16]]

        self.assertEqual(matrix_toolkit.scale_matrix(matrix_A, scalar_A), resultant_matrix_A)

    
        # Test scaling a 3x3 matrix by -2
        scalar_B = -2
        matrix_B = [[1,2,3],[4,5,6],[7,8,9]]

        resultant_matrix_B = [[-2,-4,-6],[-8,-10,-12],[-14,-16,-18]]

        self.assertEqual(matrix_toolkit.scale_matrix(matrix_B, scalar_B), resultant_matrix_B)

        # Test scaling a 5x2 matrix by -5
        scalar_C = -5
        matrix_C = [[1,2],[3,4],[5,6],[7,8],[9,10]]

        resultant_matrix_C = [[-5,-10],[-15,-20],[-25,-30],[-35,-40],[-45,-50]]

        self.assertEqual(matrix_toolkit.scale_matrix(matrix_C, scalar_C), resultant_matrix_C)

        # Test scaling a 2x5 matrix by 0
        scalar_D = 0
        matrix_D = [[1,2,3,4,5],[6,7,8,9,10]]

        resultant_matrix_D = [[0,0,0,0,0],[0,0,0,0,0]]

        self.assertEqual(matrix_toolkit.scale_matrix(matrix_D, scalar_D), resultant_matrix_D)

        

if __name__ == '__main__':
    unittest.main()