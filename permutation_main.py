import graph_data
import permutation as pt

for idx, graph in enumerate(graph_data.graph_data):
    if (len(graph) < 14):
        print("Checking graph " + str(idx))
        pt.graph_permutations(idx, len(graph) - 2)