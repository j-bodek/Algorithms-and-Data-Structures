


# QUESTION 1: ROUTE BETWEEN NODES
# Given a directed graph and two nodes(S and E), design an algorithm to find out whether there is a route from S to E

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        # We would use BFS to do this task
        # PSEUDOCODE:
        # - Create fucntion with two parameters start and end nodes
        # - Create queue and enqueue start node to it
        # - Repeat this process until the end of elements in graph 
        # - If during the above process at some point in time we encounter the destination node, we return true
        # - make visited nodes as visit
        visitedNodes = [startNode]
        # Queue with enqueued startNode
        queue = [startNode]
        path = False #couse we yet don't know if it is path between start and end node
        while queue:
            currentVertex = queue.pop(0)
            for adjacentVertex in self.gdict[currentVertex]:
                #Check if node is already visited
                if adjacentVertex not in visitedNodes:
                    # if endNode is found
                    if adjacentVertex is endNode:
                        path = True
                        break
                    # if node isn't our looking endNode enqueue it to queue and then check it 'childNodes'
                    else:
                        visitedNodes.append(adjacentVertex)
                        queue.append(adjacentVertex)
                        
        return path



customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }

graph = Graph(gdict=customDict)
print(graph.checkRoute('a','j'))














