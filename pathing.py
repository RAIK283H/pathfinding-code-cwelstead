import graph_data
import global_game_data
from numpy import random
import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    target_hit = False

    graph = graph_data.graph_data[global_game_data.current_graph_index]
    path = [global_game_data.current_player_index]

    assert len(graph) > 0, "Cannot create a path for an empty graph!"
    assert target_node < len(graph), "Target node is not in the graph!"
    assert global_game_data.current_player_index < len(graph), "Player start node is not in the graph!"

    while (not(target_hit and path[-1] == len(graph) - 1)):
        if (len(path) < len(graph) * 2):
            if (len(path) > 1 and len(graph[path[-1]][1]) > 1):
                next_idx = path[-2]
                while (next_idx == path[-2]):
                    next_idx = random.choice(graph[path[-1]][1])
            else:
                next_idx = random.choice(graph[path[-1]][1])

            if (next_idx == target_node):
                target_hit = True
            path.append(next_idx)
        else:
            path = [global_game_data.current_player_index]
            target_hit = False

    
    path.pop(0)

    assert target_node in path, "Path does not hit the target node!"
    assert (len(graph) - 1) == path[-1], "Path does not end at the end node!"

    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
