import heapq

# my solution
def getServerIndex(n, arrival, burstTime):
    # sort jobs by arrival time
    m = len(arrival)
    # sort by arrival time and then by index
    jobs = sorted([[arrival[i], burstTime[i], i] for i in range(m)], key=lambda x: (x[0],x[2]))
    
    availableServers = set(list(range(1, n + 1)))
    m = len(arrival)
    heap = []
    res = []

    for i in range(m):
        arrivalTime, burstTime, index = jobs[i]
        # restore all servers from heap which finish before or at arrival time
        while heap and arrivalTime >= heap[0][0]:
            time, completedId = heapq.heappop(heap)
            availableServers.add(completedId)

        if not len(availableServers):
            res.append(-1, index)
            continue

        # get the first available server and occupy it, choose smallest index
        serverId = sorted(list(availableServers))[0]
        # print("DEBUG: availableServers", availableServers, serverId)
        availableServers.remove(serverId)
        res.append((serverId, index))
        endTime = arrivalTime + burstTime
        heapq.heappush(heap, (endTime, serverId))

    # sort res by original index
    res = sorted(res, key=lambda x: x[1])
    res = [x[0] for x in res]    
    return res

# test 1
n = 4
arrival = [3,5, 1, 6,8]
burstTime = [9,2,10,4,5]
result = getServerIndex(n, arrival, burstTime)
print(result == [2,3,1,4,3], result)

# test 2
n = 3
arrival = [2,4,1,8,9]
burstTime = [7,9,2,4,5]
result = getServerIndex(n, arrival, burstTime)
print(result == [1,2,1,3,2], result)

