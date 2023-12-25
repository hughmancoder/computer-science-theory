from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    """ BFS Search """
    def is_route(self, start, end):
        if start == end:
            return True

        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                if node in self.graph:
                    for neighbour in self.graph[node]:
                        if neighbour == end:
                            return True
                        if neighbour not in visited:
                            queue.append(neighbour)
        return False



graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('A', 'D')

print(graph.is_route('A', 'C') == True) 
print(graph.is_route('A', 'E') == False)
