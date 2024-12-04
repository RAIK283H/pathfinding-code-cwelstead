import graph_data
import math

# u and v are both indices that refer to nodes in graph
def dist_between(graph, u, v):
    return math.sqrt((graph[u][0][0] - graph[v][0][0]) ** 2 + (graph[u][0][1] - graph[v][0][1]) ** 2)

def graph_to_matrix(graph):
    size = len(graph)
    matrix = [[math.inf] * size for _ in range(size)]
    for idx, node in enumerate(graph):
        for neighbor in node[1]:
            matrix[idx][neighbor] = dist_between(graph, idx, neighbor)
    
    return matrix

def floyd_warshall(graph, start, end):
    size = len(graph)
    dist = graph_to_matrix(graph)
    prev = [[math.inf] * size for _ in range(size)]

    for idx, node in enumerate(graph):
        dist[idx][idx] = 0
        prev[idx][idx] = idx
        for neighbor in node[1]:
            prev[idx][neighbor] = idx
    
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]
    
    u, v = start, end
    path = []
    while u != v:
        path.insert(0, v)
        v = prev[u][v]
    
    return path

def floyd_warshall_path(graph, target):
    return floyd_warshall(graph, 0, target) + floyd_warshall(graph, target, len(graph) - 1)