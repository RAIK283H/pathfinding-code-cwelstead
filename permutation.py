import graph_data

# Checks one permutation to determine if it is a Hamiltonian cycle of the graph with the idx in the parameters
def check_cycle(graph_idx, permutation, print_if_found=True):
    graph = graph_data.graph_data[graph_idx]

    for i in range(len(permutation) - 1):
        if (not permutation[i + 1] in graph[permutation[i]][1]):
            return False
    if (not permutation[0] in graph[permutation[-1]][1]):
        return False
    
    cycle = permutation
    cycle.append(cycle[0])

    if (print_if_found):
        print("Valid Hamiltonian cycle found in graph " + str(graph_idx) + ": " + str(cycle))
    return True

# Finds and checks all graph permutations
# Storing all permutations will be infeasible for larger numbers so it is left as a condition
def graph_permutations(graph_idx, n, check_cyles=True, return_permutations=False):
    direction_dict = {i: True for i in range(1, n+1)}

    all_permutations = []

    current_permutation = []
    for i in range(1, n+1):
        current_permutation.append(i)

    mobile_numbers = True
    while (mobile_numbers):
        # Performs the correct action depending on the source of the function call
        if (check_cyles):
            check_cycle(graph_idx, current_permutation) # for normal operation
        elif (return_permutations):
            all_permutations.append(current_permutation.copy()) # when collecting all permutations
        else:
            print(current_permutation) # when debugging

        # Find largest mobile index
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
            # Make a swap
            k = current_permutation[largest_mobile_idx]
            
            if (direction_dict[k]):
                temp = current_permutation[largest_mobile_idx - 1]
                current_permutation[largest_mobile_idx - 1] = k
                current_permutation[largest_mobile_idx] = temp
            else:
                temp = current_permutation[largest_mobile_idx + 1]
                current_permutation[largest_mobile_idx + 1] = k
                current_permutation[largest_mobile_idx] = temp
            
            # Update directions for all numbers greater than k
            for i in range(k+1, n+1):
                direction_dict[i] = not direction_dict[i]
        else:
            mobile_numbers = False
    
    if (return_permutations):
        return all_permutations