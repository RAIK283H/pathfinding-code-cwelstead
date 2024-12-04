import graph_data
import global_game_data
from numpy import random
import random
import heapq as heap
import math
import f_w as fw

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
#    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
#    global_game_data.graph_paths.append(get_dijkstra_path())
    global_game_data.graph_paths.append(get_fw_path())


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
    target_node = global_game_data.target_node[global_game_data.current_graph_index]

    graph = graph_data.graph_data[global_game_data.current_graph_index]
    stack = [global_game_data.current_player_index]
    path = []

    visited = set()
    visited.add(global_game_data.current_player_index)
    parents = {}
    parents[global_game_data.current_player_index] = False

    #DFS for the target node first
    while stack:
        current = stack.pop()
        if (current == target_node):
            break
        
        neighbors = graph[current][1]
        insert_idx = len(stack)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                stack.insert(insert_idx, neighbor)

    while (type(current) == int):
        path.insert(0, current)
        current = parents[current]
    
    # DFS for the end node from the target node
    stack = [target_node]
    visited = set()
    visited.add(target_node)
    parents = {}
    parents[target_node] = False
    while stack:
        current = stack.pop()
        if (current == len(graph) - 1):
            break
        
        neighbors = graph[current][1]
        insert_idx = len(stack)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                stack.insert(insert_idx, neighbor)
    
    target_path = []
    while (type(current) == int):
        target_path.insert(0, current)
        current = parents[current]
    
    #target idx appears twice, remove one instance and start node
    target_path.pop(0)
    path.pop(0)
    path = path + target_path

    #if the target node is the start, it will be considered already hit
    assert target_node in path or target_node == 0, "Target node is not in the path!"
    assert len(graph) - 1 == path[-1], "Path does not end at the exit node!"
    for i in range(len(path) - 2):
        assert path[i + 1] in graph[path[i]][1], "One or more connected nodes don't have an edge!"

    return path

def get_bfs_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]

    graph = graph_data.graph_data[global_game_data.current_graph_index]
    queue = [global_game_data.current_player_index]
    path = []

    visited = set()
    visited.add(global_game_data.current_player_index)
    parents = {}
    parents[global_game_data.current_player_index] = False

    #BFS for the target node first
    while queue:
        current = queue.pop(0)
        if (current == target_node):
            break
        
        neighbors = graph[current][1]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)

    while (type(current) == int):
        path.insert(0, current)
        current = parents[current]
    
    # BFS for the end node from the target node
    queue = [target_node]
    visited = set()
    visited.add(target_node)
    parents = {}
    parents[target_node] = False
    while queue:
        current = queue.pop(0)
        if (current == len(graph) - 1):
            break
        
        neighbors = graph[current][1]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)
    
    insert_idx = len(path)
    while (type(current) == int):
        path.insert(insert_idx, current)
        current = parents[current]
    
    #target idx appears twice, remove one instance and start node
    path.pop(insert_idx)
    path.pop(0)

    #if the target node is the start, it will be considered already hit
    assert target_node in path or target_node == 0, "Target node is not in the path!"
    assert len(graph) - 1 == path[-1], "Path does not end at the exit node!"
    for i in range(len(path) - 2):
        assert path[i + 1] in graph[path[i]][1], "One or more connected nodes don't have an edge!"

    return path

# u and v are both indices that refer to nodes in graph
def dist_between(graph, u, v):
    return math.sqrt((graph[u][0][0] - graph[v][0][0]) ** 2 + (graph[u][0][1] - graph[v][0][1]) ** 2)

def get_dijkstra_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    path = []

    graph = graph_data.graph_data[global_game_data.current_graph_index]
    distances = {node:float('inf') for node in  range(len(graph))}
    parents = {node:None for node in range(len(graph))}
    solved = {node:False for node in range(len(graph))}
    distances[0] = 0

    queue = []
    heap.heappush(queue, (distances[0], 0))

    while queue:
        current_dist, current_node = heap.heappop(queue)
        solved[current_node] = True

        for neighbor in graph[current_node][1]:
            neighbor_dist = current_dist + dist_between(graph, current_node, neighbor)
            if (not solved[neighbor]) and neighbor_dist < distances[neighbor]:
                distances[neighbor] = neighbor_dist
                parents[neighbor] = current_node
                if neighbor not in queue:
                    heap.heappush(queue, (distances[neighbor], neighbor))
    
    traced_node = target_node
    while (parents[traced_node] != None):
        path.insert(0, traced_node)
        traced_node = parents[traced_node]
    
    end_path = []
    distances = {node:float('inf') for node in  range(len(graph))}
    parents = {node:None for node in range(len(graph))}
    solved = {node:False for node in range(len(graph))}
    distances[target_node] = 0

    queue = []
    heap.heappush(queue, (distances[target_node], target_node))

    while queue:
        current_dist, current_node = heap.heappop(queue)
        solved[current_node] = True

        for neighbor in graph[current_node][1]:
            neighbor_dist = current_dist + dist_between(graph, current_node, neighbor)
            if (not solved[neighbor]) and neighbor_dist < distances[neighbor]:
                distances[neighbor] = neighbor_dist
                parents[neighbor] = current_node
                if neighbor not in queue:
                    heap.heappush(queue, (distances[neighbor], neighbor))
    
    traced_node = len(graph) - 1
    while (parents[traced_node] != None):
        end_path.insert(0, traced_node)
        traced_node = parents[traced_node]
    
    path.extend(end_path)

    assert 0 in graph[path[0]][1], "Path does not start at the first node!"
    assert target_node in path, "Target node is not in the path!"
    assert len(graph) - 1 == path[-1], "Path does not end at the exit node!"
    for i in range(len(path) - 2):
        assert path[i + 1] in graph[path[i]][1], "One or more connected nodes don't have an edge!"

    return path

def get_fw_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    graph = graph_data.graph_data[global_game_data.current_graph_index]

    path = fw.floyd_warshall_path(graph, target_node)

    assert 0 in graph[path[0]][1], "Path does not start at the first node!"
    assert target_node == 0 or target_node in path, "Target node is not in the path!"
    assert len(graph) - 1 == path[-1], "Path does not end at the exit node!"
    for i in range(len(path) - 2):
        assert path[i + 1] in graph[path[i]][1], "One or more connected nodes don't have an edge!"

    return path