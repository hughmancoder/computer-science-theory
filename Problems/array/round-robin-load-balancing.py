import heapq

# RR template
def get_server_index_(n, m, arrival_time, process_time):
    """
    Function for finding the load on each server
    """
    # Stores the load on each Server
    load_on_server = [0] * m
 
    # Minimum priority queue for
    # storing busy servers according
    # to their release time
    busy_servers = []
 
    # Set to store available Servers
    available_servers = set(range(m))
 
    # Iterating through the requests.
    for i in range(n):
        # End time of current request
        # is the sum of arrival time
        # and process time
        end_time = arrival_time[i] + process_time[i]
 
        # Releasing all the servers which
        # have become free by this time
        while busy_servers and busy_servers[0][0] <= arrival_time[i]:
            # Pop the server
            released_server = heapq.heappop(busy_servers)
            # Insert available server
            available_servers.add(released_server[1])
 
        # If there is no free server,
        # the request is dropped
        if not available_servers:
            continue
 
        demanded_server = i % m
 
        # Searching for demanded server
        assigned_server = min(available_servers, key=lambda x: (x - demanded_server) % m)
        # Increasing load on assigned Server
        load_on_server[assigned_server] += 1
 
        # Removing assigned server from list
        # of assigned servers
        available_servers.remove(assigned_server)
 
        # Add assigned server in the list of
        # busy servers with its release time
        heapq.heappush(busy_servers, (end_time, assigned_server))
 
    # Function to print load on
    print_load_on_each_server(m, load_on_server)

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

