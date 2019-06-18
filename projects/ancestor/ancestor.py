# Data is formatted as a list of parent, child pairs [1,3]
# Each individual is assigned a unique integer identifier
# Write a function that, given the data set and the ID of an individual in the dataset, returns the earliest known ancestor (farthest distance from the input individual).
# If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
# If the individual has no parents, return -1

# This is a sparse acyclic directed graph
# Not looking for the shortest path, so likely not a breadth-first anything
# Could perform DFS without saving the visited nodes, and push the path to a list of list of paths.
# Or a single list that gets replaced if the first item has a lower value

def earliest_ancestor(data, v_id):
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
  
    # Create a stack
    stack = []
    # Create a list to store longest path
    possible_paths = []
    # Loop over the keys in the dict
    for starting_vertex in adj_list:
        # push the key into the stack
        stack.append([starting_vertex])
        # while len(stack) > 0
        while len(stack) > 0:
            # pop off the first value of stack (path)
            path = stack.pop()
            # grab the last node of the path
            last = path[-1]
            
            # if last value in path is equal to the vertex id
            if last == v_id:
                # if the length of the path is greater/equal to length of possible_paths
                if len(path) >= len(possible_paths):
                    # add path to list of possible paths
                    possible_paths.append(path)
            # if last value is not a key in the adj_list
            elif last not in adj_list:
                # continue with loop
                continue
            else:
                # for neighbors in adj_list[key]
                for neighbor in adj_list[last]:
                    # create a copy of the path
                    path_copy = list(path)
                    # add the neighbor to the path
                    path_copy.append(neighbor)
                    # push the path to the stack
                    stack.append(path_copy)
              
    # if possible_paths only has one path and the length is 1 (meaning, the vertex doesn't have any ancestors)
    if len(possible_paths) == 1 and len(possible_paths[0]) == 1:
        return -1
    else:
        # sort the list of possible paths from longest to shortest
        path_list = sorted(possible_paths,key=len,reverse=True)
        # return the first value of the longest path, which ends up being the earliest ancestor
        return path_list[0][0]


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