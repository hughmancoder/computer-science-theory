SELECT 
	customer_id,
    first_name, 
    points, 
    'Gold' as type
FROM customers where points > 3000
UNION
SELECT 
	customer_id, 
    first_name, 
    points, 'SILVER' as type
FROM customers where points between 2000 AND 3000
UNION
SELECT 
	customer_id, 
    first_name, 
    points, 
    'BRONZE' as type
FROM customers where points < 2000
ORDER BY first_name