USE sql_invoicing;

SELECT p.date, p.invoice_id, p.amount, c.name AS 'client_name', pm.name FROM payments p
JOIN clients c 
ON p.client_id = c.client_id
JOIN payment_methods pm 
ON p.payment_method = pm.payment_method_id.     