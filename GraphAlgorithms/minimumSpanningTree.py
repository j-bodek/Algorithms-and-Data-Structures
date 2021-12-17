


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
        
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
        
    def union(self, x, y):
        xroot = self.find(x) # find parent node of x
        yroot = self.find(y) # find parent node of y
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
print(f"Parent node of A => {disjoint.find('A')}")
# union A and B
disjoint.union('A','B')
print(f"Parent node of B => {disjoint.find('B')}")
print(disjoint)























