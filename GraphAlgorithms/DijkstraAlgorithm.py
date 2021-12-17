


# Dijkstra algorithm
# Visualization and explanation ==> https://www.youtube.com/watch?v=CL1byLngb5Q

from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        
    def addNode(self,nodeValue):
        self.nodes.add(nodeValue)
        
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode) #add distance of edge starting from 'fromNode'
        self.distances[(fromNode, toNode)] = distance #add distance between two nodes


def dijkstraAlgorithm(graph, startNode): # time complexity O(V^2) , space complexity O(E)
    visitedNodes = {startNode:0}
    path = defaultdict(list)
    
    nodes = set(graph.nodes)
    
    while nodes:
        minNode = None
        # find min node
        for node in nodes:
            if node in visitedNodes:
                if minNode is None:
                    minNode = node
                elif visitedNodes[node] < visitedNodes[minNode]:
                    minNode = node
        #if minNode is still not found break
        if minNode is None:
            break
        
        nodes.remove(minNode)
        currentWeight = visitedNodes[minNode]
        
        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visitedNodes or weight < visitedNodes[edge]:
                visitedNodes[edge] = weight
                path[edge].append(minNode)
    
    return visitedNodes, path



graph = Graph()
# Add Nodes
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")
graph.addNode("F")
graph.addNode("G")
#Add edges
graph.addEdge("A", "B", 2)
graph.addEdge("A", "C", 5)
graph.addEdge("B", "C", 6)
graph.addEdge("B", "D", 1)
graph.addEdge("B", "E", 3)
graph.addEdge("C", "F", 8)
graph.addEdge("D", "E", 4)
graph.addEdge("E", "G", 9)
graph.addEdge("F", "G", 7)

print('-----Nodes-----')
print(graph.nodes)
print('-----Edges-----')
print(graph.edges)
print('-----Distances-----')
print(graph.distances)
print('-----Dijkstra Algorithm-----')

'''
                 [B]-----(3)------[E]        
                / | \            /   \       
               /  |  \          /     \      
             (2)  |   (1)     (4)     (9)    
            /     |     \     /         \    
           /      |      \   /           \   
        [A]      (6)      [D]            [G]      
           \      |                      /   
            \     |                     /    
            (5)   |                   (7)    
               \  |                   /      
                \ |                  /       
                 [C]------(8)------[F]      
'''

print(dijkstraAlgorithm(graph, 'A'))




'''
What if we have negative cycle in our graph
'''
# if we have negative cycle in our graph dijkstra algorithm wouldnt work 
# because djikstra algorithm would fall into infinite loop when trying to find minimum cycle (it will redo cycles to make it smaller)















































'''
    [B]             [E]
       \           /   
        \         /    
        (1)     (4)    
          \     /      
           \   /       
            [D]      
            
    [B]        
       \       
        \      
        (1)    
          \    
           \   
            [D] 
            
          [E]
         /   
        /    
     (4)     
     /       
   /         
[D]           



'''

