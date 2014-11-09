import unittest

from ..multiplyMatrix import *

class TestMatrixMult(unittest.TestCase):

    def setUp(self):
        self.A = [[2]]
        self.B = [[3]]

    def test_multply(self):
        self.assertEqual( mult(self.A,self.B), [[6]])

if __name__ == '__main__':
    unittest.main()
