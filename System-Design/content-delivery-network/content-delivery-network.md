# Content delivery network system design

A distributed system of servers located around the globe with the goal of delivering content (images, videos, static files, etc.) to users with improved speed and reduced latency. It leverages caching and intelligent routing to bring content closer to the end user.

## Components

- Origin Server: The central server where your original website or application content is stored. (setup multiple origin servers for reduncancy and geolocation efficiency)

- Edge Servers (Points of Presence - PoPs): Servers strategically placed near users in various geographic locations. Edge servers cache content to minimize the distance data needs to travel, reducing latency and improving load times

## Flow

- User Request: The user's browser sends a request for content (e.g. an image) to the CDN.

- DNS Resolution: The user's request is directed to the nearest CDN edge server via DNS (Domain Name System) resolution. DNS will map the hostname of the content to an optimal edge server

- Cache Check: The edge server checks if the requested content is available in its cache
- Cache Hit: Content is delivered immediately to the user
- Cache Miss: The request is forwarded to the origin server
- Origin Fetch (Cache Miss Only): The edge server retrieves the content from the origin server
- Caching: The edge server caches a copy of the retrieved content (following its caching strategy).
- Content Delivery: The edge server delivers the content to the user.

## Caching Strategies for edge servers (PoPs)

Least Recently Used (LRU): Discards the content that's been unused for the longest when the cache is full. (could be quite robust to expire old content)

Least Frequently Used (LFU): Evicts the least frequently accessed content. (might be great to show trending and popular content)

Time-to-Live (TTL): Caches items for a set duration before re-fetching. (great for content that doesn't change often)

## Load Balancing Strategies

- Geographic-based Distribution: Routes users to the nearest edge server.
- Round Robin: Distributes requests across edge servers in a cycle.
- Health Checks: Load balancers check the health of servers and remove problematic ones from serving requests.
- Handling Peak Traffic:
- Autoscaling: Add or remove edge servers dynamically based on load.
- Overflow Capacity: Use multiple CDNs and failover mechanisms.

## Simplified Diagram

```text
+---------+       +--------------+
|  User   | -----> |  Edge Server |
+---------+       +--------------+
     |                 |
     | (Cache Hit?)    |
     v                 v
   +---------+     +-------------+
   | Origin  |     | Load        |
   | Server  | <---+  Balancer   |
   +---------+     +-------------+`
```
