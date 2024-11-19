import math
import unittest
import pathing
import permutation


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
    
    def test_swap_valid(self):
        arr = [1, 2, 3, 4]
        permutation.swap(arr, 1, 3)
        self.assertEqual(arr, [1, 4, 3, 2])
    
    def test_swap_j_invalid_index(self):
        arr = [1, 2, 3]
        with self.assertRaises(AssertionError) as context:
            permutation.swap(arr, 0, 3)
        self.assertEqual(str(context.exception), "swap failed: j was not valid index")   

    def test_swap_i_invalid_index(self):
        arr = [1, 2, 3]
        with self.assertRaises(AssertionError) as context:
            permutation.swap(arr, -1, 2)
        self.assertEqual(str(context.exception), "swap failed: i was not valid index")

    def test_swap_j_none(self):
        arr = [1, 2, 3]
        with self.assertRaises(AssertionError) as context:
            permutation.swap(arr, 0, None)
        self.assertEqual(str(context.exception), "swap failed: j was None")   

    def test_swap_i_none(self):
        arr = [1, 2, 3]
        with self.assertRaises(AssertionError) as context:
            permutation.swap(arr, None, 2)
        self.assertEqual(str(context.exception), "swap failed: i was None")      

    def test_swap_array_none(self):
        with self.assertRaises(AssertionError) as context:
            permutation.swap(None, 0, 2)
        self.assertEqual(str(context.exception), "swap failed: array was None")      
    
    def test_getLargestMobileInt(self):
        nodeArray = [1, 2, 3, 4]
        movementArray = [True, True, False, False]
        result = permutation.getLargestMobileInt(nodeArray, movementArray)
        self.assertEqual(result, 1)
    
    def test_getLargestMobileInt_mobile_on_the_wall(self):
        nodeArray = [4, 1, 2, 3]
        movementArray = [True, True, True, True]
        result = permutation.getLargestMobileInt(nodeArray, movementArray)
        self.assertEqual(result, 3)
    
    def test_getLargestMobileInt_no_mobile_int(self):
        nodeArray = [1, 2, 3, 4]
        movementArray = [False, False, False, False]
        result = permutation.getLargestMobileInt(nodeArray, movementArray)
        self.assertIsNone(result)
    
    def test_getLargestMobileInt_nodeArray_none(self):
        movementArray = [False, False, False, False]
        with self.assertRaises(AssertionError) as context:
            permutation.getLargestMobileInt(None, movementArray)
        self.assertEqual(str(context.exception), "getLargestMobileInt failed: nodeArray was None")

    def test_getLargestMobileInt_movementArray_none(self):
        nodeArray = [1, 2, 3, 4]
        with self.assertRaises(AssertionError) as context:
            permutation.getLargestMobileInt(nodeArray, None)
        self.assertEqual(str(context.exception), "getLargestMobileInt failed: movementArray was None")    

    '''def test_6_permutations_permutationGenerator(self):
        result = permutation.permutationGenerator(3)
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0], [0, 1, 2])

    def test_24_permutations_permutationGenerator(self):
        result = permutation.permutationGenerator(4)
        self.assertEqual(len(result), 24)
        self.assertEqual(result[0], [0, 1, 2, 3])'''
        
    def test_permutationGenerator_invalid_length_negative(self):
        with self.assertRaises(AssertionError) as context:
            permutation.permutationGenerator(-1)
        self.assertEqual(str(context.exception), "Permutation Generator failed: lengthOfArray was less than 1")    
    
    def test_permutationGenerator_invalid_length(self):
        with self.assertRaises(AssertionError) as context:
            permutation.permutationGenerator(0)
        self.assertEqual(str(context.exception), "Permutation Generator failed: lengthOfArray was less than 1")

    def test_permutationGenerator_none_length(self):
        with self.assertRaises(AssertionError) as context:
            permutation.permutationGenerator(None)
        self.assertEqual(str(context.exception), "Permutation Generator failed: lengthOfArray was None")
    
    def test_isThereAHamiltonianCycle_valid(self):
        with self.assertRaises(AssertionError) as context:
            permutation.isThereAHamiltonianCycle(None)
        self.assertEqual(str(context.exception), "isThereAHamiltonianCycle failed: graph was None")

    def test_isThereAHamiltonianCycle_valid(self):
        graph = [
            ((100,100), [1,2]),
            ((200,100), [0,2]),
            ((300,100), [0,1])
        ]
        self.assertEqual(permutation.isThereAHamiltonianCycle(graph), True)

    def test_isThereAHamiltonianCycle_valid_2(self):
        graph = [
            ((100,100), [5, 1]),
            ((200,100), [0,2,3]),
            ((300,100), [1,4,5]),
            ((400,500), [1,4]),
            ((800,200), [2,3]),
            ((300,100), [0,2])
        ]
        self.assertEqual(permutation.isThereAHamiltonianCycle(graph), True)    
    
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


    def test_invalid_dijkstra_target(self):
        graph = [
            ((100,100), [1]),
            ((200,100), [0]),
        ]
        with self.assertRaises(AssertionError) as context:
            pathing.dijkstra_to_target(3, graph, [0])
        self.assertEqual(str(context.exception), "Target index is not a valid index")

    def test_graph_dijkstra_none(self):
        with self.assertRaises(AssertionError) as context:
            pathing.dijkstra_to_target(0, None, [0])
        self.assertEqual(str(context.exception), "Graph is None")


if __name__ == '__main__':
    unittest.main()

    
