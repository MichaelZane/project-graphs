"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:

            self.vertices[v1].add(v2)

        else:
            raise IndexError("Vertex doesn't Exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # enqueue the starting vertex id
        q.enqueue(starting_vertex)
        # init a set to store visited verts
        visited = set()

        # while the queue is not empty

        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()

        # if that vertex has not been visited
            if v not in visited:
                # visit it -- do whatever op
                print(v)

        # mark as visited
                visited.add(v)

        # then add all of it's neighbors to the back of the queue
                for next_v in self.get_neighbors(v):
                    q.enqueue(next_v)
                    # print(visited)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        s = Stack()
        # push starting_vertex_id on top
        s.push(starting_vertex)
        # create a set to store visited vertices
        visited = set()

        # while the stack is not empty
        while s.size() > 0:
            # pop the top of the stack vertex
            v = s.pop()

            if v not in visited:
                # visit vertex
                print(v)
                # flag as visited
                visited.add(v)

                # then add all the neighbors to the top of the stack
                for next_v in self.get_neighbors(v):
                    s.push(next_v)
                   

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # base case
        if visited == None:
            visited = set()
        # add nodes visited

        visited.add(starting_vertex)
        print(starting_vertex)

        for next_v in self.get_neighbors(starting_vertex):
            if next_v not in visited:
                self.dft_recursive(next_v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        curr_path = [starting_vertex]
        q.enqueue(curr_path)
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            curr_path = q.dequeue()
            # Grab the last vertex from the PATH
            prev_path = curr_path[-1]
            # If that vertex has not been visited...
            if prev_path not in visited:
                # CHECK IF IT'S THE TARGET
                # IF SO, RETURN PATH
                
                # Mark it as visited...
                visited.add(prev_path)
                if prev_path == destination_vertex:
                    return curr_path
                
                # Then add A PATH TO its neighbors to the back of the queue
                for next_path in self.get_neighbors(prev_path):    
                    # COPY THE PATH
                    # APPEND THE NEIGHOR TO THE BACK
                    path = list(curr_path)
                    path.append(next_path)
                    q.enqueue(path)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        curr_path = [starting_vertex]
        s.push(curr_path)
        
        visited = set()
        
        while s.size() > 0:
            
            curr_path = s.pop()

            prev_path = curr_path[-1]
        
            if prev_path not in visited:
                
                visited.add(prev_path)
                
                if prev_path == destination_vertex:
                        return curr_path
        
            for next_path in self.get_neighbors(prev_path):
                
                path = list(curr_path)
                
                path.append(next_path)
                
                s.push(path)
                        
                
            
    def dfs_recursive(self, starting_vertex, destination_vertex, curr_path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if curr_path is None:
            curr_path = []
            
        if visited is None:
            visited = set()
            
        curr_path = curr_path + [starting_vertex]
        visited.add(starting_vertex)
        
        if starting_vertex == destination_vertex:
            return curr_path
        
        for next_v in self.get_neighbors(starting_vertex):
            if next_v not in visited:
                path = self.dfs_recursive(next_v, destination_vertex, curr_path, visited)
                if path:
                    return path


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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
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
    print(graph.dfs_recursive(1, 6))
