

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
        
    # Breadth First Search Traversal
    # - BFS is aan algorithm for traversing Graph data structure. It starts at  some arbitrary 
    # node of a graph and explores the neighbor nodes (which are at current level) first, before moving
    # to the next level neighbors
    def bfs(self, vertex): #==> time complexity O(V+E)
        visitedVertexes = [vertex]
        queue = [vertex]
        while queue:  #==> time complexity O(V) where V is a number of vertexes
            dequeueVertex = queue.pop(0)
            print(dequeueVertex)
            for adjacentVertex in self.graphDict[dequeueVertex]: #==> time complexity O(E) where E is a number of edges
                if adjacentVertex not in visitedVertexes:
                    visitedVertexes.append(adjacentVertex)
                    queue.append(adjacentVertex)
                    
    # Depth First Search 
    # DFS is an algorithm for traversing a graph data structure which starts selecting some arbitrary node and 
    # explores as far as possible along each edge before backtracking (so we traverse as deep as possible and then do backtracking)
    def dfs(self, vertex): #==> time complexity O(V+E)
        # append vertex to stack
        visitedVertex = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.graphDict[popVertex]:
                if adjacentVertex not in visitedVertex:
                    visitedVertex.append(adjacentVertex)
                    stack.append(adjacentVertex)
        

graphDict = {
    'a': ['b','c'],
    'b': ['a','d','g'],
    'c': ['a','d','e'],
    'd': ['b','c','f'],
    'e': ['c','f'],
    'f': ['d','e','g'],
    'g': ['b','f'],
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
print(graph)
print('-------------------------')
# graph.addEdge(vertex='e', edge='f')
# print(graph)
print('------------BFS----------')
graph.bfs('a')
print('------------DFS----------')
graph.dfs('a')


'''
BFS vs DFS

                                           BFS                       DFS
------------------------------------------------------------------------------------------------                                       
HOw does it work internally?     it goes in breath first     it goes in depth firs
------------------------------------------------------------------------------------------------                                       
Which DS does it use internally?      Queue                        Stack
------------------------------------------------------------------------------------------------    
Time complexity                       O(V+E)                        O(V+E)
------------------------------------------------------------------------------------------------    
Space complexity                       O(V+E)                        O(V+E)
------------------------------------------------------------------------------------------------    
When to use?                    if we know that the target          if we already know that the 
                                is close to the string point        target vertex is buried very deep


'''

'''
Topological Sort
'''
# Topological Sort: Sorts given actions in such a way that if there is a dependency of one
# action on another, then the dependent action always comes later than its parent actoin.

from collections import defaultdict

class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices
        
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
        
    # topological helper function
    def topologicalSortUtil(self, vertex, visited, stack):
        visited.append(vertex)
        for element in self.graph[vertex]:
            if element not in visited:
                self.topologicalSortUtil(element, visited, stack)
        stack.insert(0, vertex)

    def topologicalSort(self): # Time complexity => O(V+E) , Space complexity => O(V+E)
        visitedElements = []
        stack = []
        for element in list(self.graph):
            if element not in visitedElements:
                self.topologicalSortUtil(element, visitedElements, stack)
        print(stack)


graph = Graph(8)
graph.addEdge('A','C')
graph.addEdge('C','E')
graph.addEdge('E','H')
graph.addEdge('E','F')
graph.addEdge('F','G')
graph.addEdge('B','D')
graph.addEdge('B','C')
graph.addEdge('D','F')

graph.topologicalSort()



















