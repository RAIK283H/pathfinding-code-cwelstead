import graph_data

def check_cycle(graph_idx, permutation):
    graph = graph_data.graph_data[graph_idx]

    for i in range(len(permutation) - 1):
        if (not permutation[i + 1] in graph[permutation[i]][1]):
            return False
    if (not permutation[0] in graph[permutation[-1]][1]):
        return False
    
    print("Valid Hamiltonian cycle found in graph " + str(graph_idx) + ": " + str(permutation))
    return True

def graph_permutations(graph_idx, n, check_cyles=True, return_permutations=False):
    direction_dict = {i: True for i in range(1, n+1)}

    all_permutations = []

    current_permutation = []
    for i in range(1, n+1):
        current_permutation.append(i)

    mobile_numbers = True
    while (mobile_numbers):
        if (check_cyles):
            check_cycle(graph_idx, current_permutation)
        elif (return_permutations):
            all_permutations.append(current_permutation.copy())
        else:
            print("current_permutation")

        largest_mobile_idx = -1
        for idx, num in enumerate(current_permutation):
            mobile = True
            if (direction_dict[num]):
                if (idx == 0):
                    mobile = False
                else:
                    mobile = num > current_permutation[idx - 1]
            else:
                if (idx == n - 1):
                    mobile = False
                else:
                    mobile = num > current_permutation[idx + 1]
            
            if (mobile and (largest_mobile_idx == -1 or num > current_permutation[largest_mobile_idx])):
                largest_mobile_idx = idx

        if (largest_mobile_idx >= 0):
            k = current_permutation[largest_mobile_idx]
            
            if (direction_dict[k]):
                temp = current_permutation[largest_mobile_idx - 1]
                current_permutation[largest_mobile_idx - 1] = k
                current_permutation[largest_mobile_idx] = temp
            else:
                temp = current_permutation[largest_mobile_idx + 1]
                current_permutation[largest_mobile_idx + 1] = k
                current_permutation[largest_mobile_idx] = temp
            for i in range(k+1, n+1):
                direction_dict[i] = not direction_dict[i]
        else:
            mobile_numbers = False
    
    if (return_permutations):
        return all_permutations