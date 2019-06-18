# Data is formatted as a list of parent, child pairs [1,3]
# Each individual is assigned a unique integer identifier
# Write a function that, given the data set and the ID of an individual in the dataset, returns the earliest known ancestor (farthest distance from the input individual).
# If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
# If the individual has no parents, return -1

# This is a sparse acyclic directed graph
# Not looking for the shortest path, so likely not a breadth-first anything

def earliest_ancestor(data, v_id):
    pass
    # Store data in a dictionary to create an adjacency list
    adj_list = {}

    # for each vertex in tuple
    for pair in data:
        # if vertex not in graph dict
        if pair[0] not in adj_list:
            # add vertex as key and initialize with a set and first value
            adj_list[pair[0]] = {pair[1]}
        # else, add the value to the set
        else:
          adj_list[pair[0]].add(pair[1])
    print(adj_list)
    # Could perform DFS without saving the visited nodes, and push the path to a list of list of paths.
    # Or a single list that gets replaced if the first item has a lower value

    # return earliest known ancestor (v_id)

dataset = [(1,3),(2,3),(3,6),(5,6),(5,7),(4,5),(4,8),(8,9),(11,8),(10,1)]
value = 6
print(earliest_ancestor(dataset, value))

'''
If I switched the key/values in the dict...
1: 10
3: 1, 2
5: 4
6: 3, 5
7: 5
8: 4,11
9: 8
'''