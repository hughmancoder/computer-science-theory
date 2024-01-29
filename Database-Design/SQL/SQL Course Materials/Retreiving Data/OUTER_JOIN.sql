-- Left join, returns all conditions from left table whether they are true or night. Vice versa for right join. LEFT OUTER -> LEFT (outer syntax is optional)

-- Outer join between two tables
SELECT 
p.product_id, p.name, oi.quantity
FROM products p
LEFT JOIN order_items oi
ON p.product_id = oi.product_id