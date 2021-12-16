

'''
What is Graph?
'''
# Graph consists of a finite set of Vertices (or nodes) and a set of Edges which connect a pair of nodes

# Graph example:

'''
[A]---[D]---[J]
 | \       /
 |   \    /
[A]---[D]    
 |   /
 |  /
[E]/  
'''



'''
Why we need Graphs?
'''
# Graphs are used to represent network
# There are used to calculate shortest path on google maps


'''
Graph TERMINOLOGY

- Vertices (vertex): Vertices are the nodes of the graph
- Edge: The edge is the line that connects pairs of vertices
- Unweighted Graph: A graph which does not have a weight associated with any edge
- Weighted Graph: A graph which has a weight associated with any edge
- Undirected Graph: In case the edges of the graph do not have a direction associated with them (we can travel both way from one node to another)
- Directed Graph: if the edges in a graph have a direction associated with them (we can travel from one node to another only in one way)
- Cyclic Graph: A graph which has at least one loop (we can start from one node and travel that way that after some travels we come back to start point)
- Acyclic Graph: A graph with no loop (we can't after some travels end in starting point)
- Tree: it is a special sace of directed acyclic graph
'''

'''
Graph Types

- Directed Graphs:
    - Weighted:
        - Positive => graph edges have weights (which all are positive numbers) and have directions associated with them
        - Negative => if graph edges have any negative weight and have directions associated
        
    - Unweighted Graphs => we don't have any weight associated with edge but we have directions specified with edges

- Undirected Graphs:
    - Weighted:
        - Positive => graph edges have weights (which all are positive numbers) and don't have directions associated with them
        - Negative => if graph edges have any negative weight and don't have any directions associated
        
    - Unweighted Graphs => we don't have any weight associated with edge and all edges don't have any direction
'''


'''
Graph Representation
'''
# - Adjacency Matrix: an adjacency matrix is a square matrix or you can sa it is a 2D array. 
# And the elements of the matrix indicate whether pairs of verices are adjacent or not in the graph
# use if a graph is complete or almost complete (on uncomplete graph most of matrix cells will be empty)

# - Adjacency List: an adjacency list is a collection of unordered list used to represent a graph.
# Each list describes the set of neighbors of a bertex in the graph (in python it is represented as dictionary)
# use if the number of edges are few


class Graph:
    def __init__(self, graphDict=None):
        if graphDict is None:
            graphDict = {}
        self.graphDict = graphDict
        
    def __str__(self):
        return '\n'.join([f'{item} : {self.graphDict[item]}' for item in self.graphDict])
        
    def addEdge(self, vertex, edge):
        self.graphDict[vertex].append(edge)
        

graphDict = {
    'a': ['b','c'],
    'b': ['a','d','e'],
    'c': ['a','e'],
    'd': ['b','e','f'],
    'e': ['d','f','c'],
    'f': ['d','e'],
}

graph = Graph(graphDict)
print(graph)
graph.addEdge(vertex='e', edge='f')
print('-------------------------')
print(graph)



























