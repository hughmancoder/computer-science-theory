# Web Crawler

- **Description**: Designing a web crawler while avoiding infinite loops.
- **Considerations**: Crawling strategy to prevent infinite loops.

## About

A web crawler, also known as a spider or spiderbot, is an internet bot that systematically browses the World Wide Web for the purpose of web indexing (web spidering). Web search engines and some other sites use web crawling or spidering software to update their web content or indices of others sites' web content.

## Design Considerations

The main challenge in designing a web crawler is to make it behave in a polite and reasonable manner, and avoid getting into infinite loops. This involves several aspects:

- URL Normalization: URLs need to be normalized so that the crawler doesn't visit the same page more than once. This involves converting the URL into a standard format.

- Robots.txt: A web crawler should respect the rules set out in the robots.txt file of a website. This file tells the crawler which parts of the website should not be crawled.

- Crawl Depth: The crawler should have a maximum crawl depth to prevent infinite loops in the case of circular links.

- Rate Limiting: The crawler should not overload any server by making too many requests in a short amount of time. This can be controlled by introducing a delay between consecutive requests.

- Duplicate Content: The crawler should be able to detect and avoid duplicate content to save resources

## High level implementation

```
class WebCrawler:
    def __init__(self):
        self.visited_urls = set()

    def crawl(self, url, max_depth):
        self._crawl([url], self.visited_urls, max_depth)

    def _crawl(self, urls, visited, max_depth):
        if max_depth == 0:
            return
        next_urls = []
        for url in urls:
            if url not in visited:
                visited.add(url)
                print(f"Crawling: {url}")
                links = self.get_links(url)
                next_urls.extend(links)
        self._crawl(next_urls, visited, max_depth - 1)

    def get_links(self, url):
        # Fetch the content of the url and extract the links
        pass
```
