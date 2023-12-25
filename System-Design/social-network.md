# System Design Specification for a Large Social Network

- **Description**: Designing data structures for a large social network like Facebook or LinkedIn, including algorithms for finding the shortest path between two people.
- **Considerations**: Data structure design, shortest path algorithm.

## Data Structure Design

- **Graph Representation:**

  - Use a graph to model the social network, where nodes represent users and edges represent connections (friendships, following, etc.).
  - Consider a directed graph to capture asymmetric relationships.
  - use bi-directional bfs starting from person A and person B in parallel. O(K^(q/2)) if each person has K friends with a path of length q.

- **Data Storage:**

  - **Graph Database:** Optimized f or storing and querying graph data (e.g., Neo4j, OrientDB).
  - **Relational Database:** Can be used with appropriate schema design, but might not be as efficient for graph-specific queries.

- **User Data:**

  - Store user profiles (name, email, interests, etc.) in a separate table or collection.

```
class User:
    id: long # use an atomic integer/long for unique id
    name: string
    email: string
    metadata: object
    interests: List[string]
    friends: List[User]

function recommend_friends(user):
    # Get user's friends and friends of friends
    friends_of_friends = find_friends_of_friends(user)

    # Filter out existing friends and the user themselves
    potential_friends = filter_connections(friends_of_friends, user)

    # Rank potential friends based on mutual connections and interests
    ranked_friends = rank_friends(potential_friends, user)

    # Return top N recommendations
    return top_n(ranked_friends, N)


function computer_mutual friends(user1, user2):
    # Get friends of user1
    friends1 = user1.friends

    # Get friends of user2
    friends2 = user2.friends

    /*
    Return intersection of friends (could implement this with a set via list(set(lst1) & set(lst2)))

    converting a list to a set takes O(n) time, and finding the intersection of two sets takes O(min(n, m)) time as a set is hash-based. Therefore, the total time complexity is O(n + m).
    */
    return intersection(friends1, friends2)
```

### Helper functions

```
function find_friends_of_friends(user):
    # Iterate through user's friends and collect their friends
    friends_of_friends = []
    for friend in user.friends:
        for friend_of_friend in friend.friends:
            friends_of_friends.append(friend_of_friend)
    return friends_of_friends

function filter_connections(connections, user):
    # Filter out existing friends and the user
    filtered_connections = []
    for connection in connections:
        if connection not in user.friends and connection != user:
            filtered_connections.append(connection)
    return filtered_connections

function rank_friends(potential_friends, user):
    # Calculate a score for each potential friend based on mutual connections and interests
    ranked_friends = []
    for friend in potential_friends:
        score = calculate_friend_score(friend, user)
        ranked_friends.append((friend, score))
    return sorted(ranked_friends, key=lambda x: x[1], reverse=True)

# Example scoring function (customize based on specific criteria)
function calculate_friend_score(friend, user):
    mutual_friends_count = count_mutual_friends(friend, user)
    shared_interests_count = count_shared_interests(friend, user)
    return mutual_friends_count + shared_interests_count

```

- **Relationship Data:**
  - Store connections between users (friend lists, following lists) in a separate table or collection.
- **Indexing:**
  - Create indexes on user IDs and relationship types for fast lookups and traversals.

## Shortest Path Algorithm

- **Choice:**
  - **Breadth-First Search (BFS):** Efficient for finding the shortest path in unweighted graphs.
  - consider bidirectional bfs from person A and person B

## Handling millions of users

```
servers = hashmap<int, Server> // ServerId, Server
personToServerMap = hashmap<int, int> // <personId, ServerId>

function addServer(self, serverId):
      server = Server(serverId)
      self.servers[serverId] = server

function addUser(self, userId, serverId):
    if serverId in self.servers:
        self.servers[serverId].users[userId] = "User data"  # Add user data
        self.personToServerMap[userId] = serverId

function getMachineWithID(self, serverId):
    return self.servers.get(serverId, None)

function getMachineIdForUsers(self, userId):
    return self.personToServerMap.get(userId, None)

function getPersonWithId(self, userId):
    serverId = self.getMachineIdForUsers(userId)
    if serverId is not None:
        return self.servers[serverId].users.get(userId, None)
    return None
```

- reduce the number of jumps by grouping machines up geographically and look up friedns all at once for a given machine

## Additional Considerations

**Scalability:**

- Partition the graph horizontally across multiple servers for very large networks (see approach above)

**Use caching techniques to reduce database load for frequent queries**

- Taking Advantage of Caching: In a social media system, caching can be used to store frequently accessed data, such as user profiles, posts, or friend lists. This reduces the load on the database and improves response times. For example, when a user's profile is accessed, the system could cache the profile data. Subsequent requests for the same profile can then be served from the cache instead of querying the database.

**failures**
Handling Server Failures: In a distributed system, server failures are inevitable. To handle this, redundancy and replication strategies are used. Data is replicated across multiple servers so if one server fails, the data is still available from another server. Load balancers can detect failed servers and redirect traffic to healthy ones. Regular backups are also crucial to recover data in case of severe failures.

**efficient graph exploration**
Searching Until the End of the Graph: In a social media context, this could refer to traversing a social graph (a graph where nodes represent users and edges represent relationships). In most cases, it's not practical or necessary to traverse the entire graph. For example, when displaying a user's friends or friend suggestions, only a small portion of the graph close to the user needs to be explored. Techniques like Breadth-First Search (BFS) can be used for such operations.

**asymmetry of data**
Handling Real World Situations Where Some Friends Have More Than Others: In a social media system, some users (like celebrities) may have many more friends or followers than typical users. This can create challenges for operations like news feed generation or friend recommendation. To handle this, the system could use techniques like fan-out on write (where posts are pushed to followers when created) or fan-out on read (where posts are pulled when a user accesses their feed), depending on the usage patterns. For friend recommendations, the system could limit the number of recommendations generated from a single user to ensure diversity.

- **Data Updates:**
  - Design efficient mechanisms for handling frequent changes in user relationships and data.
- **Privacy and Security:**
  - Implement access controls and privacy settings to protect user data.
  - Sanitize inputs and outputs to prevent security vulnerabilities.
- **Recommendations:**

  - Consider using graph algorithms for other features like: - Friend recommendations - Content personalization - Community detection
