use sql_store;
-- Default generates a unique value for the customer id, since we have specified columns this is implicit
INSERT INTO customers (
	first_name,
    last_name,
    birth_date,
    address,
    city,
    state)
VALUES (
	'Hugh',
    'Signoriello',
    '2002-05-21',
    'Address',
    'Adelaide',
    'SA'
	)
