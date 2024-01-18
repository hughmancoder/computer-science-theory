def dijkstra(graph, startProduct):
    n = len(graph)
    minDistances = [float('inf')] * n
    visited = [False] * n
    minDistances[startProduct] = 0
    for _ in range(n):
        minIndex = -1
        for j in range(n):
            if not visited[j] and (minIndex == -1 or minDistances[j] < minDistances[minIndex]):
                minIndex = j
        if minDistances[minIndex] == float('inf'):
            break
        visited[minIndex] = True
        for j in range(n):
            if graph[minIndex][j] != 0:
                potentialDist = minDistances[minIndex] + graph[minIndex][j]
                if potentialDist < minDistances[j]:
                    minDistances[j] = potentialDist
    return minDistances
 
"""
let graph = [
    [0, 2, 0, 1, 0],
    [2, 0, 3, 0, 0],
    [0, 3, 0, 4, 0],
    [1, 0, 4, 0, 5],
    [0, 0, 0, 5, 0]
];

What is the output when the recommendation system calls dijkstra(graph, 0); to find the least similar products to the current product (Product 0)?

Step1: draw out graph 

[0, 2, 5, 1, 6]    

"""