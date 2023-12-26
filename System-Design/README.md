# Key Concepts

## Horizontal vs. Vertical Scaling

- Vertical scaling: Increasing the resources of a specific node, like adding more memory to a server to handle load changes.
- Horizontal scaling: Increasing the number of nodes, such as adding additional servers to distribute the load evenly.

## Load Balancer

- Typically, scalable websites use load balancers to distribute traffic evenly across servers to prevent one server from crashing the entire system.

## Database Denormalization and NoSQL

- Joins in relational databases can slow down as the system grows, so denormalization involves adding redundant information to a database to speed up reads.
- NoSQL databases do not support joins and are designed for better scalability.

## Database Partitioning (Sharding)

- Sharding involves splitting data across multiple machines while ensuring you can locate which data is on which machine.
- Common partitioning methods include vertical partitioning, key-based (or hash-based) partitioning, and directory-based partitioning.

## Caching

- In-memory caches can deliver rapid results and are placed between the application layer and the data store to store frequently accessed data.

## Asynchronous Processing & Queues

- Slow operations should be done asynchronously to prevent users from waiting indefinitely.
- Queues of jobs can be processed in advance or users can be notified when the process is complete.

## Networking Metrics

- Bandwidth: The maximum data transfer rate expressed in bits per second.
- Throughput: The actual amount of data transferred in a unit of time.
- Latency: The delay between sending and receiving data.
