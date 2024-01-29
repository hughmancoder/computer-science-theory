-- ^ beggining
-- $ end
-- | logical or
-- [abcd] denotes a list of potential characters which can be present. e.g: [gim]e means any g, i or m can come directly before e
-- [a-z] denotes a range of characters

SELECT * 
FROM customers
WHERE last_name REGEXP 'b[ru]'
-- WHERE first_name REGEXP 'elka|ambur')
-- WHERE last_name REGEXP '^my|se'
-- WHERE last_name REGEXP 'ey$|on$'

