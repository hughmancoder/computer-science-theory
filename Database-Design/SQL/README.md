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

#### Explicit Join

```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```

#### Implicit Join

```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders, Customers
WHERE Orders.CustomerID = Customers.CustomerID;
```

## Normalized Databases

- **Focus:** Data integrity and avoiding redundancy.
- **Structure:** Data split into multiple, smaller tables connected by relationships (like keys).
- **Pros:**
  - Less wasted space with minimal repetition.
  - Easier to make changes without causing inconsistencies.
- **Cons:**
  - Retrieving data can be slower due to joining multiple tables.

**Example:** An online store

- **Customer Table:** customer_id, name, address
- **Product Table:** product_id, name, price, description
- **Order Table:** order_id, customer_id, date
- **Order Items Table:** order_id, product_id, quantity

## Denormalized Databases

- **Focus:** Faster reads and performance.
- **Structure:** Duplicate data intentionally introduced, often by combining information from various tables.
- **Pros:**
  - Queries simpler and faster, often needing fewer joins.
- **Cons:**
  - More storage space used due to redundancy.
  - Higher risk of data inconsistencies if updates aren't carefully managed.

**Example:** Report generation for the online store.

- **Denormalized Order Report Table:** order_id, customer_name, product_name, quantity, price, date

## The Main Trade-off

Normalization offers the tidiest data structure with strong integrity, while denormalization sacrifices some tidiness for speedier reading.

## When to Choose

- **Normalized:** If data consistency and frequent updates are top priorities, normalization is usually best. Think of systems like online stores, banking systems, etc.

- **Denormalized:** If blazing-fast data retrieval for reports or analysis outweighs some redundancy, denormalization might be necessary. Examples include data warehouses and analytical systems.

**Important Note:** It's often not an "either/or" situation. Modern databases frequently use a hybrid approach – core data stays normalized for integrity, and specific denormalized structures are designed for performance-critical areas.

## Relational Database Design

Normalization: The process of structuring your database to reduce redundancy and data anomalies. Consider aiming for at least Third Normal Form (3NF). Here's a primer on normalization forms:

1NF (First Normal Form): Each cell holds a single value, and there are no repeating groups of columns.
2NF (Second Normal Form): Meets 1NF criteria and any non-key attributes are fully dependent on the entire primary key, not just part of it.
3NF (Third Normal Form): Meets 2NF criteria and removes any transitive dependencies (columns depending on non-key columns).
Understand Relationships: Carefully analyze the connections between your data entities. The main relationship types are:

One-to-One: A single record in one table corresponds to a single record in another.
One-to-Many: A single record in one table can relate to multiple records in another.
Many-to-Many: Multiple records in one table relate to multiple records in another. This often requires a junction table to implement.
Indexing: Judiciously apply indexes to columns involved in frequent searching, sorting, and joining. Indexes speed up retrieval but can slightly slow down data changes.

Referential Integrity: Enforce this through foreign key constraints. This ensures data consistency across tables (e.g., preventing an order from being created for a non-existent customer).

## SQL Tips

Clear Formatting: Use indentation and spacing to increase query readability.
Specific Column Selection: Rather than SELECT \*, explicitly list the columns you need. This leads to less network traffic and improved performance.
Efficient JOINs: Select the correct join type (INNER, OUTER, LEFT, RIGHT) depending on the desired result set.
WHERE Clause Filtering: Employ WHERE effectively to isolate the required data.
EXPLAIN Statement: Use EXPLAIN or its equivalent in your database system to analyze query execution plans and identify optimization opportunities.
Additional Best Practices

Thorough Documentation: Maintain organized documentation detailing the schema, table relationships, and design decisions.
Naming Conventions: Implement a consistent naming system for tables, columns, and constraints to make your database understandable.
Data Types: Select appropriate data types based on the nature of the data being stored to optimize storage and performance.
