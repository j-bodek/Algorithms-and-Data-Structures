

'''
Bellman Ford Algorithm
'''
# Bellman Ford algorithm is used to find single source shortest path problem. If there is a negetive
# cycle it catches it and report its existence.

# Bellman Ford Visualization and Explanation ==>  https://www.youtube.com/watch?v=obWXjtg0L64

'''
Why Bellman Ford runs V - 1 times?
'''
# If any node is achieved better distance in previous iteration, then that better distance is used to 
# improve distance of other vertices

# Bellman Ford runs V-1 times because maximum number of edges between two vertex is
# V-1 (where V is total number of vertices)



class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []
        
    def addEdge(self, startElement, endElement, weight):
        self.graph.append([startElement, endElement, weight])
                
    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, dist, sourceVertex):
        print('\n'.join([f'{sourceVertex} --> {key}  takes  {value}  units' for key,value in dist.items()]))

    def bellmanFord(self, sourceVertex):
        #set all cost of distance to infinity and sourceVertex to 0
        dist = {i : float("Inf") for i in self.nodes}
        dist[sourceVertex] = 0
        
        # run loop for V-1 iterations and inside this loops run another which will update weights of vertieces
        for iteration in range(self.vertices-1):
            # loop through all edges in graph
            for startElement, endElement, weight in self.graph:
                #updata weights
                if dist[startElement] != float('Inf') and dist[startElement] + weight < dist[endElement]:
                    dist[endElement] = dist[startElement] + weight
        # identify negative cycle (run loop V times)
        for startElement, endElement, weight in self.graph:
            # if elements will keep changeing it will return message
            if dist[startElement] != float('Inf') and dist[startElement] + weight < dist[endElement]:
                print('Graph contains negative cycle')
                return

        #if everything is ok
        self.printSolution(dist, sourceVertex)



graph = Graph(5)
#add vertices
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")
#add edges
graph.addEdge("A", "C", 6)
graph.addEdge("A", "D", 6)
graph.addEdge("B", "A", 3)
graph.addEdge("C", "D", 1)
graph.addEdge("D", "C", 2)
graph.addEdge("D", "B", 1)
graph.addEdge("E", "B", 4)
graph.addEdge("E", "D", 2)

#run bellman Form algorithm
graph.bellmanFord("E")




















