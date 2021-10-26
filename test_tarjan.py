import unittest
from tarjan_scc import tarjan_scc


class TestRecursiveDFS(unittest.TestCase):
    
    def test_1(self):
        graph = [
            [1, 2],
            [0],
            [3],
            [5],
            [4],
            [2]
        ]

        self.assertEqual([[0, 1], [2, 3, 5], [4]], tarjan_scc(graph))


    def test_2(self):
        graph = [
            [],
            [2],
            [3],
            [1],
            [0, 2, 6],
            [4],
            [5]
        ]

        self.assertEqual([[0], [1, 2, 3], [4, 5, 6]], tarjan_scc(graph))


    def test_3(self):
        graph = [
            [],
            [],
            [],
            []
        ]

        self.assertEqual([[0], [1], [2], [3]], tarjan_scc(graph))