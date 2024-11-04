import math
import unittest
import global_game_data
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

    def test_dfs_1(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 1]
        expected = [17, 11, 4, 7, 1, 2, 5, 21, 23]
        result = pathing.get_dfs_path()
        self.assertEqual(expected, result)
    def test_bfs_1(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 1]
        expected = [21, 19, 1, 19, 21, 23]
        result = pathing.get_bfs_path()
        self.assertEqual(expected, result)

    def test_dfs_2(self):
        global_game_data.current_graph_index = 3
        global_game_data.target_node = [0, 0, 0, 11]
        expected = [1, 2, 3, 7, 11, 15]
        result = pathing.get_dfs_path()
        self.assertEqual(expected, result)
    def test_bfs_2(self):
        global_game_data.current_graph_index = 3
        global_game_data.target_node = [0, 0, 0, 11]
        expected = [1, 2, 3, 7, 11, 15]
        result = pathing.get_bfs_path()
        self.assertEqual(expected, result)

    def test_permutation(self):
        expected = [[1, 2, 3, 4],
                    [1, 2, 4, 3],
                    [1, 4, 2, 3],
                    [4, 1, 2, 3],
                    [4, 1, 3, 2],
                    [1, 4, 3, 2],
                    [1, 3, 4, 2],
                    [1, 3, 2, 4],
                    [3, 1, 2, 4],
                    [3, 1, 4, 2],
                    [3, 4, 1, 2],
                    [4, 3, 1, 2],
                    [4, 3, 2, 1],
                    [3, 4, 2, 1],
                    [3, 2, 4, 1],
                    [3, 2, 1, 4],
                    [2, 3, 1, 4],
                    [2, 3, 4, 1],
                    [2, 4, 3, 1],
                    [4, 2, 3, 1],
                    [4, 2, 1, 3],
                    [2, 4, 1, 3],
                    [2, 1, 4, 3],
                    [2, 1, 3, 4],]
        result = permutation.graph_permutations(0, 4, check_cyles=False, return_permutations=True)
        self.assertEqual(expected, result)
    def test_circuit_1(self):
        circuit = [1,14,7,8,9,4,13,12,11,10,3,6,5,2]
        self.assertTrue(permutation.check_cycle(5, circuit, print_if_found=False))
    def test_circuit_2(self):
        circuit = [1,2,5,6,3,10,11,12,13,4,9,8,7,14]
        self.assertTrue(permutation.check_cycle(5, circuit, print_if_found=False))
    def test_circuit_false(self):
        circuit = [1,2,3,10,11,12,13,4,6,5,14,7,8,9]
        self.assertFalse(permutation.check_cycle(5, circuit, print_if_found=False))
    

if __name__ == '__main__':
    unittest.main()
