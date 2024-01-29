-- Get customters whose addresses contain TRAIL or AVENUE
SELECT * 
FROM customers
WHERE address LIKE '%TRAIL%' OR
	  address LIKE '%AVENUE%'