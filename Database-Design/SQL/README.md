# Databases

## Relational (SQL)

- stores data in linked tables via references
- RDBMS: Oracle, MySQL, SQLServer

## Non-relational

- doesn't understand SQL

## ACID database properties

1. **Atomicity:**

   - All operations within a transaction either complete fully or fail entirely, leaving the database in a consistent state.
   - There are no partial transactions.
   - Example: In a bank transfer, both debiting one account and crediting another must succeed for the transaction to be valid.

2. **Consistency:**

   - Every transaction brings the database from one valid state to another, preserving its integrity and constraints.
   - Data remains consistent with defined rules and relationships.
   - Example: A database with a constraint that account balances cannot be negative will reject transactions that violate this rule.

3. **Isolation:**

   - Concurrent transactions are isolated from each other, preventing them from interfering with each other's results.
   - Each transaction operates as if it's the only one accessing the database.
   - Example: If two users try to update the same record simultaneously, isolation ensures only one change takes effect, avoiding conflicts.

4. **Durability:**
   - Once a transaction is committed, its changes are permanent and survive system failures or crashes.
   - Data is persisted even in the event of power outages or other disruptions.
   - Example: If a transaction completes successfully, even if the system abruptly shuts down, the database will recover with the committed changes intact.

**ACID properties are essential for ensuring:**

- Data integrity and reliability
- Accurate and consistent results
- Prevention of data corruption
- Safeguarding against errors and failures
- Enabling complex operations without compromising data integrity

### Implicit vs explicit joins

These two statements are equivalent, and it's a matter of personal preference which one you choose

**Explicit Join**

```
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```

**Implicit Join**

```
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders, Customers
WHERE Orders.CustomerID = Customers.CustomerID;
```

### Normalized vs Denormalised databases

Normalized Databases

Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like Insertion, Update and Deletion Anomalies. Normalization rules divide larger tables into smaller tables and link them using relationships. The purpose of Normalization is to eliminate redundant (useless) data and ensure data is stored logically.

Normalized databases are ideal when the application requires complex transactions and data integrity is critical. They are also beneficial when the data structure is complex and needs to be able to handle a variety of queries.

Denormalized Databases

Denormalization is a strategy used on a previously-normalized database to increase performance. In computing, denormalization is the process of trying to improve the read performance of a database, at the expense of losing some write performance, by adding redundant copies of data or by grouping data.

Denormalized databases are often used in data warehousing and big data scenarios, where read performance and analytical capabilities are more important than write performance. They are also used when the data structure is simple and the types of queries to be performed are known in advance.
