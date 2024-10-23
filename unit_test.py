import math
import unittest
import pathing


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
    
    def test_find_DFS_path(self):
        graph = [
            ((100,100), [2, 1]),
            ((200,100), [0,3]),
            ((300,100), [0,6]),
            ((400,100), [1,4]),
            ((500,100), [4,5]),
            ((600,100), [5,6]),
            ((700,100), [1,5]),
        ]
        stack = [0]
        result = pathing.dfs_to_target(6, graph, stack)
        self.assertEqual(result, [0, 1, 3, 4, 5, 6], "The path to target is not expected val")

    def test_no_DFS_path(self):
        graph = [
            ((100,100), [1, 2]),
            ((200,100), [0]),
            ((300,100), [0]),
            ((400,100), []),
        ]
        stack = [0]
        result = pathing.dfs_to_target(3, graph, stack)
        self.assertIsNone(result, "Did not return None when target reachable")

    def test_graph_none(self):
        with self.assertRaises(AssertionError) as context:
            pathing.dfs_to_target(0, None, [0])
        self.assertEqual(str(context.exception), "Graph is None")

    def test_stack_DFS_path(self):
        graph = [
            ((100,100), [1, 2]),
            ((200,100), [0,2]),
            ((300,100), [0,1,3]),
            ((400,100), [2]),
        ]
        with self.assertRaises(AssertionError) as context:
            pathing.dfs_to_target(1, graph, None)
        self.assertEqual(str(context.exception), "Stack cannot be None")

    def test_invalid_DFS_target(self):
        graph = [
            ((100,100), [1]),
            ((200,100), [0]),
        ]
        with self.assertRaises(AssertionError) as context:
            pathing.dfs_to_target(3, graph, [0])
        self.assertEqual(str(context.exception), "Target index is not a valid index")

    def test_find_BFS_path(self):
        graph = [
            ((100,100), [1, 2]),
            ((200,100), [0,3]),
            ((300,100), [0,6]),
            ((400,100), [1,4]),
            ((500,100), [4,5]),
            ((600,100), [5,6]),
            ((700,100), [1,5]),
        ]
        stack = [0]
        result = pathing.bfs_to_target(6, graph, stack)
        self.assertEqual(result, [0, 2, 6], "The path to target is not expected val")

    def test_no_BFS_path(self):
        graph = [
            ((100,100), [1, 2]),
            ((200,100), [0]),
            ((300,100), [0]),
            ((400,100), []),
        ]
        stack = [0]
        result = pathing.bfs_to_target(3, graph, stack)
        self.assertIsNone(result, "Did not return None when target reachable")

    def test_graph_BFS_none(self):
        with self.assertRaises(AssertionError) as context:
            pathing.bfs_to_target(0, None, [0])
        self.assertEqual(str(context.exception), "Graph is None")

    def test_stack_BFS_path(self):
        graph = [
            ((100,100), [1, 2]),
            ((200,100), [0,2]),
            ((300,100), [0,1,3]),
            ((400,100), [2]),
        ]
        with self.assertRaises(AssertionError) as context:
            pathing.bfs_to_target(1, graph, None)
        self.assertEqual(str(context.exception), "Stack cannot be None")

    def test_invalid_BFS_target(self):
        graph = [
            ((100,100), [1]),
            ((200,100), [0]),
        ]
        with self.assertRaises(AssertionError) as context:
            pathing.bfs_to_target(3, graph, [0])
        self.assertEqual(str(context.exception), "Target index is not a valid index")


if __name__ == '__main__':
    unittest.main()

    
