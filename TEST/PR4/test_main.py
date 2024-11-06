import unittest

def reflect_matrix(matrix):
    return matrix[::-1]

class TestReflectMatrix(unittest.TestCase):

    def test_reflect_2x2(self):
        self.assertEqual(reflect_matrix([[1, 2], [3, 4]]), [[3, 4], [1, 2]])

    def test_reflect_3x3(self):
        self.assertEqual(reflect_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 8, 9], [4, 5, 6], [1, 2, 3]])

    def test_reflect_empty_matrix(self):
        self.assertEqual(reflect_matrix([[]]), [[]])

    def test_reflect_single_element_matrix(self):
        self.assertEqual(reflect_matrix([[42]]), [[42]])

    def test_reflect_1x3(self):
        self.assertEqual(reflect_matrix([[1, 2, 3]]), [[1, 2, 3]])

if __name__ == '__main__':
    unittest.main()