import sys
import numpy as np

class Node:
    def __init__(self,point,d=None,val=None,left=None,right=None):
        self.label = point[-1]
        self.point = point[:-1]
        self.d = d
        self.val = val
        self.left = left
        self.right = right

class KdTree:
    def __init__(self, P, d):
        self.split_dim = d
        self.labels = P[:, -1]
        self.M = P.shape[1] - 1
        self.root = self.BuildKdTree(P, 0)

    def BuildKdTree(self,P,D=0):
        d = D % 11
        if P is None or P.size == 0: return None
        elif P.shape[0] == 1:
            return Node(P[0], d=d, val=P[0][d])
        else:
            sorted_indices = np.argsort(P[:, d])
            sorted_points = P[sorted_indices]
            median_index = sorted_indices[len(sorted_indices) // 2]
            # Median value along dimension among points in P.
            val = P[median_index][d]
            point = P[median_index] # point at median along dimension d
            node = Node(point,d=d,val=val)
        
            left_points = np.empty((0,12), int)
            right_points = np.empty((0,12), int)    
            for cur_point in P:
                if (cur_point == point).all():
                    continue
                if cur_point[d] <= val: 
                    left_points = np.append(left_points, [cur_point], axis=0)
                elif cur_point[d] > val:
                    right_points = np.append(right_points, [cur_point], axis=0)

            # create new node
            node = Node(point,d=d,val=val)
            node.left = self.BuildKdTree(left_points, D + 1)
            node.right = self.BuildKdTree(right_points,D + 1)
        return node
            

    def distance(self, node, y):
        return  np.linalg.norm(node.point - y)

    def distance_lb(self, node,y):
        return node.point[node.d] - y[node.d]
    
    def search(self, y):
        best_node, best_dist = self.search_helper(self.root, y)
        return best_node.label, best_dist

    def search_helper(self, node, y, best_node=None, best_dist=None):
        if node is None:
            return best_node, best_dist
        # Record the leaf node as the current best node.
        if best_node is None:
            best_node = node
            best_dist = self.distance(node, y)
        else:
            dist = self.distance(node, y)
            if dist < best_dist:
                best_node = node
                best_dist = dist
    
        # Unwind the recursion of the tree, calculating at each node the lower bound of the distance to y of the other branch
        d = node.d
        lb_distance = self.distance_lb(node, y)
        if lb_distance >= 0:
            near_node = node.left
            far_node = node.right
        else:
            near_node = node.right
            far_node = node.left
        
        # 4. If the lower bound is larger than the current best distance, continue ascending the tree.
        best_node, best_dist = self.search_helper(near_node, y, best_node, best_dist)
        # if we find a shorter lower bound we explore that branch
        if far_node and abs(self.distance_lb(node, y)) <= best_dist:
            best_node, best_dist = self.search_helper(far_node, y, best_node, best_dist)
        return best_node, best_dist
        

    def search_bf(self, train_data, query_point):
        best_dist = np.inf
        best_label = None
        for sample in train_data:
            x = sample[:-1]
            y = sample[-1]
            dist = np.linalg.norm(np.array(x) - np.array(query_point))
            if dist < best_dist:
                best_label = y
                best_dist = dist
        return best_label, best_dist
        
def getInput():
    train_file,test_file, dim = sys.argv[1], sys.argv[2], int(sys.argv[3])
    train_data = np.genfromtxt(train_file, delimiter=None, skip_header=1, usecols=range(12))
    test_data = np.genfromtxt(test_file, delimiter=None, skip_header=1, usecols=range(11))
    return np.array(train_data), np.array(test_data), dim

def main():
    train_data, x_test, split_dim = getInput()
    Kdt = KdTree(train_data, split_dim)
    Kdt.root.d = split_dim
    for query_point in x_test:
        expected_res, expected_dist = Kdt.search_bf(train_data, query_point)
        best_label, distance= Kdt.search(query_point)
        print(int(expected_res))
main()