-- Delete row in a database (be careful when executing this). Removing where deletes entire database

DELETE FROM invoices 
WHERE client_id = 
	(SELECT client_id FROM clients
	WHERE name = 'Myworks')
