# System Design for a Rate Limiter

A rate limiter is a tool used in software development to control the amount of traffic sent or received by a network interface controller. It's often used to prevent abuse and denial-of-service (DoS) attacks, ensure fair usage of shared resources, and optimize server load and control traffic flow.

## Purpose

- Prevent abuse and denial-of-service (DoS) attacks.
- Ensure fair usage of shared resources.
- Optimize server load and control traffic flow

## Common Algorithms

### Fixed Window

- Tracks requests within a defined time window (e.g., 100 requests per minute).
- Simple to implement.
- Can be "bursty" at the beginning of each window.

### Sliding Window

- Divides time into smaller windows. Maintains a count of requests in each.
- Smoother traffic flow than fixed window.
- More computationally intensive.

### Token Bucket

- Each user/IP gets a bucket of tokens, replenished at a fixed rate.
- Allows for flexibility and handling bursts.
- Requires tracking token state.

## System Components

### In-Memory Storage

Use Redis or Memcached for speed and efficiency.
Store keys such as:
User ID or IP address
Timestamps of requests (for sliding window)
Token count (for token bucket)

## Rate Limiting Logic:

Implemented as middleware or an API gateway layer.
Fetches data from the storage.
Applies selected algorithm's rules.
Allows the request or returns an HTTP 429 (Too Many Requests) error.
Distributed Coordination (Optional):

For rate limiting across multiple servers, use a centralized message queue (Kafka, RabbitMQ) or a distributed cache to synchronize rate limit data.

## Scalability Considerations

- Horizontal Scaling: Add more servers and replicate the rate-limiting logic across them.
- Distributed Caching: Use a distributed cache like Redis Cluster to handle large rate limit volumes.
  Example: Fixed Window with Redis

```python
# Define the maximum number of requests per minute
MAX_REQUESTS_PER_MINUTE = 100

# Function to handle incoming requests
def handle_request(request):
    # Extract the user ID from the request
    user_id = extract_user_id_from(request)

    # Get the current timestamp, truncate to minute interval
    current_time = get_current_timestamp_truncated_to_minute()

    # Construct a key for this user and minute
    key = construct_key("ratelimit", user_id, current_time)

    # Increment the request count for this user and minute
    requests = increment_request_count_in_datastore(key)

    # Set an expiration on the key for efficient cleanup
    set_key_expiration_in_datastore(key, 60)

    # If the number of requests is greater than the maximum allowed
    if requests > MAX_REQUESTS_PER_MINUTE:
        # Return an error response
        return error_response("HTTP 429 Too Many Requests")
    else:
        # Allow the request to proceed
        allow_request()
```
