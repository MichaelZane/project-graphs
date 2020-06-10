from util import Stack, Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):

    #if no parent return -1
    g = Graph()
    #make the graph
    for a in ancestors:
        g.add_vertex(a[0])
        g.add_vertex(a[1])
    #add vertices
    for a in ancestors:
        g.add_edge(a[1], a[0])
       
    
    """
    child key -- parents set of vertexes
    {1: {10}, 3: {1, 2}, 2: set(), 6: {3, 5}, 5: {4}, 7: {5}, 4: set(), 8: {11, 4}, 9: {8}, 11: set(), 10: set()}
    """
    
    # print(g.vertices.values())
    q = Queue()
    #set up and add starting node
    q.enqueue(starting_node)
    # length holding distance from start of vertex
    length = {starting_node: 0}
    # parent for curr vertex, vertex just added as value
    parent = {starting_node: 0}
    
    #search while q is not empty
            
    while q.size() > 0:
        
        path = q.dequeue()
        #get path off of front of queue
        for vert in g.vertices[path]: 
        #get the key{vertex: neighbors} of path which we dequeued   
            q.enqueue(vert)
        #step forward searching tracking length 
            length[vert] = length[path] + 1
        #use the parent to get path of vertex   
            parent[vert] = path
         
    if path == starting_node:
        return -1    
                            
    return  path      
                
            
            
     
        
            
    
      
                
                
                
                
                
        
        
        
           
            
              
                    
                        
                        
                     
                    
    





   
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)
earliest_ancestor(test_ancestors, 2)
earliest_ancestor(test_ancestors, 3)
earliest_ancestor(test_ancestors, 4)
earliest_ancestor(test_ancestors, 5)
earliest_ancestor(test_ancestors, 6)
earliest_ancestor(test_ancestors, 7)
earliest_ancestor(test_ancestors, 8)
earliest_ancestor(test_ancestors, 9)
earliest_ancestor(test_ancestors, 10)
earliest_ancestor(test_ancestors, 11)

            