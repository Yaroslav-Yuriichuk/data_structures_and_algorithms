import unittest
from recursive_dfs import recursive_dfs
from iterative_dfs import iterative_dfs


class TestRecursiveDFS(unittest.TestCase):
    
    def test_visited(self):
        graph = [
            [4],
            [2, 5],
            [1, 5],
            [7],
            [0, 6],
            [1, 2, 6],
            [4, 5],
            [3]
        ]

        visited, _ = recursive_dfs(graph, 2)
        self.assertEqual(visited, [True, True, True, False, True, True, True, False])

        visited, _ = recursive_dfs(graph, 5)
        self.assertEqual(visited, [True, True, True, False, True, True, True, False])

        visited, _ = recursive_dfs(graph, 3)
        self.assertEqual(visited, [False, False, False, True, False, False, False, True])

        visited, _ = recursive_dfs(graph, 7)
        self.assertEqual(visited, [False, False, False, True, False, False, False, True])


    def test_previous(self):
        graph = [
            [4],
            [2, 5],
            [1, 5],
            [7],
            [0, 6],
            [1, 2, 6],
            [4, 5],
            [3]
        ]

        _, previous = recursive_dfs(graph, 2)
        self.assertEqual(previous, [4, 2, None, None, 6, 1, 5, None])

        _, previous = recursive_dfs(graph, 5)
        self.assertEqual(previous, [4, 5, 1, None, 6, None, 5, None])

        _, previous = recursive_dfs(graph, 3)
        self.assertEqual(previous, [None, None, None, None, None, None, None, 3])

        _, previous = recursive_dfs(graph, 7)
        self.assertEqual(previous, [None, None, None, 7, None, None, None, None])


class TestIterativeDFS(unittest.TestCase):
    
    def test_visited(self):
        graph = [
            [4],
            [2, 5],
            [1, 5],
            [7],
            [0, 6],
            [1, 2, 6],
            [4, 5],
            [3]
        ]

        visited, _ = iterative_dfs(graph, 2)
        self.assertEqual(visited, [True, True, True, False, True, True, True, False])

        visited, _ = iterative_dfs(graph, 5)
        self.assertEqual(visited, [True, True, True, False, True, True, True, False])

        visited, _ = iterative_dfs(graph, 3)
        self.assertEqual(visited, [False, False, False, True, False, False, False, True])

        visited, _ = iterative_dfs(graph, 7)
        self.assertEqual(visited, [False, False, False, True, False, False, False, True])


    def test_previous(self):
        graph = [
            [4],
            [2, 5],
            [1, 5],
            [7],
            [0, 6],
            [1, 2, 6],
            [4, 5],
            [3]
        ]

        _, previous = iterative_dfs(graph, 2)
        self.assertEqual(previous, [4, 2, None, None, 6, 1, 5, None])

        _, previous = iterative_dfs(graph, 5)
        self.assertEqual(previous, [4, 5, 1, None, 6, None, 5, None])

        _, previous = iterative_dfs(graph, 3)
        self.assertEqual(previous, [None, None, None, None, None, None, None, 3])

        _, previous = iterative_dfs(graph, 7)
        self.assertEqual(previous, [None, None, None, 7, None, None, None, None])
