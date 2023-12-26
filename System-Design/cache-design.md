# System Design: Caching Mechanism for Web Server

## Introduction

A caching mechanism is crucial for a web server, especially when dealing with a large number of machines and high traffic. It can significantly reduce the load on the server, decrease response times, and improve the overall user experience.

## Design Considerations

Distributed Cache: Given the scale of 100 machines, a distributed cache like Memcached or Redis would be suitable. These systems allow data to be stored across multiple nodes, increasing the overall cache capacity and providing redundancy.

Cache Invalidation: A strategy needs to be in place for invalidating cache entries when the underlying data changes. This could be a time-based strategy (TTL), where entries are automatically removed after a certain period, or an event-based strategy, where entries are invalidated when a change event occurs.

Cache Eviction Policy: When the cache is full, a policy needs to be in place to decide which entries to remove. Common policies include Least Recently Used (LRU), where the entries that haven't been accessed for the longest time are removed, or Least Frequently Used (LFU), where the entries that are accessed the least frequently are removed.

Load Balancing: Load balancing strategies should be used to distribute requests evenly across the cache nodes. This can be achieved using consistent hashing or other load balancing algorithms.

## Psuedocode

```
# LRU CACHE
class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Key-value store
        self.access_time = {}  # Store access time for LRU eviction policy; Alternatively we could use a linked list data structure of Nodes to maintain a queue like data structure with stale data being at the end of the linked list

    def get(self, key):
        if key in self.cache:
            self.access_time[key] = time.time()  # Update access time
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            # Evict least recently used entry
            oldest_key = min(self.access_time, key=self.access_time.get)
            del self.cache[oldest_key]
            del self.access_time[oldest_key]
        self.cache[key] = value
        self.access_time[key] = time.time()
```

## Distributed cache strategies

- Consistent Hashing (common): This is a strategy that allows cache nodes to be added or removed without significantly changing the mapping of keys to cache nodes. It minimizes the reorganization of existing keys when a node is added or removed.

- Sharding: This involves splitting the cache data across multiple nodes. Each node is responsible for storing a subset of the cache data. The specific shard for a given key is typically determined using a hash function. e.g: node X = hash(key) % n, where n is the number of nodes.

- Replication: This involves duplicating the entire cache across multiple nodes. This can increase read availability, but it also increases the complexity of writes, as they need to be propagated to all nodes.

- Partitioning: This involves dividing the cache into isolated partitions, each managed by a separate cache server. This can be combined with replication for increased reliability.

The best approach depends on the specific requirements of the system. However, a common and often effective approach is to use consistent hashing for distributing keys among cache nodes. This strategy provides a good balance between load distribution and minimizing key remapping when nodes are added or removed.

## Partitioning vs Sharding

Partitioning and sharding are both techniques used in distributed systems to split large datasets into smaller, more manageable parts. However, they are used in slightly different contexts and have different implications.

Partitioning:

Partitioning is typically used within a single database and involves dividing a table into smaller, more manageable parts, known as partitions. Each partition is stored separately and can be queried independently. The data is divided based on a specified key, such as date, ID, or region.

Partitioning can help improve performance, manageability, and availability of applications. It allows operations to be performed on a subset of the data, reducing I/O operations and improving query performance.

Sharding:

Sharding, on the other hand, is a method used in distributed databases where the data is split across multiple databases or servers, known as shards. Each shard holds a subset of the data and operates independently of the others.
