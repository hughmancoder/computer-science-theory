import math
import heapq
from collections import deque
import sys
# python3 pathfinder.py tests/test-2.txt astar manhattan
def read_file(map_file):
    with open(map_file, 'r') as f:
        rows, cols = map(int, f.readline().strip().split())
        start_row, start_col = map(int, f.readline().strip().split())
        end_row, end_col = map(int, f.readline().strip().split())
        matrix = []
        for _ in range(rows):
            row = list(map(str, f.readline().strip().split()))
            matrix.append(row)
    return (rows, cols), (start_row, start_col), (end_row, end_col), matrix

def calculateCost(mat, node1, node2):
    a,b = node1
    c,d = node2
    mab = int(mat[a][b])
    mcd = int(mat[c][d])
    if mcd - mab > 0:
        return 1 + mcd - mab 
    else:
        return 1

def calculateHeuristic(heuristic, src, dest):
    (x1, y1) = src
    (x2, y2) = dest
    if heuristic == "euclidean":
        return math.sqrt((x1 - x2)**2 + (y1-y2)**2)
    elif heuristic == "manhattan":
        return abs(x1-x2) + abs(y1-y2)
    
def bfs(grid, start, dest):
    queue = deque([(start, [])])
    visited = set(start)
    # keep track of parent of each node to construct path
    parent = {}
    parent[start] = None
    while queue:
        node, path = queue.popleft()
        visited.add(node)
        if node == dest:
            for x, y in path:
                grid[x][y] = '*'
            grid[dest[0]][dest[1]] = '*'
            return grid
        x,y = node
        for X, Y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= X < len(grid) and 0 <= Y < len(grid[0]) and  grid[X][Y] != 'X' and (X,Y) not in visited:
                queue.append([(X, Y), path + [node]])
                parent[(X, Y)] = node
                
    return None

def pathToMatrix(matrix, start, parent):
    path = []
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    for i, j in path[::-1]:
        matrix[i][j] = '*'
    return matrix

def ucs(grid, start, dest):
    queue = [(0, start)]
    parent = {}
    visited = set()
    while queue:
        # maintain the path as we calculate cost
        cost, node = heapq.heappop(queue)
        visited.add(node)
        if node == dest:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            for i, j in path[::-1]:
                grid[i][j] = '*'
            return grid
            
        row, col = node
        
        # previous: dir = [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]
        for X, Y in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= X < len(grid) and 0 <= Y < len(grid[0]) and grid[X][Y] != 'X' and (X,Y) not in visited:
                neighbor_cost = cost + calculateCost(grid, node, (X, Y))
                heapq.heappush(queue, (neighbor_cost, (X, Y)))
                parent[(X,Y)] = node
    return None

def printGrid(res):
    if res == "null" or res is None: print("null")
    else:
        r, c = len(res), len(res[0])
        for i in range(r):
            for j in range(c):
                print(res[i][j], end=" ")
            print()


class Node:
    def __init__(self, position, g_cost, h_cost, parent=None):
        self.position = position
        self.g_cost = g_cost # cost so far
        self.h_cost = h_cost # heuristic cost
        self.parent = parent
        # self.popped = False
    # calculate the total cost f(n) = g(n) + h(n)
    def f_cost(self):
        return self.g_cost + self.h_cost

    # add a comparison function to nodes so prioirity queue knows how to sort node objects
    def __lt__(self, other):
        return self.f_cost() < other.f_cost()

def h(heuristic, start, end):
    x1,y1 = start
    x2,y2 = end
    if heuristic == "manhattan":
        return abs(y1-y2) + abs(x1-x2)
    return (math.sqrt((y1-y2)**2 + (x1-x2)**2))

def astar(grid, start, dest, heuristic):
    # Initialize the start node
    # h_cost = h(heuristic, start, dest)
    h_cost = 0
    start_node = Node(start, 0, h_cost)
    # Initialize the open list with the start node
    open_list = [start_node]
    # Initialize the closed list as an empty set
    visited = set()
    # Loop until the open list is empty
    while open_list:
        # Get the node with the lowest f_cost value
        open_list.sort(key=lambda node: node.f_cost())
        current_node = open_list.pop(0)
        # current_node.popped = True
        # check if we have reached dest
        if current_node.position == dest:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            for x, y in path:
                grid[x][y] = '*'
            return grid

        visited.add(current_node.position)
        row, col = current_node.position
        for X, Y in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= X < len(grid) and 0 <= Y < len(grid[0]) and grid[X][Y] != 'X':
                neighbor = (X, Y) # same as neighbors
                if neighbor in visited:
                    continue
                cc = max(1, (int(grid[X][Y]) - int(grid[row][col])) + 1)
                g_cost = current_node.g_cost + cc
                # current_node.g_cost = min(current_node.g_cost, g_cost)
                h_cost = h(heuristic, neighbor, dest)
                child_node = Node(neighbor, g_cost, h_cost, current_node)
                open_list.append(child_node)
    return None         

def main():
    input_path = sys.argv[1]
    search = sys.argv[2]
    heuristic = ""
    if len(sys.argv) >= 4 and sys.argv[3]:
        heuristic = sys.argv[3]
    _, start, end, grid = read_file(input_path)
    if grid is None: 
        print('null')
        return
    zeroOffsetConvert = lambda xy: (xy[0] - 1, xy[1] - 1)
    start = zeroOffsetConvert(start)
    end = zeroOffsetConvert(end)
    matrix = []
    if search == 'bfs':
        matrix = bfs(grid, start, end)
    elif search == 'ucs':
        matrix = ucs(grid, start, end)
    elif search == "astar":
        matrix = astar(grid, start, end, heuristic)
    printGrid(matrix)

main()
# run: python3 pathfinder.py input-0-txt bfs 


