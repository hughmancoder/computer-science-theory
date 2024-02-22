# System Design for Fetching End-of-Day Stock Price Information

- **Description**: Building a service for up to 1,000 client applications to fetch simple end-of-day stock price information.
- **Considerations**: Data storage format, client-facing service design, development, rollout, monitoring, and maintenance.

## Data Storage

- **Format:** JSON

  - Human-readable and easily parsed by various programming languages.
  - Efficient for transferring over networks.
  - Flexible structure for potential future additions.

```json
{
  "stocks": [
    {
      "symbol": "AAPL",
      "date": "2022-03-01",
      "open": 174.81,
      "high": 175.67,
      "low": 172.85,
      "close": 174.07,
      "volume": 63856664
    },
    {
      "symbol": "GOOGL",
      "date": "2022-03-01",
      "open": 2720.2,
      "high": 2725.6,
      "low": 2678.14,
      "close": 2695.79,
      "volume": 1402115
    }
    // More stock data here
  ]
}
```

- Alternative: XML

```xml
<stocks>
    <stock>
        <symbol>AAPL</symbol>
        <date>2022-03-01</date>
        <open>174.81</open>
        <high>175.67</high>
        <low>172.85</low>
        <close>174.07</close>
        <volume>63856664</volume>
    </stock>
    <stock>
        <symbol>GOOGL</symbol>
        <date>2022-03-01</date>
        <open>2720.20</open>
        <high>2725.60</high>
        <low>2678.14</low>
        <close>2695.79</close>
        <volume>1402115</volume>
    </stock>
</stocks>
```

- **Database:** MySQL
  - Mature, open-source, and widely supported relational database.
  - Handles structured data effectively.
  - Offers ACID (Atomicity, Consistency, Isolation, Durability) guarantees for reliability.
  - Optimized for storing large datasets and frequent read operations.

## Client-Facing Service Design

- **API Endpoints:**
  - `GET /stock/{id}`: Retrieves end-of-day price for a specific stock id/symbol.
  - `GET /stocks`: Retrieves end-of-day prices for a list of specified symbols.
- **Authentication and Authorization:**
  - Implement API keys or OAuth for secure access control.
- **Rate Limiting:**
  - Prevent excessive requests with a rate-limiting mechanism.
- **Error Handling:**
  - Provide informative error messages for invalid requests or data issues.

## Rollout

- **Deployment:**
  - Choose a suitable cloud platform (AWS, Azure, GCP) or on-premise infrastructure.
  - Consider load balancing and scaling strategies for potential high traffic (not needed for 1000 clients)
- **Monitoring:**
  - Set up metrics for server health, API response times, error rates, and usage patterns.
  - Utilize logging for debugging and auditing
