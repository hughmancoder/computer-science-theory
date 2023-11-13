import sys
import numpy as np

def loadInputs(input_file):
    with open(input_file, 'r') as f:
        rows, cols = map(int, f.readline().split())
        map_data = [list(f.readline().strip().split()) for _ in range(rows)]
        num_observations = int(f.readline())
        observations = [''.join(list(f.readline().strip())) for _ in range(num_observations)]
        error_rate = float(f.readline())
    return rows, cols, map_data, num_observations, observations, error_rate
    
def getProbabiltyMap(map_data, trellis, S):
    maps = []
    K = trellis.shape[0]
    T = trellis.shape[1]
    for t in range(T):
        map_t = np.zeros_like(map_data, dtype=float)
        for i in range(K):
            x, y = S[i]
            map_t[x, y] = trellis[i, t] # map probability to its coordinate in grid
        maps.append(map_t)
    return maps

def computeSensorError(error_rate, dit):
    return ((1-error_rate)**(4-dit))*(error_rate**dit)

def getNeighbors(map_data, i, j, rows, cols):
    neighbors = []
    for offset_i, offset_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # NSWE
        x, y = i + offset_i, j + offset_j
        if 0 <= x < rows and 0 <= y < cols and map_data[x][y] == '0':
            neighbors.append((x, y))
    return neighbors

def getTransitionMatrix(map_data, K, rows, cols, S):
    Tm = np.zeros((K, K))
    for i in range(rows):
        for j in range(cols):
            if map_data[i][j] == '0':
                neighbors = getNeighbors(map_data, i, j, rows, cols)
                for ni, nj in neighbors:
                    x = S.index((i, j))
                    y = S.index((ni, nj))
                    Tm[x, y] = 1.0 / len(neighbors)
    return Tm

def getObservation(map_data, i, j, rows, cols):
    observation = ""
    for offset_i, offset_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # NSWE
        x, y = i + offset_i, j + offset_j
        if 0 <= x < rows and 0 <= y < cols:
            if map_data[x][y] == 'X': 
                observation += '1'
            else: 
                observation += '0'
        else: 
            observation += '1'
    return observation

def getHammingDistance(str1,str2):
    # dit (hamming distance) denotes the number of directions are reporting erroneous values
    dist = 0
    if len(str1) != len(str2): return dist
    for c1, c2 in zip(str1, str2):
         if c1 != c2: dist += 1
    return dist

def getEmisionMatrix(map_data, rows, cols, S, Y, error_rate):
    # em is of size rows * cols
    N = len(Y)
    K = len(S)
    Em = np.zeros((K, N))
    for i, (x, y) in enumerate(S):
        for j in range(N):
            # get number of incorrect
            recorded_observation = Y[j]
            observation = getObservation(map_data, x, y, rows, cols)
            dit = getHammingDistance(recorded_observation, observation)
            # print(recorded_observation, observation, dit)
            Em[i, j] = computeSensorError(error_rate, dit)
    return Em

def viterbiForward(map_data, O, S, Q, Y, Tm, Em, N, K):
    """
    Y, a sequence of observations Y = (y1,y2,...,yT )
    O, observation space O = {o1, o2,...,oN}
    S, state space S = {s1,s2,...,sK} // Here, K refers to the traversable positions
    Q, array of initial probabilities Q = (π1,π2,...,πK) Y, a sequence of observations Y = (y1,y2,...,yT)
    Tm, transition matrix of size K x K
    Em, emission matrix of size K x N
    """
    T = len(Y)
    trellis = np.zeros((K, T))

    for i in range(K):
        y0 = O.index(Y[0])
        trellis[i][0] = Q[i] * Em[i][0]

    for j in range(1, T):
        for i in range(K):
            max_prob = 0.0
            for k in range(K):
                prob = trellis[k][j - 1] * Tm[k][i] * Em[i][j]
                if prob > max_prob:
                    max_prob = prob
            trellis[i][j] = max_prob

    return trellis

def main(input_file):
    output_file = "output.npz"
    rows, cols, map_data, num_observations, observations, error_rate = loadInputs(input_file)

    N = 16
    O = [''.join(bin(i)[2:].zfill(4)) for i in range(16)] # observation space
    S = [(i, j) for i in range(rows) for j in range(cols) if map_data[i][j] != 'X']
    K = len(S) 
    Q = [1.0/K for _ in range(K)] # array of initial probabilities
    Y = observations

    Tm = getTransitionMatrix(map_data, K, rows, cols, S)
    Em = getEmisionMatrix(map_data, rows, cols, S, Y, error_rate)
    
    trellis = viterbiForward(map_data, O, S, Q, Y, Tm, Em, N, K)
    output_map = getProbabiltyMap(map_data, trellis, S)
    np.savez("output.npz", *output_map)

# Allows You to Execute Code When the File Runs as a Script
if __name__ == '__main__':
    main(sys.argv[1])
    