import graph_data
import permutation as pt

largest_graph = 13 # can be changed depending on how big of a graph you want to check

for idx, graph in enumerate(graph_data.graph_data):
    if (len(graph) <= largest_graph):
        print("Checking graph " + str(idx))
        pt.graph_permutations(idx, len(graph) - 2)