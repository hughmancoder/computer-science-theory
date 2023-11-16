from collections import defaultdict
from collections import deque

"""Kahn's algorithm for topological sorting"""

def find_build_order(projects, dependencies):
    graph = defaultdict(list)
    
    in_degree = {}

    for project in projects:
        in_degree[project] = 0

    for u, v in dependencies:
        graph[u].append(v)
        in_degree[v] += 1
    
    q = deque([key for key,value in in_degree.items() if value == 0])

    res = []

    while q:
        node = q.popleft()
        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                q.append(neighbour)
        res.append(node)


    return res
    

if __name__ == "__main__":
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    print(find_build_order(projects, dependencies)) # ['e', 'f', 'b', 'a', 'd', 'c']
    