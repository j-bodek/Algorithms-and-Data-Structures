


'''
Minimum Spanning Tree
'''
# A minimum spanning tree (MST) is a subset of the edges of connected, weighted and undirected graph which:
# - Connects all vertices together
# - No cycle
# - Minimum total edge

# Real life probelm example:
# - Connect five island with bridges 
# - The cost of bridges between island varies based on different factors
# - Which bridge should be constructed so that all islands are accessible and the cost is minimum

'''
Disjoint Set
'''
# it is a data structure that keeps track of set of elements which are partitioned into a number of 
# disjoint and non overlapping sets and each sets have representative which helps in identifying that sets

# STANDARD OPERATIONS FOR DISJOINT SET
# - makeSet(N): used to create initial set
# - union(x,y): merge two given sets
# - findSet(x): returns the set name in which this element is there

# Starting Disjoint Set
# [A], [B], [C], [D], [E]
# After union(A,B)
# [AB], [C], [D], [E] => findSet(B) -> returns [AB]
# After union(A,E)
# [ABE], [C], [D]





class Disjoint:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0) #create dictionary with vertices as keys and values initialized to 0
        
    def __str__(self):
        disjoint = self.vertices.copy()
        for v in self.parent:
            if self.parent[v] != v:
                disjoint.remove(v)
                disjoint = [element + v if self.parent[v] in element else element for element in disjoint]
        return str(disjoint)
        
    def findParent(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.findParent(self.parent[item])
        
    def union(self, x, y):
        xroot = self.findParent(x) # find parent node of x
        yroot = self.findParent(y) # find parent node of y
        # then check which one have higher rank
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[yroot] < self.rank[xroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1



vertices = ['A','B','C','D','E']

disjoint = Disjoint(vertices)
print(f"Parent node of A => {disjoint.findParent('A')}")
# union A and B
disjoint.union('A','B')
print(f"Parent node of B => {disjoint.findParent('B')}")
print(disjoint)



'''
Kruskal's Algorithm
'''
# it is a greedy algorithm
# it finds a minimum spanning tree (tree made from all nodes connected with minimum weight edges) 
# for weighted undirected graphs in two ways:
# - Add increasing cost edges at each step
# - Avoid any cycle at each step

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []
        self.minimumSpanningTree = []
        
    def addEdge(self, startElement, endElement, weight):
        self.graph.append([startElement, endElement, weight])
        
    def addNode(self, value):
        self.nodes.append(value)
        
    def printSolution(self, startElement, endElement, weight):
        for startElement, endElement, weight in self.minimumSpanningTree:
            print(f'{startElement} - {endElement}: {weight}')

    def kruskalAlgorithm(self):
        i, e = 0, 0
        # make set for each node
        disjoint = Disjoint(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2]) #sort graph by edge weights

        while e < self.vertices - 1:
            startElement, endElement, weight = self.graph[i]
            i+=1
            
            x = disjoint.findParent(startElement)
            y = disjoint.findParent(endElement)
            if x != y:
                e+=1
                self.minimumSpanningTree.append([startElement, endElement, weight])
                disjoint.union(x,y)
        self.printSolution(startElement, endElement, weight)


graph = Graph(5)
# Add vertices
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")
# Add edges (graph is undirected so we have to add it both way)
graph.addEdge("A", "B", 5)
graph.addEdge("A", "C", 13)
graph.addEdge("A", "E", 15)
graph.addEdge("B", "A", 5)
graph.addEdge("B", "C", 10)
graph.addEdge("B", "D", 8)
graph.addEdge("C", "A", 13)
graph.addEdge("C", "B", 10)
graph.addEdge("C", "E", 20)
graph.addEdge("C", "D", 6)
graph.addEdge("D", "B", 8)
graph.addEdge("D", "C", 6)
graph.addEdge("E", "A", 15)
graph.addEdge("E", "C", 20)

print('-'*10 + 'Kruskal Algorithm' + '-'*10)
graph.kruskalAlgorithm()





'''
Prims Algorithm
'''
# It is a greed algorithm
# It finds a minimum spanning tree for weighted undirected graphsin following ways:
# 1. take any vertex as a source set its weight to 0 and all other vertices weight to infinity
# 2. For every adjacent vertices if the current weight is more than current edge then we set it to current edge
# 3. Then we mark current vertex as visitd
# 4. Repeat these steps for all vertices in increasing order of weight


import sys
class Graph:
    def __init__(self, vertexNumber, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexNumber = vertexNumber
        self.minimalSpanningTree = []
        
    def printSolution(self):
        for startElement, endElement, weight in self.minimalSpanningTree:
            print(f'{startElement} - {endElement}: {weight}')
            
    def primsAlgorithm(self):
        # Array which keeps visited nodes
        visitedNodes = [0]*self.vertexNumber
        edgeNumber = 0
        visitedNodes[0]=True
        # while not traversed through all vertices countinue looping
        while edgeNumber < self.vertexNumber - 1:
            #default size of each vertex is infinity
            minimum = sys.maxsize # sys.maxsize = infinity
            
            for startElement in range(self.vertexNumber):
                # if node was visited check it connections
                if visitedNodes[startElement]:
                    for endElement in range(self.vertexNumber):
                        # if node is not inside visited nodes and has connection with startElement
                        if not visitedNodes[endElement] and self.edges[startElement][endElement]:
                            # if weight of edges between start and end element is less then current value asigned to endElement change it
                            if minimum > self.edges[startElement][endElement]:
                                minimum = self.edges[startElement][endElement]
                                finalStartElement, finalEndElement = startElement, endElement
            # when node was visited add it edge to MST
            self.minimalSpanningTree.append([self.nodes[finalStartElement], self.nodes[finalEndElement], self.edges[finalStartElement][finalEndElement]])
            visitedNodes[finalEndElement] = True
            edgeNumber += 1
            
        self.printSolution()

edges = [
    [0, 10, 20, 0, 0],
    [10, 0, 30, 5, 0],
    [20, 30, 0, 15, 6],
    [0, 5, 15, 0, 8],
    [0, 0, 6, 8, 0],
]


nodes = ['A','B','C','D','E']
graph = Graph(5, edges, nodes)

print('-'*10 + 'Prims Algorithm' + '-'*10)
graph.primsAlgorithm()


'''
Prim's vs Kruskal Algorithms

Kruskal:
    - Concentrates on Edges 
    - Finalize edge in each iteration
    
Prim's:
    - concentrates on Vertices 
    - Finalize Vertex in each iteration
    


Applicatoins of Kruskal Algorithm:
    - Landing Cables
    - Tv network
    - Tour Operations
    - lan networks
    - a network of pipes of drinking water or natural gas
    - an electric grid
    - single-link cluster
    
    
    
Applications of Prim's algorithm:
    - network for roads and rail tracks connecting all the citeis
    - irrigation channels and placing microwave towers
    - designing a fiber-optic grid or ics
    - traveling salesman problem
    - cluster analysis
    - pathfinding algorithms used in AI


'''



