# File System Design

## Algorithms

**1. Creating a File:**

- Find the target directory using path traversal.
- Create a new `File` object.
- Add the file to the directory's `files` map.

**2. Reading a File:**

- Locate the file using path traversal.
- Return its content.

**3. Writing to a File:**

- Find the file.
- Replace its content with the new data.

**4. Creating a Directory:**

- Find the parent directory.
- Create a new `Directory` object.
- Add the directory to the parent's `subDirectories` map.

**5. Listing Directory Contents:**

- Retrieve and return a list of names of files and subdirectories within a directory.

## Additional Considerations

**- Metadata:** - Store file metadata using additional fields in the `File` and `Directory` classes.

**- Error Handling:** - Implement robust error handling for invalid paths, file/directory existence checks, and resource constraints.

**- Persistence:** - Consider using serialization to save the in-memory file system to disk.

**- Performance Optimization:** - Explore techniques like caching and indexing for larger file systems.
