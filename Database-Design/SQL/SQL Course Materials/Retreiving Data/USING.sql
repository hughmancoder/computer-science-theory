use sql_invoicing;

SELECT p.date, c.name as client, p.amount, pm.name as payment_method
FROM payments p
JOIN clients c
USING (client_id)
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id
