

'''
Single Source Shortest Path Problem
'''

# A single source problem is about finding a path between a given vertex (called source)
# to all other vertices in a graph such that the total distance between then (source and destination) is
# is minimum

# The real world problem example:
# - Five offices in different cities.
# - Travel costs between these cities are known
# - Find the cheapest way from head office to branches in different cities


# Single Source Shortest Path Problem Algorithms:
# - BFS
# - Dijkstra's Algorithm
# - Bellman Ford Algorithm


class Graph:
    def __init__(self, graphDict = None):
        if graphDict is None: graphDict = {}
        self.graphDict = graphDict
        
    # BFS works only for unweighted graphs
    # Time Complexity => O(E) - because we visit only connected vertixes , Space complexity => O(E)
    def BFS(self, startElement, endElement): #find shortes path between startElement and endElement
        queue = []
        queue.append([startElement]) #append list to create path from few elements
        while queue:
            path = queue.pop(0) #pop out first element from queue
            node = path[-1] #get last element from 
            if node is endElement: #return first path that comes to endElement
                return path
            for adjacantNode in self.graphDict.get(node, []): #use get method to return empty list [] if node is not found
                new_path = list(path)
                new_path.append(adjacantNode) # create new path
                queue.append(new_path) #append new path to queue
                
            
graphDict = {
    'a': ['b','c'],
    'b': ['d','g'],
    'c': ['d','e'],
    'd': ['f'],
    'e': ['f'],
    'g': ['f'],
}


''' How our graph looks like?
[A]-----[B]
 |       |  \
 |       |    \
[C]-----[D]    [G]
 |       |    /
 |       |  /
[E]-----[F]  
'''

graph = Graph(graphDict)
print(graph.BFS('a','f'))



'''
Which graphs works with which algorithms?

Graph Type                         |  BFS  |
---------------------------------------------------------------------------------------------------------------------------
Unweighted - undirected            | WORKS |
---------------------------------------------------------------------------------------------------------------------------
Unweighted - directed              | WORKS |
---------------------------------------------------------------------------------------------------------------------------
Positive - weighted - undirected   |   X   |
---------------------------------------------------------------------------------------------------------------------------
Positive - weighted - directed     |   X   |
---------------------------------------------------------------------------------------------------------------------------
Negative - weighted - undirected   |   X   |
---------------------------------------------------------------------------------------------------------------------------
Negative = weighted - directed     |   X   |
---------------------------------------------------------------------------------------------------------------------------

'''
















