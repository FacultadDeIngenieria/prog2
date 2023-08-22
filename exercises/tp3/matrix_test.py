import unittest

from matrix import (Matrix)


class MatrixTest(unittest.TestCase):
    def test_empty_matrices(self):
        a = Matrix([])
        b = Matrix([])
        c = Matrix([])
        self.assertEqual((a * b).matrix, c.matrix)

    def test_one_by_one(self):
        a = Matrix([[1]])
        b = Matrix([[1]])
        c = Matrix([[1]])
        self.assertEqual((a * b).matrix, c.matrix)

    def test_different_dimensions(self):
        a = Matrix([[1, 2, 3],
                    [4, 5, 6]])

        b = Matrix([[1, 2],
                    [3, 4],
                    [5, 6]])

        c = Matrix([[22, 28],
                    [49, 64]])

        self.assertEqual((a * b).matrix, c.matrix)

    def test_add(self):
        a = Matrix([[1, 2],
                    [4, 5]])

        b = Matrix([[1, 2],
                    [3, 4]])

        self.assertEqual((a + b).matrix, [[2, 4],
                                          [7, 9]])

    def test_invalid_dimensions(self):
        a = Matrix([[1, 2],
                    [4, 5]])

        b = Matrix([[1, 2],
                    [3, 4],
                    [5, 6]])

        with self.assertRaises(ValueError) as err:
            a * b
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Incompatibles dimensions A = 2x2, B = 3x2")

    def test_invalid_multiplication(self):
        a = Matrix([[1, 2],
                    [4, 5]])

        with self.assertRaises(ValueError) as err:
            a * "break"
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Argument should be a Matrix or a scalar int")

    def test_invalid_add(self):
        a = Matrix([[1, 2],
                    [4, 5]])

        b = Matrix([[1, 2]])

        with self.assertRaises(ValueError) as err:
            a + b
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Matrices should have the same dimensions!")

    def test_scalar_multiply(self):
        a = Matrix([[1, 2, 3]])
        b = 2
        self.assertEqual((a * b).matrix, [[2, 4, 6]])

    def test_transpose(self):
        a = Matrix([[1, 2, 3]])
        b = Matrix([[1, 2], [3, 4]])
        c = Matrix([[1, 2], [3, 4], [5, 6]])
        self.assertEqual((~a).matrix, [[1], [2], [3]])
        self.assertEqual((~b).matrix, [[1, 3], [2, 4]])
        self.assertEqual((~c).matrix, [[1, 3, 5], [2, 4, 6]])
