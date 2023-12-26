# System Design: Duplicate URLs Detection

A system that can detect duplicate documents among billions of URLs is crucial for many applications, such as search engines, where it's important to avoid indexing the same content multiple times. This system needs to be highly efficient to handle such a large volume of data.

## Context

Each url of 100 characters on average might take up 4 bytes. If we have 1 trillion URLs, we would need 4 TB of storage. We probably are not going to hold this much data in memory. In the case of all data being in memory we could use a hashtable.

## Design Considerations

Hashing: A common approach to detect duplicates is to generate a hash for each document's content. If two documents have the same hash, they are considered duplicates. A cryptographic hash function like MD5 or SHA-256 can be used for this purpose.

Shingling: To reduce the computational cost, instead of hashing the entire document, we can hash small parts of it (shingles) and compare those. If a certain percentage of shingles match, the documents are considered duplicates.

MinHash and Locality-Sensitive Hashing (LSH): To further optimize the process, techniques like MinHash and LSH can be used. MinHash reduces the dimensionality of the data, and LSH helps in bucketing similar items together.

**Case where not all data can be loaded into memory**

- Storage: The hashes need to be stored for comparison. Given the large number of URLs, a distributed storage system like Hadoop HDFS or Google Cloud Storage could be used.
- we could divide the data into n buckets/partitions where x = hash(u) % n. Hence we can store data at bucket x in <x>.txt file through the use of a distributed file system
- we could use a distributed database like Cassandra or MongoDB to store the hashes

**Alternative**

- we could parallelise n machines to process the data and store the hashes in a distributed database. This may be faster and more scalable for large data but may be more expensive be overlly reliant on all n servers being up and running and perfectly in sync.

```
class DuplicateDetector:
    def __init__(self):
        self.storage = {}  # A distributed storage system

    def add_document(self, url, content):
        hash = self.hash_content(content)
        if hash in self.storage:
            print(f"Duplicate detected: {url} is a duplicate of {self.storage[hash]}")
        else:
            self.storage[hash] = url

    def hash_content(self, content):

        pass
```
