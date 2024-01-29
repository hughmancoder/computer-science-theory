SELECT 
	o.order_date,
    o.order_id,
    c.first_name,
    sh.name as "shipper",
    os.name as "status"
FROM customers c
JOIN orders o
	ON c.customer_id = o.customer_id
LEFT JOIN shippers sh
	ON o.shipper_id = sh.shipper_id
JOIN order_statuses os
	ON os.order_status_id = o.status
ORDER BY sh.name