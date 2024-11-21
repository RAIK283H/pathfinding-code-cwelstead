import math
import unittest
import global_game_data
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

    def test_dfs_happy_path_1(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 1]
        expected = [17, 11, 4, 7, 1, 2, 5, 21, 23]
        result = pathing.get_dfs_path()
        self.assertEqual(expected, result)
    def test_dfs_happy_path_2(self):
        global_game_data.current_graph_index = 3
        global_game_data.target_node = [0, 0, 0, 11]
        expected = [1, 2, 3, 7, 11, 15]
        result = pathing.get_dfs_path()
        self.assertEqual(expected, result)
    def test_dfs_optimal_path_backtracks(self):
        global_game_data.current_graph_index = 7
        global_game_data.target_node = [0, 0, 0, 0, 0, 0, 0, 3]
        expected = [3, 0, 9]
        result = pathing.get_dfs_path()
        self.assertEqual(expected, result)
    def test_dfs_target_is_start(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 0]
        expected = [17, 18, 23]
        result = pathing.get_dfs_path()
        self.assertEqual(expected, result)
    def test_dfs_target_is_end(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 23]
        expected = [17, 18, 23]
        result = pathing.get_dfs_path()
        self.assertEqual(expected, result)

    def test_bfs_happy_path_1(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 1]
        expected = [21, 19, 1, 19, 21, 23]
        result = pathing.get_bfs_path()
        self.assertEqual(expected, result)
    def test_bfs_happy_path_2(self):
        global_game_data.current_graph_index = 3
        global_game_data.target_node = [0, 0, 0, 11]
        expected = [1, 2, 3, 7, 11, 15]
        result = pathing.get_bfs_path()
        self.assertEqual(expected, result)
    def test_bfs_optimal_path_backtracks(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 22]
        expected = [22, 0, 21, 23]
        result = pathing.get_bfs_path()
        self.assertEqual(expected, result)
    def test_bfs_target_is_start(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 0]
        expected = [21, 23]
        result = pathing.get_bfs_path()
        self.assertEqual(expected, result)
    def test_bfs_target_is_end(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 23]
        expected = [21, 23]
        result = pathing.get_bfs_path()
        self.assertEqual(expected, result)
    

if __name__ == '__main__':
    unittest.main()
