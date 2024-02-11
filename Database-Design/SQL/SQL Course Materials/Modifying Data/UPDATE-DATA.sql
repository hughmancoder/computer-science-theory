USE sql_store;

UPDATE customers
SET points = 50
WHERE birth_date < '1990-01-01'


