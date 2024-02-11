-- Delete row in a database (be careful when executing this)
DELETE FROM invoices 
WHERE client_id = 
	(SELECT client_id FROM clients
	WHERE name = 'Myworks')
    
-- Restore a row in a database