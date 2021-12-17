



'''
Graph Type                         |  BFS  |  Dijkstra  |  Bellman Ford  |  Floyd Warshall  |
---------------------------------------------------------------------------------------------------------------------------
Unweighted - undirected            | WORKS |   WORKS    |      WORKS     |       WORKS      |
---------------------------------------------------------------------------------------------------------------------------
Unweighted - directed              | WORKS |   WORKS    |      WORKS     |       WORKS      |
---------------------------------------------------------------------------------------------------------------------------
Positive - weighted - undirected   |   X   |   WORKS    |      WORKS     |       WORKS      |
---------------------------------------------------------------------------------------------------------------------------
Positive - weighted - directed     |   X   |   WORKS    |      WORKS     |       WORKS      |
---------------------------------------------------------------------------------------------------------------------------
Negative - weighted - undirected   |   X   |   WORKS    |      WORKS     |       WORKS      |
---------------------------------------------------------------------------------------------------------------------------
Negative = weighted - directed     |   X   |     X      |      WORKS     |         X        |
---------------------------------------------------------------------------------------------------------------------------

'''

'''
BFS vs Dijkstra vs Bellman Ford

= Time complexity:
    - BFS => O(V^2)
    - Dijkstra => O(V^2)
    - Bellman Ford => O(VE)
    - Floyd Warshall => O(V^3)

-----------------------------------------------------------------------------------------------------------------
    
= Space complexity:
    - BFS => O(E)
    - Dijkstra => O(V)
    - Bellman Ford => O(V)
    - Floyd Warshall => O(V^2)

-----------------------------------------------------------------------------------------------------------------
    
= Implementation:
    - BFS => Easy
    - Dijkstra => Moderate
    - Bellman Ford => Moderate
    - Floyd Warshall => Moderate

-----------------------------------------------------------------------------------------------------------------
    
= Limitations:
    - BFS => Not work for weighted graph
    - Dijkstra => Not work for negative cyclse
    - Bellman Ford => N/A
    - Floyd Warshall => Not work for negative cycle

-----------------------------------------------------------------------------------------------------------------
    
= Unweighted Graphs:
    - BFS => Words - Use this as time complexity is good and easy to implement
    - Dijkstra => Works - Not use as implementation not easy
    - Bellman Ford => Works - Not use as time complexity is bad
    - Floyd Warshall => Can be used

-----------------------------------------------------------------------------------------------------------------
    
= Weighted Graphs:
    - BFS => Not Supported
    - Dijkstra => Works - Use as time complexity is better than Bellman 
    - Bellman Ford => Not use as time complextiy is bad
    - Floyd Warshall =>  Can be preferred as implementation easy

-----------------------------------------------------------------------------------------------------------------
    
= Negative Cycle:
    - BFS => Not supported
    - Dijkstra => Not supported
    - Bellman Ford => Use this as others not support
    - Floyd Warshall => Not supported

-----------------------------------------------------------------------------------------------------------------
'''




