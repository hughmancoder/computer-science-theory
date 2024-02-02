use sql_store;
-- combines every record in table A with every record in table B 
-- Use for example where we have a product table and a colour table and we want each product to attain every color from the color table

-- Explicit syntax (preferred(
SELECT sh.name as shipper, p.name as product
FROM shippers sh
CROSS JOIN products p
ORDER BY sh.name

-- Implicit syntax
-- SELECT sh.name as shipper, p.name as product
-- FROM shippers sh, products p
-- ORDER BY sh.name