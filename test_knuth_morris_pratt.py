import unittest
from knuth_morris_pratt import find


class TestKnuthMorrisPratt(unittest.TestCase):
    
    def test_knuth_morris_pratt_1(self):
        self.assertEqual(find("Hello", ""), 0)

    def test_knuth_morris_pratt_2(self):
        self.assertEqual(find("Hello", "ll"), 2)

    def test_knuth_morris_pratt_3(self):
        self.assertEqual(find("Hello", "elll"), -1)

    def test_knuth_morris_pratt_4(self):
        self.assertEqual(find("Hello, world!", "o, wo"), 4)

    def test_knuth_morris_pratt_5(self):
        self.assertEqual(find("vhdsbvbsdbvdsjkksd", "bsdbv"), 6)

    def test_knuth_morris_pratt_6(self):
        self.assertEqual(find("vhdsbvbsdbvdsjkksd", "bsdbvv"), -1)
