

'''
Floyd Warshall
'''
# Algorithm which solve all pairs shortest paths problem

# Visualization and Explanation of floyd warshall algorithm ==>  https://www.youtube.com/watch?v=4OQeCuLYj-4

'''
Why Floayd Warshall algorithm?
'''
# With any given node they can be only 3 possible way to find optimal distance between other nodes:
# - The vertex is not reachable (no any edge between node)
# - Two vertices are directly connected (this is the best solution it can be imporved vie other vertex)
# - Two vertices are connected via other vertex


INF = 9999
# helper print solution function
def printSoution(numberVertices, distance):
    for index in range(numberVertices):
        for insideIndex in range(numberVertices):
            if distance[index][insideIndex] == INF:
                print('INF', end=" ")
            else:
                print(distance[index][insideIndex], end=" ")
        print(" ")


def floydWarshal(numberVertices, Graph): # time complexity => O(V^3), space complexity => O(V^2) (couse we create 2d matrix)
    distance = Graph
    for index in range(numberVertices):
        # now visit each cell in two dimensional matrix 
        for row in range(numberVertices):
            for column in range(numberVertices):
                distance[row][column] = min(distance[row][column], distance[row][index] + distance[index][column])

    printSoution(numberVertices, distance)

Graph = [
        [0, 8, INF,1],
        [INF, 0, 1,INF],
        [4, INF, 0,INF],
        [INF, 2, 9,1]
        ]

floydWarshal(4, Graph)



































