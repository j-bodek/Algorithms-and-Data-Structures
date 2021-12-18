

'''
Build Order
'''
# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project).
# All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to 
# be built. If there is no valid build order, return an error.

# Input:
# - Projects: a,b,c,d,e,f
# - Dependencies: (a,d),(f,b),(b,d),(f,a),(d,c)
# project d is dependent on project a / project b is dependent on project f / and so on ...
# Output:
# - e,f,a,b,d,c 

# We can solve this problem by creating directed graph
# Find all nodes that are dependent (a,b,c,d) (that cannot be done befor previously done someone else)
# Fina all undependent nodes (e,f)

# Find order by taking out nodes without dependencies then links be broken and other nodes will become independent
# After deleting E and F => A and B will become independent then after deleting them => D become independent after deleting it => C becomes independent 
# Final order: E,F,A,B,D,C


def createGraph(projects, dependencies):
    projectGraph = {}
    # loop through project
    for project in projects:
        # add projects as key values
        projectGraph[project] = [] #initialize to empty list
        
    # loop through pairs of dependencies
    for pair in dependencies:
        projectGraph[pair[0]].extend(pair[1])

    return projectGraph

customGraph = createGraph(['A', 'B', 'C', 'D', 'E', 'F'], [('A','D'), ('F', 'B'), ('B','D'), ('F','A'), ('D','C')])
# keys of dictionary are projects and values are projects which depend on it
print(customGraph)

def findProjectsWithDependencies(graph):
    return list(set([project for projects in graph.values() for project in projects]))

projectsWithDependencies = findProjectsWithDependencies(customGraph)
print(projectsWithDependencies)

# Find out nodes without dependencies
def findProjectsWithoutDependencies(graph, projectsWithDependencies):
    return list(set([project for project in graph.keys() if project not in projectsWithDependencies]))

projectWithoutDependencies = findProjectsWithoutDependencies(customGraph, projectsWithDependencies)
print(projectWithoutDependencies)

def findBuildOrder(projects, dependencies):
    buildOrder = []
    projectGraph = createGraph(projects, dependencies)
    while projectGraph:
        projectsWithDependencies = findProjectsWithDependencies(projectGraph)
        projectWithoutDependencies = findProjectsWithoutDependencies(projectGraph, projectsWithDependencies)
        if len(projectWithoutDependencies) == 0 and projectGraph:
            raise ValueError('Cycle inside the build order')
        buildOrder.extend(projectWithoutDependencies)
        for project in projectWithoutDependencies:
            del projectGraph[project]
            
    return buildOrder

buildOrder = findBuildOrder(['A', 'B', 'C', 'D', 'E', 'F'], [('A','D'), ('F', 'B'), ('B','D'), ('F','A'), ('D','C')])
print('-'*40)
print(f'Build Order ==> {buildOrder}')



