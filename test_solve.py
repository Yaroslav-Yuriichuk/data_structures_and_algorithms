import unittest
from main import solve


class TestSolve(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(solve('101101101', 5), 3)

    def test_2(self):
        self.assertEqual(solve('1111101', 5), 1)

    def test_3(self):
        self.assertEqual(solve('110011011', 5), 3)

    def test_4(self):
        self.assertEqual(solve('100111011110100100111110110011100101000111100101110010' +
            '001100111011110100100111110110011100101000110010110000111100101110010001', 7), 5)

    def test_5(self):
        self.assertEqual(solve('111111', 1), 6)

    def test_6(self):
        self.assertEqual(solve('111101', 1), -1)

    def test_7(self):
        self.assertEqual(solve('111101', 2), 5)    

    def test_8(self):
        self.assertEqual(solve('10000000000000', 2), 1)

    def test_9(self):
        self.assertEqual(solve('10001000100001000', 2), 4)        