-- Union command combines multiple queries
SELECT 
	order_id, 
	order_date, 
	'Active' as status 
FROM orders
WHERE order_date >= '2019-01-01'
UNION
SELECT 
	order_id, 
	order_date, 
	'Archive' as status 
FROM orders
WHERE order_date < '2019-01-01'