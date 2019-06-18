"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        ---
        If vs exist in self.vertices, add second value as a value to the first, which is a key
        Else, return "Vertex not in graph"
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("Vertex does not exist in graph.")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        ---
        Create an empty set to store visited nodes
        Create an empty Queue and enqueue the starting vertex
        While the queue is not empty
        Dequeue the first vertex
        If that vertex has not been visited, mark it as visited then add its neighbors to the back of the queue
        """
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        ---
        Create an empty set to store visited nodes
        Create an empty Stack and push the starting vertex
        While the stack is not empty
        Pop the first vertex
        If that vertex has not been visited, mark it as visited then add its neighbors to the top of the stack
        """
        visited = set()
        s = Stack()
        s.push(starting_vertex)

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        
        visited = set()

        def dft_inner(passed_vertex):
            print(passed_vertex)
            nonlocal visited
            visited.add(passed_vertex)
            for node in self.vertices[passed_vertex]:
                if node not in visited:
                    dft_inner(node)
                
        
        dft_inner(starting_vertex)
        
                
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        ---
        Edge case:
        If starting_v == destination_v, return list of that v

        Create an empty set to store visited nodes
        create empty list to contain paths
        Create new Queue
        enqueue starting_vertex

        while queue size is greater than 0
        dequeue the first path
        grab the last node from the path
        if v not in visited
        for neighbor in self.vertices[v]
        create a new list from the path, add neighbor to the list, and add this list to the queue
        return path if neighbor == goal 
        """
        if starting_vertex == destination_vertex:
            return [starting_vertex]

        visited = set()
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()
            print("PATH", path)
            last_node = path[-1]
            print("LAST NODE", last_node)
            if last_node not in visited:
                visited.add(last_node)
                for neighbor in self.vertices[last_node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

                    if neighbor == destination_vertex:
                        return new_path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
