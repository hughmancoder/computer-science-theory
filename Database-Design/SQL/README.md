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
