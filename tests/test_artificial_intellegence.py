from artificial_intellegence import dfs_graph_traversal
from artificial_intellegence import bfs_graph_traversal
from artificial_intellegence import uniform_cost_search

import unittest


class test_dfs(unittest.TestCase):
    def test_dfs(self):
        adj, st, visited = [[1, 2], [0, 3], [
            0, 3], [1, 2]], 0, [-1, -1, -1, -1]

        dfs_instance = dfs_graph_traversal.Dfs()
        dfs_instance.dfs(adj, st, visited)

        expected_output = [0, 1, 3, 2]
        self.assertEqual(dfs_instance.output.sort(), expected_output.sort())


class test_bfs(unittest.TestCase):
    def test_bfs(self):
        adj, st, visited = [[1, 2], [0, 3], [
            0, 3], [1, 2]], 0, [-1, -1, -1, -1]

        bfs_instance = bfs_graph_traversal.Bfs()
        bfs_instance.bfs(adj, st, visited)

        expected_output = [0, 1, 3, 2]
        self.assertEqual(bfs_instance.output.sort(), expected_output.sort())


class test_ucs(unittest.TestCase):
    def test_ucs(self):
        adj, st, visited = [[[1, 1], [5, 2]], [[1, 0], [1, 3]], [
            [5, 0], [5, 3]], [[1, 1], [5, 2]]], 0, [-1, -1, -1, -1]
        distance = [float('inf') for x in range(4)]

        ucs_instance = uniform_cost_search.Ucs()

        expected_output = 2
        self.assertEqual(ucs_instance.ucs(
            adj, 0, 3, visited, distance), expected_output)
