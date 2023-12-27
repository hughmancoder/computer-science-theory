# Pastebin

- **Description**: Designing a system like Pastebin for generating random URLs to access user-entered text.
- **Considerations**: URL generation and text storage.

## About

A Pastebin-like service allows users to store and share plain text through a specific URL. This system needs to generate a unique URL for each new piece of text and retrieve the text when the URL is accessed.

## Constraints and assumptions

- System does not support user accounts or editing documents
- System tracks analytics of how many times a page has been accessed
- Old documents expunge

## Design considerations

URL Generation: The system needs to generate a unique URL for each new piece of text. This could be done by generating a random string or by using a unique identifier like a UUID. This could be mapped by adding an addiontional route on the pastebin server to correspond to this mapping

Text Storage: The system needs to store the text associated with each URL. This could be done using a database or a key-value store.

Data Retrieval: The system needs to retrieve the text when the URL is accessed. This involves looking up the URL in the storage system and returning the associated text.

Expiration: Optionally, the system could allow the text to expire after a certain period of time or after it has been accessed a certain number of times. I could use an additional priority queue with key/timestamp maps to keep track of when a document should be deleted. I could also use a priority queue to keep track of the most accessed documents and delete the least accessed documents when the queue is full to assign an system ranking

## Implementation template

```
class Pastebin:
    def __init__(self):
        self.storage = {}  # Key: url, Value: text

    def store_text(self, text):
        url = self.generate_url()
        self.storage[url] = text
        return url

    def retrieve_text(self, url):
        return self.storage.get(url, None)

    def generate_url(self):
        # Generate a unique URL
        pass
```
